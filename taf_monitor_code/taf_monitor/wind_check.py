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

import weather_regex as wr


class wind(object):
    def __init__(self, airfield):

        if airfield["rules"] == "civil":
            self.wind_check = self.check_wind_conditionals
        else:
            self.wind_check = self.check_wind_conditionals_military

    def check(self, base_wind, tempo_wind, metar_wind):
        """
        Controlling routine for checking the wind terms.

        """
        wind_ok = True
        wind_angle = True
        [metar_angle, metar_mean, metar_gust] = self.wind_extract(metar_wind[0])

        # Check base conditions vs. metar.
        base_angle, base_mean, base_gust = self.wind_extract(base_wind[0])
        [wind_ok, wind_angle] = self.wind_check(
            metar_angle, metar_mean, metar_gust, base_angle, base_mean, base_gust
        )

        # Wind satisfied by base conditions, no further checking required.
        if wind_ok and wind_angle:
            if tempo_wind:
                return True, True, True
            else:
                return True, True, 'No TEMPO'

        # As angle and speed may be covered by two separate groups they must
        # be considered separately.
        wind_ok_base = wind_ok
        wind_angle_base = wind_angle

        # Implied (not wind_ok or not wind_angle) by if statement above.
        # Can the wind be saved by a tempo or becmg group?
        if tempo_wind:
            # wind_ok = True reset implied.
            # becmg group check.
            for item in tempo_wind:
                if "BEC" in item:
                    wind_ok = self.becmg_wind_test(
                        metar_angle,
                        metar_mean,
                        metar_gust,
                        base_angle,
                        base_mean,
                        base_gust,
                        *self.wind_extract(item),
                    )
                    # If in a becoming group, angle cannot bust the TAF, so
                    # only care about mean speed and gusts.
                    if wind_ok:
                        return True, True, True
            # tempo group check.
            for item in tempo_wind:
                [wind_ok, wind_angle] = self.wind_check(
                    metar_angle, metar_mean, metar_gust, *self.wind_extract(item)
                )
                # Tempo group satisfies wind speed and wind angle, or covers
                # one whilst the base covers the other.
                if (wind_ok or wind_ok_base) and (wind_angle or wind_angle_base):
                    return True, False, True

        # Base doesn't cover wind, and no tempo groups to save taf.
        if tempo_wind:
            return False, False, False
        else:
            return False, False, 'No TEMPO'

    # Break down wind term into component parts; angle, mean speed, gusts.
    def wind_extract(self, wind_in):
        wind_angle = wind_in[0:3]
        if wind_angle == "VRB":
            wind_angle = 999
        if wind_angle == "BEC":
            wind_angle = 888
        wind_angle = int(wind_angle)
        wind_mean = int(wind_in[3:5])
        if wr.GUST_TERM.search(wind_in):
            wind_gust = int(wind_in[6:8])
        else:
            wind_gust = wind_mean

        return wind_angle, wind_mean, wind_gust

    # The actual tests for the metar wind against the provided taf conditions.
    # This set of tests if for civil airfields.
    def check_wind_conditionals(
        self, metar_angle, metar_mean, metar_gust, other_angle, other_mean, other_gust
    ):
        wind_ok = True
        wind_angle = True
        # Check speeds.
        if abs(metar_mean - other_mean) >= 10:
            wind_ok = False
        if (
            metar_gust
            and abs(metar_gust - other_gust) >= 10
            and other_gust < metar_gust
            and (metar_mean >= 15 or other_mean >= 15)
        ):
            wind_ok = False
        # Check angles - all winds above 10kt.
        if not other_angle == 888:
            # Angle calculated such that e.g. (350 - 010) = 20
            angle_sep = abs(((metar_angle - other_angle) + 180) % 360 - 180)

            if (
                metar_mean >= 10
                and metar_mean < 20
                and other_mean < 20
                and angle_sep >= 60
            ):
                wind_angle = False
            if (
                other_mean >= 10
                and other_mean < 20
                and metar_mean < 20
                and angle_sep >= 60
            ):
                wind_angle = False
            if angle_sep >= 30 and (metar_mean >= 20 or other_mean >= 20):
                wind_angle = False

        # Check low speed winds.
        # if metar_angle == 999 and other_mean >= 10: wind_ok = False
        # if other_angle == 999 and metar_mean >= 10: wind_ok = False
        if metar_angle == 999 and not other_angle == 999 and other_mean >= 10:
            wind_ok = False

        return wind_ok, wind_angle

    # The actual tests for the metar wind against the provided taf conditions.
    # This set of tests if for military airfields.
    def check_wind_conditionals_military(
        self, metar_angle, metar_mean, metar_gust, other_angle, other_mean, other_gust
    ):
        wind_ok = True
        wind_angle = True
        # Check speeds - greater than 10kt difference in mean speed with the
        # speed before or after (in forecast or ob) being >=15kt.
        if metar_mean >= 15 or other_mean >= 15:
            if abs(metar_mean - other_mean) >= 10:
                wind_ok = False

            if (
                metar_gust
                and abs(metar_gust - other_gust) >= 10
                and other_gust < metar_gust
            ):
                wind_ok = False

            # Check angles - all winds above 10kt.
            if not other_angle == 888:
                # Angle calculated such that e.g. (350 - 010) = 20
                angle_sep = abs(((metar_angle - other_angle) + 180) % 360 - 180)

                if angle_sep >= 30:
                    wind_angle = False

        # Check low speed winds.
        # if metar_angle == 999 and other_mean >= 10: wind_ok = False
        # if other_angle == 999 and metar_mean >= 10: wind_ok = False
        # if (metar_angle == 999 and not other_angle == 999 and
        #        other_mean >= 10):
        #    wind_ok = False

        return wind_ok, wind_angle

    # becmg group test assumes that any angle is acceptable and only the speeds
    # matter.
    def becmg_wind_test(
        self,
        metar_angle,
        metar_mean,
        metar_gust,
        base_angle,
        base_mean,
        base_gust,
        other_angle,
        other_mean,
        other_gust,
    ):
        wind_ok = True
        forecast_means = sorted([base_mean, other_mean])
        if metar_mean < forecast_means[0] - 9 or metar_mean > forecast_means[-1] + 9:
            wind_ok = False
        if metar_gust and (metar_mean >= 15 or base_mean >= 15 or other_mean >= 15):
            forecast_gusts = sorted([base_gust, other_gust])
            if (
                abs(metar_gust - forecast_gusts[-1]) >= 10
                and forecast_gusts[-1] < metar_gust
            ):
                wind_ok = False

        if (
            metar_angle == 999
            and not (other_angle == 999 or base_angle == 999)
            and (other_mean >= 10 and base_mean >= 10)
        ):
            wind_ok = False

        return wind_ok
