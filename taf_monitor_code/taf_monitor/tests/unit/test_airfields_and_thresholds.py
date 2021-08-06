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

from taf_monitor.airfields_and_thresholds import (
    define_airfields,
    define_benches,
    define_thresholds,
)


class test_define_thresholds(unittest.TestCase):
    def test_return_type(self):
        result = define_thresholds()
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    def test_list_lengths_non_helicopter(self):
        result = define_thresholds()
        self.assertEqual(len(result[0]), 7)
        self.assertEqual(len(result[1]), 6)

    def test_list_lengths_helicopter(self):
        result = define_thresholds(helicopter=True)
        self.assertEqual(len(result[0]), 9)
        self.assertEqual(len(result[1]), 7)


class test_define_benches(unittest.TestCase):
    def test_return_type(self):
        result = define_benches()
        self.assertIsInstance(result, dict)


class test_define_airfields(unittest.TestCase):
    def test_return_type(self):
        result = define_airfields()
        self.assertIsInstance(result, dict)

    def test_key_values(self):
        result = define_airfields()
        self.assertIsInstance(list(result.keys())[0], str)
        self.assertEqual(len(list(result.keys())[0]), 4)


if __name__ == "__main__":
    unittest.main()
