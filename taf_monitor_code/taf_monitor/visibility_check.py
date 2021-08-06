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

from airfields_and_thresholds import define_thresholds


class visibility(object):
    def __init__(self, airfield):

        self.vis_thresholds, _ = define_thresholds(
            rules=airfield["rules"], helicopter=airfield["helicopter"]
        )

    def check(self, base_visibility, tempo_visibility, metar_visibility):

        vis_ok = False

        # Check base and TEMPOs together
        visibilities = sorted(
            [int(item) for item in (base_visibility + tempo_visibility)]
        )
        [vis_min, vis_max] = self.lookup_visibilities(visibilities)

        vis_ok = vis_min <= int(metar_visibility[0]) < vis_max

        # Check just base
        vis_base = sorted(
            [int(item) for item in base_visibility]
        )
        [vis_min_base, vis_max_base] = self.lookup_visibilities(vis_base)

        vis_ok_base = vis_min_base <= int(metar_visibility[0]) < vis_max_base

        # Check just TEMPOs
        if tempo_visibility:

            vis_tempos = sorted(
                [int(item) for item in tempo_visibility]
            )
            [vis_min_tempo, vis_max_tempo] = self.lookup_visibilities(vis_tempos)

            vis_ok_tempo = vis_min_tempo <= int(metar_visibility[0]) < vis_max_tempo

        else:
            vis_ok_tempo = False

        return vis_ok, vis_ok_base, vis_ok_tempo

    # Return visibility ranges.
    def lookup_visibilities(self, visibilities):
        taf_min = visibilities[0]
        taf_max = visibilities[-1]

        vis_min = self.vis_thresholds[bisect_right(self.vis_thresholds, taf_min) - 1]
        vis_max = self.vis_thresholds[bisect_right(self.vis_thresholds, taf_max)]
        return vis_min, vis_max
