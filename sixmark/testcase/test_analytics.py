import unittest
from data.analytics_mode import NumberAnalytcsMode
from data.local.local_number_datasource import LocalNumberDataSource
from utils.analytics import Analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.list = [1,2,3,4,5]
        self.list2 = [6,2,8,1,10]
        self.list3 = [11,2,3,14,15]
        self.list4 = [16,17,18,19,20]
        self.list5 = [21,2,16,24,25]
        self.dataSource = LocalNumberDataSource()
        self.dataSource.add(self.list)
        self.dataSource.add(self.list2)
        self.dataSource.add(self.list3)
        self.dataSource.add(self.list4)
        self.dataSource.add(self.list5)
        self.analytics = Analytics(self.dataSource)

    def tearDown(self):
        self.dataSource.clear()

    def test_validation(self):
        result = self.analytics.validation(fromNum=[1,2,3,4,5], toNum=[2,3,4,6,9,7])
        self.assertEqual(result, {'hits': 3, 'numbers': [2, 3, 4]})

    def test_collect_number(self):
        result = self.analytics.recollect(mode=NumberAnalytcsMode.RANGE, scope=1)
        resultWithLevel = self.analytics.recollect(mode=NumberAnalytcsMode.RANGE, scope=2, level=2)
        self.assertEqual(result, {'odd': [1, 3, 5], 'even': [2, 4]})
        self.assertEqual(resultWithLevel, {'odd': [1], 'even': [2]})

    def test_trace(self):
        result = self.analytics.recollect(mode=NumberAnalytcsMode.TRACE, time=2, scope=1)
        self.assertEqual(result, {'hit_numbers': [[1, 2], []]})

    def test_recollect(self):
        resultAvg = self.analytics.recollect()
        resultMax = self.analytics.recollect(avg=False)
        self.assertEqual(resultAvg, {'odd': 2, 'even': 3, 'single': 2, 'double': 3})
        self.assertEqual(resultMax, {'odd': 3, 'even': 4, 'single': 5, 'double': 5})