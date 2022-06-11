import unittest
from data.local.local_number_datasource import LocalNumberDataSource
from data.analytics_mode import NumberSearchMode

class TestLocalNumberDataSources(unittest.TestCase):

    def setUp(self):
        self.dataSources = LocalNumberDataSource()
        self.list = [1,2,3,4,5,6]
        self.list2 = [7,8,9,10,11]
        self.dataSources.add(self.list)
        self.dataSources.add(self.list2)

    def tearDown(self):
        self.dataSources.clear()

    def test_add(self):
        self.assertEqual(self.dataSources.get_list(), self.list + self.list2)

    def test_search_list(self):
        self.assertEqual(self.dataSources.search(size=6), self.list)
        self.assertEqual(self.dataSources.search(skip=6), self.list2)
        self.assertEqual(self.dataSources.search(skip=6, size=6), self.list2)

    def test_search_slots(self):
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, size=0), [])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, size=1), [self.list])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=1), [self.list2])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=1, size=1), [self.list2])

    def test_clear(self):
        self.dataSources.clear()
        self.assertEqual(self.dataSources.get_list(), [])
        self.assertEqual(self.dataSources.get_slots(), [])
        self.assertEqual(self.dataSources.log_msg, "")
