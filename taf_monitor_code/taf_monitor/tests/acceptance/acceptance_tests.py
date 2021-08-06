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

import glob
import json
import sys
import textwrap
from collections import OrderedDict
from datetime import datetime as dt

from taf_monitor.checking import CheckTafThread


class ConstructTests(object):
    def __init__(self, verbose=True):
        self.verbose = verbose

    @staticmethod
    def format_description(description):
        width = 89
        border = "=" * width
        fmt = "{}\n\n{}\n\n{}"
        description = textwrap.fill(description, width)
        print((fmt.format(border, description, border)))

    def format_test_result(self, test_passed, test_name, output, test_time, test_pair):

        width = 75
        # Return text to default terminal colour at the end.
        cend = "\033[0m"

        verbose_message = ""
        if test_passed:
            status = "succeeded"
            cstatus = "\033[32m"

        else:
            status = "failed"
            cstatus = "\033[31m"

        vfmt = (
            "\n{}{}{} - details:\n{}\n{}\nTAF:\t{}\nMETAR:\t{}\n"
            "Checked at:\t{}\n\nReturns:\n{}\n{}"
        )
        if self.verbose:
            verbose_message = vfmt.format(
                cstatus,
                status,
                cend,
                test_name,
                "-" * 50,
                " ".join(test_pair[2]),
                " ".join(test_pair[1]),
                test_time,
                output.strip(),
                "-" * 50,
            )
            print(verbose_message)
        else:
            if len(test_name) > width - 3:
                test_name = test_name[: width - 3] + "..."
            print(
                (
                    "{:{width}.{width}}  -- {}{}{}".format(
                        test_name, cstatus, status, cend, width=width
                    )
                )
            )

    @staticmethod
    def extract_tests(test_files):

        descriptions = []
        taf_tests = []
        for test_file in test_files:
            with open(test_file, "r") as ff:
                all_reports = json.load(ff, object_pairs_hook=OrderedDict)

            test_pairs = []
            test_names = []
            test_times = []
            test_results = []

            taf_key = list(all_reports.keys())[0]
            descriptions.append(all_reports["description"])
            taf = taf_key.split()
            for test_name, report in all_reports[taf_key].items():
                metar = report.get("metar", "NoRecord").split()
                speci = report.get("speci", "NoRecord").split()
                test_time = report["test time"]
                test_result = report["expected"]

                test_time = dt.strptime(test_time, "%Y%m%dT%H%MZ")

                test_names.append(test_name)
                test_pairs.append([taf[0], metar, taf, speci])
                test_times.append(test_time)
                test_results.append(test_result)

            taf_tests.append(
                list(zip(test_names, test_pairs, test_times, test_results))
            )

        return list(zip(descriptions, taf_tests))

    def operation(self):

        overall_result = 0

        TEST_PATH = (
            "/home/h02/bayliffe/scripts/python/forecasting/"
            "taf_monitor/taf_monitor/tests/acceptance/"
        )

        test_files = glob.glob(TEST_PATH + "*.tst")
        tests = self.extract_tests(test_files)

        # Not actually used.
        bench = "All Civilian Airfields"

        for description, taf_test in tests:
            self.format_description(description)
            for test_name, test_pair, test_time, test_result in taf_test:

                output = CheckTafThread(
                    bench, test_obs_list=[test_pair], test_times=[test_time]
                ).run()

                test_passed = output.strip() == test_result.strip()
                self.format_test_result(
                    test_passed, test_name, output, test_time, test_pair
                )
                if not test_passed:
                    overall_result = 1

        if overall_result != 0:
            sys.exit(1)


if __name__ == "__main__":
    verbose = False
    try:
        if sys.argv[1] == "-v":
            verbose = True
    except IndexError:
        pass

    ConstructTests(verbose=verbose).operation()
