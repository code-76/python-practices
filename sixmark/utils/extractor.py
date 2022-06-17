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

    def gen(self, followList=[], divideList=[], singularPoint=0, oddPoint=0, evenPoint=0, tenPoint=0, twoPoint=0, threePoint=0, fourPoint=0, excludePast=0):
        luckyNum = []
        while len(luckyNum) < 6:
            n = random.randint(1, 49) if len(followList) == 0 else random.choice(followList)
            self._log("debug", "gen: {}".format(n))
            if n not in luckyNum:
                if self._is_divide_range(n, divideList) == False:
                    continue

                luckyNum.append(n)

                if len(luckyNum) == 6:
                    if excludePast > 0 and self._as_same(luckyNum, excludePast):
                        # print("Reset by same number")
                        luckyNum = []
                    elif singularPoint > 0 and self._range_count(luckyNum, by=1, to=9) < singularPoint:
                        # print("Reset by single count")
                        luckyNum = []
                    elif tenPoint > 0 and self._range_count(luckyNum, by=10, to=19) < tenPoint:
                        # print("Reset by double count")
                        luckyNum = []
                    elif twoPoint > 0 and self._range_count(luckyNum, by=20, to=29) < twoPoint:
                        # print("Reset by double count")
                        luckyNum = []
                    elif threePoint > 0 and self._range_count(luckyNum, by=30, to=39) < threePoint:
                        # print("Reset by double count")
                        luckyNum = []
                    elif fourPoint > 0 and self._range_count(luckyNum, by=40, to=49) < fourPoint:
                        # print("Reset by double count")
                        luckyNum = []
                    elif oddPoint > 0 and self._odd_count(luckyNum) < oddPoint:
                        # print("Reset by odd count")
                        luckyNum = []
                    elif evenPoint > 0 and self._even_count(luckyNum) < evenPoint:
                        # print("Reset by even count")
                        luckyNum = []
                    
        self._log("info", "gen: {}".format(luckyNum))
        return luckyNum

    def log(self):
        self.debugLogger.log()

    def _log(self, level, message):
        self.debugLogger.info(level, message)