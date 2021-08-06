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
from datetime import timedelta

from taf_monitor.data_retrieval import RetrieveObservations


class test_RetrieveObservations(unittest.TestCase):
    def setUp(self):
        self.ICAO = "EGCC"
        self.TORM = "T"
        self.current_date = dt.today()

    def test_record_request_type(self):
        self.assertEqual(
            RetrieveObservations(self.ICAO, "T", self.current_date).request_type(),
            "TAFS",
        )
        self.assertEqual(
            RetrieveObservations(self.ICAO, "M", self.current_date).request_type(),
            "METARS",
        )
        self.assertEqual(
            RetrieveObservations(self.ICAO, "S", self.current_date).request_type(),
            "SPECI",
        )
        msg = "Unknown record requested: Not TAF/METAR/SPECI"
        with self.assertRaisesRegex(ValueError, msg):
            RetrieveObservations(self.ICAO, "A", self.current_date).request_type()

    def test_metdb_address(self):
        metdb_address = (
            "http://mdbdb-prod/cgi-bin/moods/webret.pl?pageType="
            "mainpage&subtype={type}&system=mdbdb-prod&idType"
            "=ICAO&stn01={icao}&stn02=&stn03=&stn04=&stn05=&stn06"
            "=&stn07=&stn08=&stn09=&stn10={latest}&startdate={start_date}"
            "&starthour={start_hour:02d}&startminute=00"
            "&enddate={end_date}&endhour={end_hour:02d}&endminute=59&maxobs="
            "0500&header=no&area_n=&area_s=&area_w=&area_e="
        )
        self.assertEqual(
            RetrieveObservations(self.ICAO, self.TORM, self.current_date).metdb,
            metdb_address,
        )

    def test_invalid_ICAO_retrieval(self):
        ICAO = "NotAnAirport"
        self.assertEqual(
            RetrieveObservations(ICAO, self.TORM, self.current_date).operation(),
            ["NoRecord"],
        )

    def test_time_range_retrieval(self):
        """
        Check multiple TAFs are retrieved if latest_only is False and start
        and finish hours are provided.
        """
        start_time = self.current_date - timedelta(hours=24)
        end_time = self.current_date + timedelta(hours=1)
        result = RetrieveObservations(
            self.ICAO,
            self.TORM,
            self.current_date,
            latest_only=False,
            start_time=start_time,
            end_time=end_time,
        ).operation()
        self.assertTrue(len(result) > 1)

    def test_non_latest_without_range(self):
        """
        Check an error is raised if latest_only is False but start or finish
        hours are not provided.
        """
        msg = "For range retrieval a start_time and end_time must be specified"
        with self.assertRaisesRegex(ValueError, msg):
            RetrieveObservations(
                self.ICAO, self.TORM, self.current_date, latest_only=False
            )


if __name__ == "__main__":
    unittest.main()
