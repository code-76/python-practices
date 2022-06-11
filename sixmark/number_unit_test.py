

import sys
import unittest
from testcase.test_extractor import TestNumberExtractor
from testcase.test_local_number_datasources import TestLocalNumberDataSources
from testcase.test_analytics import TestAnalytics
from testcase.test_remote_number_datasources import TestRemoteNumberDataSource

# https://docs.python.org/3/library/unittest.html

def module(className):
    return getattr(sys.modules[__name__], className)

def suite(className):
    return unittest.TestLoader().loadTestsFromTestCase(className)

def suites(dict):
    suite = unittest.TestSuite()
    for className, caseName in dict.items():
        suite.addTest(module(className)(caseName))
    return suite

if __name__ == '__main__':
    # python -m unittest -v test_module
    # unittest.main()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite(TestAnalytics))
    runner.run(suite(TestNumberExtractor))
    runner.run(suite(TestLocalNumberDataSources))
    runner.run(suite(TestRemoteNumberDataSource))
    # runner.run(suites({"TestAnalytics" : "test_collect_number"}))
    # runner.run(suites({"TestAnalytics" : "test_trace"}))
    # runner.run(suites({"TestAnalytics": "test_recollect"}))
    # runner.run(suites({"TestLocalNumberDataSources": "test_search_slots"}))
    # runner.run(suites({"TestLocalNumberDataSources": "test_search_list"}))
