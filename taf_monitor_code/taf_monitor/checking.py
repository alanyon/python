#!/usr/bin/python
# (C) British Crown Copyright 2018-2019 Met Office.
# All rights reserved.
#
# This file is part of TAF Monitor.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import platform
from datetime import datetime as dt
from datetime import timedelta as timedelta

from airfields_and_thresholds import define_airfields, define_benches
from cloud_check import cloud
from constants import condition_type
from data_retrieval import RetrieveObservations
from taf_interpretation import Interpret_TAF, Simplify_TAF
from time_functionality import ConstructTimeObject, Is_Time_Current
from utilities import DefineConditionsDictionary
from visibility_check import visibility
from weather_check import weather
from wind_check import wind


# Create dict type to contain airfield lists.
airfield_benches = define_benches()
all_airfields = define_airfields()


class CheckTafThread():

    def __init__(self, bench_selected, start_time, taf_start_time,
                 taf_end_time):
        self.bench_selected = bench_selected
        self.start_time = start_time
        self.taf_start_time = taf_start_time
        self.taf_end_time = taf_end_time

    def time_in_seconds(self, td):
        return (
            td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6
        ) / 10 ** 6

    @staticmethod
    def create_obs_list(airfields, start_time, taf_start_time, taf_end_time):

        GetObs = RetrieveObservations
        obs_list = []
        for icao in airfields:

            # get the metar in list form
            metars = GetObs(icao, "M", start_time, latest_only=False,
                            start_time=start_time,
                            end_time=taf_end_time).operation()

            # get the taf in list form
            tafs = GetObs(icao, "T", start_time, latest_only=False,
                          start_time=start_time,
                          end_time=taf_end_time).operation()

            # get any specials in list form
            specis = GetObs(icao, "S", start_time, latest_only=False,
                            start_time=start_time,
                            end_time=taf_end_time).operation()

            # Dodgy way to determine correct TAF to use
            use_taf = []
            for taf in tafs:

                # Move on to next TAF if no record
                if taf == "NoRecord" or 'CNL' in taf:
                    continue

                # Get start and end times of TAF
                [taf_start, taf_end] = ConstructTimeObject(
                    taf[2], taf_start_time.day, taf_start_time.month,
                    taf_start_time.year
                ).TAF()

                # If same as TAF being looked for, use it
                if taf_start == taf_start_time and taf_end == taf_end_time:
                    use_taf = taf
                    break

            # Move to next airport if no valid TAF
            if not use_taf:
                continue

            # Collect METARs and SPECIs into single list
            metars += specis

            # Remove METARs and SPECIs recorded as 'NoRecord'
            metars = [metar for metar in metars if metar != "NoRecord"]

            # Remove AUTO term from METARs and SPECIs as it has no value
            metars = [[ele for ele in metar if ele != 'AUTO']
                      for metar in metars]

            obs_list.append([icao, metars, use_taf])

        return obs_list

    def check_condition(self, function, condition, airfield):
        """
        Call the relevant checking plugin for a given condition (e.g. wind,
        cloud, etc). The taf_status is then updated relative to this condition.
        """
        (self.taf_status[condition],
         base_ok, tempo_ok) = function(airfield).check(
            self.base_conditions[condition],
            self.tempo_changes[condition],
            self.metar_conditions[condition],
        )

        return base_ok, tempo_ok

    def run(self):
        """
        ######################################
        #                                    #
        #            MAIN ROUTINE            #
        #                                    #
        ######################################
        Principle code that drives TAF Monitor once a bench has been selected.
        """
        airfields = airfield_benches[self.bench_selected]

        # String list to record details of broken tafs.
        summary = []
        metars_bust = []

        obs_list = self.create_obs_list(airfields, self.start_time,
                                        self.taf_start_time, self.taf_end_time)

        for ii, (icao, metars, taf) in enumerate(obs_list):

            for ind, metar in enumerate(metars):

                # Check if airfield is helicopter station.
                airfield = all_airfields[icao]

                # Simplify TAF groups to just BECMG and TEMPO.
                taf = Simplify_TAF().by_group(taf)

                print('')
                print('taf', taf)
                print('')

                # Get TAF validity time as python datetime object.
                [taf_start, taf_end] = ConstructTimeObject(
                    taf[2], self.start_time.day, self.start_time.month,
                    self.start_time.year
                ).TAF()
                # Get METAR issue time as python datetime object.
                metar_time = ConstructTimeObject(
                    metar[1][:-1], self.start_time.day, self.start_time.month,
                    self.start_time.year
                ).METAR()

                # Stops checking TAF if it is not currently valid.
                if not Is_Time_Current(taf_start, taf_end, metar_time).check():
                    continue

                # Get indices of different groups.
                [
                    becmg_groups,
                    tempo_groups,
                    change_groups,
                ] = Interpret_TAF().get_all_indices(taf)

                # Create dict types to contain conditions.
                self.metar_conditions = DefineConditionsDictionary().create(
                    condition_type
                )
                self.base_conditions = DefineConditionsDictionary().create(
                    condition_type
                )
                self.becmg_changes = DefineConditionsDictionary().create(condition_type)
                self.tempo_changes = DefineConditionsDictionary().create(condition_type)
                self.taf_status = DefineConditionsDictionary().create(condition_type)

                # Get base conditions of taf.
                self.base_conditions = Interpret_TAF().conditions(
                    taf[0 : change_groups[0]], self.base_conditions, icao
                )

                # Check becmg group status and modify taf.
                [
                    taf,
                    kill_list,
                    self.becmg_changes,
                ] = Interpret_TAF().interpret_becmg_group(
                    taf,
                    becmg_groups,
                    metar_time,
                    change_groups,
                    self.becmg_changes,
                    icao,
                    taf_start.day,
                    taf_start.month,
                    taf_start.year,
                )
                # Remove becmg groups that have not yet started.
                taf = Simplify_TAF().kill_elements(taf, kill_list)
                # Apply changes from completed becmg groups to the base
                # conditions.
                self.base_conditions = Simplify_TAF().apply_becmg(
                    self.base_conditions, self.becmg_changes, condition_type
                )

                # Remake indices for remaining tempo groups (all groups are now
                # of type tempo).
                [
                    becmg_groups,
                    tempo_groups,
                    change_groups,
                ] = Interpret_TAF().get_all_indices(taf)

                # Get tempo groups valid at current metar time.
                self.tempo_changes = Simplify_TAF().get_valid_tempo_groups(
                    taf,
                    tempo_groups,
                    metar_time,
                    change_groups,
                    self.tempo_changes,
                    condition_type,
                    icao,
                    taf_start.day,
                    taf_start.month,
                    taf_start.year,
                )
                # Extract current METAR conditions.
                self.metar_conditions = Interpret_TAF().conditions(
                    metar, self.metar_conditions, icao
                )
                # Check METAR has three essential components; wind, vis, cloud.
                # CAVOK dealt with in get_conditions.
                valid_metar = True
                for item_mt in ["wind", "visibility", "cloud"]:
                    if not self.metar_conditions[item_mt]:
                        valid_metar = False

                bust, base_bust = False, False

                # Calls a checking routine for each of the condition_type to
                # determine taf status.
                if valid_metar:
                    print('')
                    print('metar', metar)
                    print('')
                    (base_ok_wind,
                     tempo_ok_wind) = self.check_condition(wind, "wind",
                                                           airfield)
                    (base_ok_vis,
                     tempo_ok_vis) = self.check_condition(visibility,
                                                          "visibility",
                                                          airfield)
                    (base_ok_wx,
                     tempo_ok_wx) = self.check_condition(weather, "weather",
                                                         airfield)
                    (base_ok_cld,
                     tempo_ok_cld) = self.check_condition(cloud, "cloud",
                                                          airfield)

                    for item in condition_type:
                        if item == 'wind':
                            base_ok, tempo_ok = base_ok_wind, tempo_ok_wind
                        elif item == 'visibility':
                            base_ok, tempo_ok = base_ok_vis, tempo_ok_vis
                        elif item == 'visibility':
                            base_ok, tempo_ok = base_ok_wx, tempo_ok_wx
                        elif item == 'cloud':
                            base_ok, tempo_ok = base_ok_cld, tempo_ok_cld

                        cap_item = item.capitalize()
                        nice_time = metar_time.strftime('%H:%M')

                        if self.taf_status[item]:

                            if not base_ok:
                                msg = ('{} not covered by base conditions at '
                                       '{} but covered by TEMPO/PROB '
                                       'group'.format(cap_item, nice_time))
                                summary.append(msg)
                                base_bust = True
                        else:
                            # Indicate metar that bust TAF
                            bust = True

                            nice_time = metar_time.strftime('%H:%M')
                            msg = 'TAF bust by {} at {}'.format(item,
                                                                nice_time)
                            if not base_ok:
                                msg += ' (base conditions'
                                if not tempo_ok:
                                    msg += ' and TEMPO/PROB group)'
                                else:
                                    msg += ')'
                            elif not tempo:
                                msg += ' (TEMPO/PROB group)'

                            summary.append(msg)
                else:
                    summary.append(str(icao) + " METAR Invalid")

                metars_bust.append([metar, bust, base_bust])

            print('')
            print('------------------------------------------------')
            print('')

        return summary, metars_bust
