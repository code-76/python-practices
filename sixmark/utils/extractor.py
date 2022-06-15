import random
from data.analytics_mode import NumberSearchMode
from data.remote.remote_number_datasource import RemoteNumberDataSource
from data.local.local_number_datasource import LocalNumberDataSource
from utils.debug import DebugLogger

class NumberExtractor:
    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.debugLogger = DebugLogger()
        self.dataSource.__class__ = LocalNumberDataSource if type(dataSource) is LocalNumberDataSource else RemoteNumberDataSource

    def log_level(self, level):
        self.debugLogger.log_level(level) 

    def sample(self):
        num = []
        while len(num) <= 6:
            num.append(random.randint(1, 49))
        return num

    def _range_count(self, luckyNum, by, to):
        count = 0
        for num in luckyNum:
            if num in range(by, to):
                count += 1
        return count

    def _is_within_range(self, num, withinList):
        return num in withinList or len(withinList) == 0

    def _is_divide_range(self, num, divideList):
        return num not in divideList or len(divideList) == 0

    def _odd_count(self, luckyNum):
        count = 0
        for num in luckyNum:
            if num % 2 == 1:
                count += 1
        return count

    def _even_count(self, luckyNum):
        count = 0
        for num in luckyNum:
            if num % 2 == 0:
                count += 1
        return count

    def _as_same(self, luckyNum, time=0):
        slots = self.dataSource.search(mode=NumberSearchMode.SLOTS, size=50)
        for slot in slots:
            count = 0   
            for num in slot:
                if num in luckyNum:
                    count += 1
                if time == count:
                    return True

        return False

    def gen(self, followList=[], divideList=[], singleTime=0, doubleTime=0, oddTime=0, evenTime=0, excludeTime=0):
        lucky_num = []
        while len(lucky_num) < 6:
            n = random.randint(1, 49) if len(followList) == 0 else random.choice(followList)
            self._log("debug", "gen: {}".format(n))
            if n not in lucky_num:
                if self._is_divide_range(n, divideList) == False:
                    continue

                lucky_num.append(n)

                if len(lucky_num) == 6:
                    if excludeTime > 0 and self._as_same(lucky_num, excludeTime):
                        # print("Reset by same number")
                        lucky_num = []
                    elif singleTime > 0 and self._range_count(lucky_num, by=1, to=9) < singleTime:
                        # print("Reset by single count")
                        lucky_num = []
                    elif doubleTime > 0 and self._range_count(lucky_num, by=10, to=49) < doubleTime:
                        # print("Reset by double count")
                        lucky_num = []
                    elif oddTime > 0 and self._odd_count(lucky_num) < oddTime:
                        # print("Reset by odd count")
                        lucky_num = []
                    elif evenTime > 0 and self._even_count(lucky_num) < evenTime:
                        # print("Reset by even count")
                        lucky_num = []
                    
        self._log("info", "gen: {}".format(lucky_num))
        return lucky_num

    def log(self):
        self.debugLogger.log()

    def _log(self, level, message):
        self.debugLogger.info(level, message)