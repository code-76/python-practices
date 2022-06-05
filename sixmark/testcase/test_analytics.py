from time import time
import unittest
from data.analytics_mode import NumberHitMode, NumberTraceMode
from data.local.local_number_datasource import LocalNumberDataSource
from utils.analytics import Analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.list = [1,2,3,4,5]
        self.list2 = [6,7,8,1,10]
        self.list3 = [11,2,3,14,15]
        self.list4 = [16,17,18,19,20]
        self.list5 = [21,22,23,24,25]
        self.dataSources = LocalNumberDataSource()
        self.dataSources.add(self.list)
        self.dataSources.add(self.list2)
        self.dataSources.add(self.list3)
        self.dataSources.add(self.list4)
        self.dataSources.add(self.list5)
        self.analytics = Analytics(self.dataSources)

    def tearDown(self):
        self.dataSources.clear()

    def test_sample_slots(self):
        result = "Number of slots: {}".format([self.list, self.list2, self.list3, self.list4, self.list5])
        self.assertEqual(result, self.analytics.log_msg)

    def test_validation(self):
        self.analytics.log_msg = ""
        result = "\nHit: {}, Number: {}".format(3, [2, 3, 4])
        self.analytics.hit(mode=NumberHitMode.VALIDATION, fromNum=[1,2,3,4,5], toNum=[2,3,4,6,9,7])
        self.assertEqual(result, self.analytics.log_msg)

    def test_trace_back_hit(self):
        self.analytics.log_msg = ""
        result = "\nTrace Back Hit {}".format([3, 0, 0, 0])
        self.analytics.hit(previous=2)
        self.assertEqual(result, self.analytics.log_msg)

    def test_trace_back_odd_and_even(self):
        self.analytics.log_msg = ""
        result = "\nTrace Back Hit {}".format("['[odd([1]), even([])]']")
        self.analytics.hit(mode=NumberHitMode.ODD_AND_EVEN, traceMode=NumberTraceMode.ODD_AND_EVEN, previous=1, time=1)
        self.assertEqual(result, self.analytics.log_msg)