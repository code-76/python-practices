
from unittest import TestCase
from data.analytics_mode import NumberTraceMode
from data.local.local_number_datasource import LocalNumberDataSource
from utils.extractor import NumberExtractor

class TestNumberExtractor(TestCase):

    def setUp(self):
        self.list = [1,2,3,4,5]
        self.list2 = [6,7,8,1,10]
        self.list3 = [11,2,3,14,15]
        self.dataSource = LocalNumberDataSource()
        self.dataSource.add(self.list)
        self.dataSource.add(self.list2)
        self.dataSource.add(self.list3)
        self.extractor = NumberExtractor(self.dataSource)

    def tearDown(self):
        self.dataSource.clear()

    def test_sample(self):
        numbers = self.extractor.sample()
        self.assertEqual(len(numbers), 7)

    def test_get_with_level(self):
        odd = self.extractor.get_with_level(mode=NumberTraceMode.ODD, to=2)
        even = self.extractor.get_with_level(mode=NumberTraceMode.EVEN, to=2)
        self.assertEqual(odd, [1,3,5,7])
        self.assertEqual(even, [2,4,6,8,10])

    def test_distinct_count(self):
        num = self.extractor.distinct_count([1,2,3,1,5])
        self.assertEqual(num, [[1, 2], [2, 1], [3, 1], [5, 1]])