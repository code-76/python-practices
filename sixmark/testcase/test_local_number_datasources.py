import unittest
from data.local.local_number_datasource import LocalNumberDataSource
from data.search_mode import NumberSearchMode

class TestLocalNumberDataSources(unittest.TestCase):

    def setUp(self):
        self.dataSources = LocalNumberDataSource()

    def tearDown(self):
        self.dataSources.clear()

    def test_add(self):
        list = [1,2,3,4,5]
        list2 = [7,8,9,10,11]
        self.dataSources.add(list, list2)
        self.assertEqual(self.dataSources.get_list(), list + list2)

    def test_search_list(self):
        list = [1,2,3,4,5]
        list2 = [7,8,9,10,11]
        self.dataSources.add(list)
        self.dataSources.add(list2)
        self.assertEqual(self.dataSources.search(skip=0, to=5), list)
        self.assertEqual(self.dataSources.search(skip=0), list + list2)
        self.assertEqual(self.dataSources.search(skip=5), list2)
        self.assertEqual(self.dataSources.search(to=5), list)
        self.assertEqual(self.dataSources.search(skip=5, to=10), list2)

    def test_search_slots(self):
        list = [1,2,3,4,5]
        list2 = [7,8,9,10,11]
        self.dataSources.add(list)
        self.dataSources.add(list2)
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=1, to=2), [list2])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=0, to=2), [list, list2])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=0), [list, list2])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, to=0), [])
        self.assertEqual(self.dataSources.search(mode=NumberSearchMode.SLOTS, to=1), [list])

    def test_clear(self):
        self.dataSources.clear()
        self.assertEqual(self.dataSources.get_list(), [])
        self.assertEqual(self.dataSources.get_slots(), [])
        self.assertEqual(self.dataSources.log_msg, "")
