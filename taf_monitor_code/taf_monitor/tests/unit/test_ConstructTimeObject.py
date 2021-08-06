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

import unittest
from datetime import datetime as dt

from taf_monitor.time_functionality import ConstructTimeObject


class test_ConstructTimeObject(unittest.TestCase):

    # today_is_last_day_of_month

    def test_is_today_last_day_of_month_normal_year(self):
        initialisation_time = 1215 / 1815
        # Non-leap year
        year = 2015
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for month, day in zip(months, lengths):
            self.assertTrue(
                ConstructTimeObject(
                    initialisation_time, day, month, year
                ).is_today_last_day_of_month()
            )

    def test_is_today_last_day_of_month_leap_year(self):
        initialisation_time = 1215 / 1815
        # Leap year
        year = 2016
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for month, day in zip(months, lengths):
            self.assertTrue(
                ConstructTimeObject(
                    initialisation_time, day, month, year
                ).is_today_last_day_of_month()
            )

    # TAF

    def test_taf_time_group_midday(self):
        # Standard midmonth check.
        year, month, day, hour = 2017, 1, 15, 12
        taf_group = "1512/1612"
        expected_start = dt(year, month, day, hour, 0)
        expected_end = dt(year, month, day + 1, hour, 0)
        start_time, end_time = ConstructTimeObject(taf_group, day, month, year).TAF()
        self.assertEqual(expected_start, start_time)
        self.assertEqual(expected_end, end_time)

    def test_taf_time_group_end_of_month(self):
        # TAF checked on last day of month, with TAF starting the same day and
        # ending in the next month.
        year, month, day, hour = 2017, 1, 31, 12
        taf_group = "3112/0112"
        expected_start = dt(year, month, day, hour, 0)
        expected_end = dt(year, month + 1, 1, hour, 0)
        start_time, end_time = ConstructTimeObject(taf_group, day, month, year).TAF()
        self.assertEqual(expected_start, start_time)
        self.assertEqual(expected_end, end_time)

    def test_taf_time_group_start_of_month(self):
        # TAF checked on first day of month, with TAF starting the previous
        # month and ending today.
        year, month, day, hour = 2017, 2, 1, 12
        taf_group = "3112/0112"
        expected_start = dt(year, month - 1, 31, hour, 0)
        expected_end = dt(year, month, day, hour, 0)
        start_time, end_time = ConstructTimeObject(taf_group, day, month, year).TAF()
        self.assertEqual(expected_start, start_time)
        self.assertEqual(expected_end, end_time)

    def test_taf_time_group_end_of_year(self):
        # TAF checked on last day of year, with TAF starting the same day and
        # ending in the next year.
        year, month, day, hour = 2017, 12, 31, 12
        taf_group = "3112/0112"
        expected_start = dt(year, month, day, hour, 0)
        expected_end = dt(year + 1, 1, 1, hour, 0)
        start_time, end_time = ConstructTimeObject(taf_group, day, month, year).TAF()
        self.assertEqual(expected_start, start_time)
        self.assertEqual(expected_end, end_time)

    def test_taf_time_group_start_of_year(self):
        # TAF checked on first day of year, with TAF starting the previous
        # year and ending today.
        year, month, day, hour = 2017, 1, 1, 1
        taf_group = "3118/0103"
        expected_start = dt(2016, 12, 31, 18, 0)
        expected_end = dt(year, 1, 1, 3, 0)
        start_time, end_time = ConstructTimeObject(taf_group, day, month, year).TAF()
        self.assertEqual(expected_start, start_time)
        self.assertEqual(expected_end, end_time)

    # METAR

    def test_metar_time_midday(self):
        # Standard midmonth check.
        year, month, day, hour = 2017, 1, 15, 12
        metar_time = "151150Z"
        expected_time = dt(year, month, day, hour, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)

    def test_metar_time_midnight(self):
        # Midnight time check; should push a 2350Z ob to the next day as 00Z.
        year, month, day, hour = 2017, 1, 16, 0
        metar_time = "152350Z"
        expected_time = dt(year, month, day, hour, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)

    def test_metar_time_midnight_end_of_month_checked_before_midnight(self):
        # Midnight time check; should push a 2350Z ob to the next day and next
        # month as 00Z.
        year, month, day, hour = 2017, 1, 31, 0
        metar_time = "312350Z"
        expected_time = dt(year, month + 1, 1, 0, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)

    def test_metar_time_midnight_end_of_month_checked_after_midnight(self):
        # Midnight time check; should push a 2350Z ob to the next day and next
        # month as 00Z.
        year, month, day, hour = 2017, 2, 1, 0
        metar_time = "312350Z"
        expected_time = dt(year, month, day, 0, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)

    def test_metar_time_midnight_end_of_year_checked_before_midnight(self):
        # Midnight time check; should push a 2350Z ob to the next day and next
        # year as 00Z.
        year, month, day, hour = 2016, 12, 31, 0
        metar_time = "312350Z"
        expected_time = dt(year + 1, 1, 1, hour, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)

    def test_metar_time_midnight_end_of_year_checked_after_midnight(self):
        # Midnight time check; should push a 2350Z ob to the next day and next
        # year as 00Z.
        year, month, day, hour = 2017, 1, 1, 0
        metar_time = "312350Z"
        expected_time = dt(year, month, day, hour, 0)
        result_time = ConstructTimeObject(metar_time, day, month, year).METAR()
        self.assertEqual(expected_time, result_time)


if __name__ == "__main__":
    unittest.main()
