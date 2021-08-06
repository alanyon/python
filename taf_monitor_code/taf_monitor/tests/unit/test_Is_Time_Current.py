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

from taf_monitor.time_functionality import Is_Time_Current


class test_Is_Time_Current(unittest.TestCase):
    def setUp(self):
        self.year = 2017
        self.month = 6
        self.day = 15

    def test_time_within_limits(self):
        start_time = dt(self.year, self.month, self.day, 12, 00)
        end_time = dt(self.year, self.month, self.day, 18, 00)
        current_time = dt(self.year, self.month, self.day, 15, 00)

        self.assertTrue(Is_Time_Current(start_time, end_time, current_time).check())

    def test_time_outside_limits(self):
        start_time = dt(self.year, self.month, self.day, 12, 00)
        end_time = dt(self.year, self.month, self.day, 18, 00)
        current_time = dt(self.year, self.month, self.day, 19, 00)

        self.assertFalse(Is_Time_Current(start_time, end_time, current_time).check())

    def test_time_on_lower_limit(self):
        start_time = dt(self.year, self.month, self.day, 12, 00)
        end_time = dt(self.year, self.month, self.day, 18, 00)
        current_time = dt(self.year, self.month, self.day, 12, 00)

        self.assertTrue(Is_Time_Current(start_time, end_time, current_time).check())

    def test_time_on_upper_limit(self):
        start_time = dt(self.year, self.month, self.day, 12, 00)
        end_time = dt(self.year, self.month, self.day, 18, 00)
        current_time = dt(self.year, self.month, self.day, 18, 00)

        self.assertTrue(Is_Time_Current(start_time, end_time, current_time).check())

    def test_sending_junk(self):
        start_time = dt(self.year, self.month, self.day, 12, 00)
        end_time = dt(self.year, self.month, self.day, 18, 00)
        current_time = dt(self.year, self.month, self.day, 18, 00)

        msg = "Received invalid input: Not a datetime object."
        with self.assertRaisesRegex(ValueError, msg):
            Is_Time_Current(start_time, end_time, "junk").check()


if __name__ == "__main__":
    unittest.main()
