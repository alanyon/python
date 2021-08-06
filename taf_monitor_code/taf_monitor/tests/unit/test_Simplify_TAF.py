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

import copy
import unittest
from datetime import datetime as dt

from taf_monitor.constants import condition_type
from taf_monitor.taf_interpretation import Interpret_TAF, Simplify_TAF
from taf_monitor.utilities import DefineConditionsDictionary

TAF_raw = [
    "EGTE",
    "131100Z",
    "1312/1412",
    "30010KT",
    "9999",
    "FEW040",
    "BECMG",
    "1315/1318",
    "24012KT",
    "PROB40",
    "TEMPO",
    "1318/1321",
    "8000",
    "-SHRA",
    "BKN014",
    "PROB30",
    "1321/1324",
    "0300",
    "FG",
    "BKN001",
]


class test_Simplify_TAF_by_group(unittest.TestCase):
    def test_prob_group_conversion(self):
        """
        PROB## and PROB## TEMPO  groups are changed to tempo groups as they
        are equivalent from a TAF validity perspective.

        """
        simplified_TAF = Simplify_TAF().by_group(TAF_raw)

        msg = "'PROB40' is not in list"
        with self.assertRaisesRegex(ValueError, msg):
            simplified_TAF.index("PROB40")
        msg = "'PROB30' is not in list"
        with self.assertRaisesRegex(ValueError, msg):
            simplified_TAF.index("PROB30")


class test_Simplify_TAF_get_valid_tempo_groups(unittest.TestCase):
    def setUp(self):
        self.year, self.month, self.day = 2017, 6, 13
        self.simplified_TAF = Simplify_TAF().by_group(TAF_raw)
        self.tempo_change_dictionary = DefineConditionsDictionary().create(
            condition_type
        )
        (
            self.becmg_groups,
            self.tempo_groups,
            self.change_groups,
        ) = Interpret_TAF().get_all_indices(self.simplified_TAF)

    def test_get_valid_tempo_groups_none(self):

        # METAR 1150Z 13/06/2017 - Expect no tempo groups to be in effect.
        metar_time = dt(self.year, self.month, self.day, 12, 0)

        self.tempo_change_dictionary = Simplify_TAF().get_valid_tempo_groups(
            self.simplified_TAF,
            self.tempo_groups,
            metar_time,
            self.change_groups,
            self.tempo_change_dictionary,
            condition_type,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )
        expected = DefineConditionsDictionary().create(condition_type)
        self.assertDictEqual(self.tempo_change_dictionary, expected)

    def test_get_valid_tempo_groups_prob40_tempo(self):

        # METAR 1850Z 13/06/2017 - Expect prob40 tempo group to be in effect.
        metar_time = dt(self.year, self.month, self.day, 19, 0)

        self.tempo_change_dictionary = Simplify_TAF().get_valid_tempo_groups(
            self.simplified_TAF,
            self.tempo_groups,
            metar_time,
            self.change_groups,
            self.tempo_change_dictionary,
            condition_type,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )
        expected = DefineConditionsDictionary().create(condition_type)
        expected["visibility"] = ["8000"]
        expected["cloud"] = ["BKN014"]

        self.assertDictEqual(self.tempo_change_dictionary, expected)

    def test_get_valid_tempo_groups_prob30(self):

        # METAR 2150Z 13/06/2017 - Expect prob30 group to be in effect.
        metar_time = dt(self.year, self.month, self.day, 22, 0)

        self.tempo_change_dictionary = Simplify_TAF().get_valid_tempo_groups(
            self.simplified_TAF,
            self.tempo_groups,
            metar_time,
            self.change_groups,
            self.tempo_change_dictionary,
            condition_type,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )
        expected = DefineConditionsDictionary().create(condition_type)
        expected["visibility"] = ["0300"]
        expected["cloud"] = ["BKN001"]
        expected["weather"] = ["FG"]

        self.assertDictEqual(self.tempo_change_dictionary, expected)


class test_Simplify_TAF_apply_becmg(unittest.TestCase):
    def setUp(self):
        self.year, self.month, self.day = 2017, 6, 13
        self.simplified_TAF = Simplify_TAF().by_group(TAF_raw)
        self.becmg_change_dictionary = DefineConditionsDictionary().create(
            condition_type
        )
        (
            self.becmg_groups,
            self.tempo_groups,
            self.change_groups,
        ) = Interpret_TAF().get_all_indices(self.simplified_TAF)

    def test_interpret_and_apply_becmg_none(self):
        # METAR 1150Z 13/06/2017 - Expect no becmg groups to have completed or
        # be in effect.
        metar_time = dt(self.year, self.month, self.day, 12, 0)

        (
            new_TAF,
            kill_list,
            self.becmg_change_dictionary,
        ) = Interpret_TAF().interpret_becmg_group(
            copy.copy(self.simplified_TAF),
            self.becmg_groups,
            metar_time,
            self.change_groups,
            self.becmg_change_dictionary,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )

        # TAF Unchanged by this routine
        self.assertEqual(new_TAF, self.simplified_TAF)
        # Indentified BECMG group as inactive adds indices of becmg elements
        # to kill list TAF[6], TAF[7], TAF[8]
        self.assertListEqual(kill_list, [6, 7, 8])

        # becmg_change_dictionary contains no entries.
        expected = DefineConditionsDictionary().create(condition_type)
        self.assertDictEqual(expected, self.becmg_change_dictionary)

    def test_interpret_and_apply_becmg_midway(self):
        # METAR 1550Z 13/06/2017 - Becmg group has not completed but the change
        # is in effect.
        metar_time = dt(self.year, self.month, self.day, 16, 0)

        (
            new_TAF,
            kill_list,
            self.becmg_change_dictionary,
        ) = Interpret_TAF().interpret_becmg_group(
            copy.copy(self.simplified_TAF),
            self.becmg_groups,
            metar_time,
            self.change_groups,
            self.becmg_change_dictionary,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )

        # TAF changed by this routine, the becmg group changed to a tempo.
        self.assertNotEqual(new_TAF, self.simplified_TAF)
        # Check the element is now a TEMPO group.
        self.assertEqual("TEMPO", new_TAF[6])

        # Nothing to remove, so kill_list should be empty.
        self.assertListEqual(kill_list, [])

        # becmg_change_dictionary contains no entries.
        expected = DefineConditionsDictionary().create(condition_type)
        self.assertDictEqual(expected, self.becmg_change_dictionary)

    def test_interpret_and_apply_becmg_complete(self):
        # METAR 1950Z 13/06/2017 - Becmg group has completed.
        metar_time = dt(self.year, self.month, self.day, 20, 0)

        (
            new_TAF,
            kill_list,
            self.becmg_change_dictionary,
        ) = Interpret_TAF().interpret_becmg_group(
            copy.copy(self.simplified_TAF),
            self.becmg_groups,
            metar_time,
            self.change_groups,
            self.becmg_change_dictionary,
            "EGTE",
            self.day,
            self.month,
            self.year,
        )


if __name__ == "__main__":
    unittest.main()
