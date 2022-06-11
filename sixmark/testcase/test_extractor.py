from unittest import TestCase
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