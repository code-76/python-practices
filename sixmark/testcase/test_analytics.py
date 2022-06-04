import unittest

from data.local.local_number_datasource import LocalNumberDataSource
from utils.analytics import Analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.list = [1,2,3,4,5]
        self.list2 = [6,7,8,9,10]
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
        self.analytics.validation([1,2,3,4,5], [2,3,4,6,9,7])
        self.assertEqual(result, self.analytics.log_msg)

    def test_hit(self):
        self.analytics.log_msg = ""
        result = "\nTrace Hit {}".format([2, 0, 0, 0])
        self.analytics.hit(traceOfTime=2)
        self.assertEqual(result, self.analytics.log_msg)