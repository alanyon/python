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

from bisect import bisect_right

import numpy as np
from airfields_and_thresholds import define_thresholds


class cloud(object):

    """Class for checking cloud components of tafs against metars."""

    def __init__(self, airfield):

        _, self.cloud_thresholds = define_thresholds(
            rules=airfield["rules"], helicopter=airfield["helicopter"]
        )
        self.rules = airfield["rules"]

        if self.rules == "civil":
            self.cavok_groups = ["CAVOK", "FEW", "SCT"]
            self.significant_groups = ["BKN", "OVC"]
            self.significant_height = 14
        else:
            self.cavok_groups = ["CAVOK", "FEW"]
            self.significant_groups = ["SCT", "BKN", "OVC"]
            self.significant_height = 24

    def check(self, base_cloud, tempo_cloud, metar_cloud):

        cloud_ok, cloud_ok_base, cloud_ok_tempo = True, True, True

        all_taf_cloud = base_cloud + tempo_cloud

        some_cloud_groups = ["FEW", "SCT", "BKN", "OVC", "VV///"]

        # Dealing with CAVOK
        # Check if CAVOK in metar, is there significant cloud in taf base,
        # with any allowances in tempo.
        if self.rules == "civil":
            if metar_cloud[0] == "CAVOK" and any(
                sig_cloud in base_item
                for base_item in base_cloud
                for sig_cloud in self.significant_groups
            ):
                cloud_ok, cloud_ok_base = False, False
                for item in self.cavok_groups:
                    if any(item in c_item for c_item in tempo_cloud):
                        cloud_ok = True
                        break
                    else:
                        cloud_ok_tempo = False

            # Check if any significant cloud in metar, but TAF has CAVOK, with
            # any allowances.
            if any("CAVOK" in item for item in all_taf_cloud) and any(
                sig_cloud in metar_item
                for metar_item in metar_cloud
                for sig_cloud in self.significant_groups
            ):
                cloud_ok = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in all_taf_cloud):
                        cloud_ok = True
                        break

            # Same for just base conditions.
            if any("CAVOK" in item for item in base_cloud) and any(
                sig_cloud in metar_item
                for metar_item in metar_cloud
                for sig_cloud in self.significant_groups
            ):
                cloud_ok_base = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in base_cloud):
                        cloud_ok_base = True
                        break

            # Same for just TEMPOs.
            if any("CAVOK" in item for item in tempo_cloud) and any(
                sig_cloud in metar_item
                for metar_item in metar_cloud
                for sig_cloud in self.significant_groups
            ):
                cloud_ok_tempo = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in tempo_cloud):
                        cloud_ok_tempo = True
                        break

        # For military TAFs we need to check if CB have been reported in a
        # METAR but not allowed for in the TAF.
        if self.rules == "military":
            if any("CB" in item for item in metar_cloud):
                if not any("CB" in item for item in all_taf_cloud):
                    cloud_ok = False
                if not any("CB" in item for item in base_cloud):
                    cloud_ok_base = False
                if not any("CB" in item for item in tempo_cloud):
                    cloud_ok_tempo = False

        # Dealing with significant cloud heights.
        # Extract the significant clouds.
        metar_significant_cloud = []
        taf_significant_cloud = []
        base_significant_cloud = []
        tempo_significant_cloud = []

        # Identify BKN, OVC, or sky obscured amounts of cloud.
        for item in metar_cloud:
            if any(sig_cloud in item for sig_cloud in self.significant_groups):
                metar_significant_cloud.append(int(item[3:6]))
            if "VV" in item:
                metar_significant_cloud.append(int(0))
        for item in all_taf_cloud:
            if any(sig_cloud in item for sig_cloud in self.significant_groups):
                taf_significant_cloud.append(int(item[3:6]))
            if "VV" in item:
                taf_significant_cloud.append(int(0))
        for item in base_cloud:
            if any(sig_cloud in item for sig_cloud in self.significant_groups):
                base_significant_cloud.append(int(item[3:6]))
            if "VV" in item:
                base_significant_cloud.append(int(0))
        for item in tempo_cloud:
            if any(sig_cloud in item for sig_cloud in self.significant_groups):
                tempo_significant_cloud.append(int(item[3:6]))
            if "VV" in item:
                tempo_significant_cloud.append(int(0))

        if self.rules == "military":
            if metar_cloud[0] == "CAVOK" and any(
                np.array(taf_significant_cloud) < self.significant_height
            ):
                cloud_ok = False
                for item in self.cavok_groups:
                    if any(item in c_item for c_item in tempo_cloud):
                        cloud_ok = True
                        break
            # Just base conditions and TEMPOs
            if metar_cloud[0] == "CAVOK" and any(
                np.array(base_significant_cloud) < self.significant_height
            ):
                cloud_ok_base = False
                for item in self.cavok_groups:
                    if not any(item in c_item for c_item in tempo_cloud):
                        cloud_ok_tempo = False
                        break

            # Check if any significant cloud in metar, but TAF has CAVOK, with
            # any allowances.
            if any("CAVOK" in item for item in all_taf_cloud) and any(
                np.array(metar_significant_cloud) < self.significant_height
            ):
                cloud_ok = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in all_taf_cloud):
                        cloud_ok = True
                        break
            # Just for base conditions
            if any("CAVOK" in item for item in base_cloud) and any(
                np.array(metar_significant_cloud) < self.significant_height
            ):
                cloud_ok_base = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in base_cloud):
                        cloud_ok_base = True
                        break
            # Just for TEMPOs
            if any("CAVOK" in item for item in tempo_cloud) and any(
                np.array(metar_significant_cloud) < self.significant_height
            ):
                cloud_ok_tempo = False
                for item in some_cloud_groups:
                    if any(item in c_item for c_item in tempo_cloud):
                        cloud_ok_tempo = True
                        break

        # Sort significant cloud in metar and tempo groups in height ascending
        # order.
        metar_significant_cloud = sorted(metar_significant_cloud)
        tempo_significant_cloud = sorted(tempo_significant_cloud)
        taf_significant_cloud = sorted(taf_significant_cloud)
        base_significant_cloud = sorted(base_significant_cloud)

        # Significant cloud below the significant height in metar, and no
        # corresponding group in the TAF
        if self.sig_low_cloud(metar_significant_cloud) and not self.sig_low_cloud(
            taf_significant_cloud
        ):
            cloud_ok = False
        # Just base conditions
        if self.sig_low_cloud(metar_significant_cloud) and not self.sig_low_cloud(
            base_significant_cloud
        ):
            cloud_ok_base = False
        # Just TEMPOs
        if tempo_significant_cloud:
            if self.sig_low_cloud(metar_significant_cloud) and not self.sig_low_cloud(
                tempo_significant_cloud
            ):
                cloud_ok_tempo = False

        # Check base condition specific rules (significant cloud below the
        # relevant height with nothing equivalent in metar).
        if self.sig_low_cloud(base_significant_cloud) and not self.sig_low_cloud(
            metar_significant_cloud
        ):
            cloud_ok, cloud_ok_base = False, False
            # Allow for taf containing temporary improvement  group
            # (e.g. TEMPO SCT014, TEMPO CAVOK, TEMPO BKN016)
            if tempo_cloud:
                for item in self.cavok_groups:
                    if any(item in c_item for c_item in tempo_cloud):
                        cloud_ok = True
                    else:
                        cloud_ok_tempo = False
                if tempo_significant_cloud:
                    if tempo_significant_cloud[0] > self.significant_height:
                        cloud_ok = True
                    else:
                        cloud_ok_tempo = False

        # Checking for cloud group heights when significant low cloud is
        # present in TAF and METAR
        if self.sig_low_cloud(metar_significant_cloud) and self.sig_low_cloud(
            taf_significant_cloud
        ):
            [cloud_min, cloud_max] = self.lookup_clouds(taf_significant_cloud)

            # METAR cloud below lowest allowed height.
            if metar_significant_cloud[0] < cloud_min:
                cloud_ok = False

            # Just for base conditions
            if base_significant_cloud:
                [cloud_min_base,
                 cloud_max_base] = self.lookup_clouds(base_significant_cloud)
                if metar_significant_cloud[0] < cloud_min_base:
                    cloud_ok_base = False

            # Just for TEMPOs
            if tempo_significant_cloud:
                [cloud_min_tempo,
                 cloud_max_tempo] = self.lookup_clouds(tempo_significant_cloud)
                if metar_significant_cloud[0] < cloud_min_tempo:
                    cloud_ok_tempo = False

            # METAR cloud above highest allowed in TAF.
            if (
                cloud_max <= 15
                and metar_significant_cloud[0] >= cloud_max
                and base_significant_cloud
            ):
                cloud_ok, cloud_ok_base = False, False
                if tempo_cloud:
                    for item in self.cavok_groups:
                        if any(item in c_item for c_item in tempo_cloud):
                            cloud_ok = True
                        else:
                            cloud_ok_tempo = False
                if tempo_significant_cloud:
                    if tempo_significant_cloud[0] > self.significant_height:
                        cloud_ok = True
                    else:
                        cloud_ok_tempo = False

        return cloud_ok, cloud_ok_base, cloud_ok_tempo

    def sig_low_cloud(self, cloud_in):
        if cloud_in and cloud_in[0] <= self.significant_height:
            return True
        else:
            return False

    # Return cloud ranges.
    def lookup_clouds(self, taf_significant_cloud):
        taf_min = taf_significant_cloud[0]
        taf_max = taf_significant_cloud[-1]

        cloud_min = self.cloud_thresholds[
            bisect_right(self.cloud_thresholds, taf_min) - 1
        ]

        # Handle TAFs with an 050 height cloud group.
        if taf_max >= self.cloud_thresholds[-1]:
            cloud_max = self.cloud_thresholds[-1]
        else:
            cloud_max = self.cloud_thresholds[
                bisect_right(self.cloud_thresholds, taf_max)
            ]

        return cloud_min, cloud_max
