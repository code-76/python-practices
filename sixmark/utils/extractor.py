import random
import numpy as np
from data.analytics_mode import NumberSearchMode, NumberTraceMode
from data.extractor_mode import NumberExtractorMode
from data.remote.remote_number_datasource import RemoteNumberDataSource
from data.local.local_number_datasource import LocalNumberDataSource

class NumberExtractor:
    def __init__(self, dataSource):
        self.numberDataSource = dataSource
        if type(dataSource) is RemoteNumberDataSource:
            self.numberDataSource.__class__ = RemoteNumberDataSource
        elif type(dataSource) is LocalNumberDataSource:
            self.numberDataSource.__class__ = LocalNumberDataSource

    def sample(self):
        num = []
        while len(num) <= 6:
            num.append(random.randint(1, 49))
        return num

    def get_with_level(self, less=0, max=50, to=0, level=0, mode=NumberTraceMode.ODD):
        slots = self.numberDataSource.search(mode=NumberSearchMode.SLOTS, to=to)
        match mode:
            case NumberTraceMode.ODD:
                lists = [y for x in slots for y in x if y % 2 == 1 and y > less and y < max]
            case NumberTraceMode.EVEN:
                lists = [y for x in slots for y in x if y % 2 == 0 and y > less and y < max]
            case _:
                lists = [y for x in slots for y in x if y > less and y < max]
        
        count_lists = self.distinct_count(lists)
        soack = [x[0] for x in count_lists if x[1] >= level]

        # print(slots)
        # print("level {}".format(level))
        # print("count {}".format(count_lists))
        # print("soack {}".format(soack))
        return soack

    def distinct(self, lists1, lists2):
        return np.unique(lists1, lists2)

    def distinct_count(self, lists):
        unique, counts = np.unique(lists, return_counts=True)
        return np.column_stack((unique, counts)).tolist()

    def gen(self, withinList=[], divideList=[]):
        lucky_num = []
        while len(lucky_num) < 6:
            pick = True
            n = random.randint(1, 49)
            if n in lucky_num: 
                pick = False
            if len(withinList) > 0 and n not in withinList:
                pick = False
            if len(divideList) > 0 and n in divideList:
                pick = False
            if pick:
                lucky_num.append(n)

        print("Lucky number: {}".format(lucky_num))
        return lucky_num