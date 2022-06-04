import random
from data.datasources import NumberDataSource

class NumberExtractor:
    def __init__(self, dataSource: NumberDataSource):
        self.numberDataSource = dataSource

    def sample(self):
        num = []
        while len(num) <= 6:
            num.append(random.randint(1, 49))
        return num

    def within(self, **kwargs):
        to = kwargs.get("timeOfBack", None)
        rangeOfList = kwargs.get("ranageOflist", range(1, 49))
        outOfList = kwargs.get("outOfList", [])
        num = []

        if to is not None and to > 0:
            rangeOfList = self.numberDataSource.getNumberSlots(to=to, merge=True)

        while len(num) <= 6:
            n = random.choice(rangeOfList)
            if n not in num:
                if len(outOfList) == 0:
                    num.append(n)
                elif n not in outOfList:
                    num.append(n)
        return num
        


# from itertools import count
# from mimetypes import init
# import random


# class AnalyticsUtils:
#     def __init__(self):
#         self.myNumArr = []
#         self.targetNumArr = []

#     def set_myNum(self, *args):
#         self.myNumArr = self.__combine(args)

#     def set_targetNum(self, *args):
#         self.targetNumArr = self.__combine(args)

#     def get_myNum(self):
#         return self.myNumArr

#     def add_myNum(self, *args):
#         num = self.__combine(args)
#         self.myNumArr.append(num)

#     def get_targetNum(self):
#         return self.targetNumArr

#     def add_targetNum(self, *args):
#         num = self.__combine(args)
#         self.targetNumArr.append(num)

#     def __combine(self, *args):
#         result = []
#         for arg in args:
#             for i in arg:
#                 if type(i) is int:
#                     result.append(i)
#                 elif type(i) is list:
#                     result += i
#         return result

#     def mulitple_match(self, num):
#         count = 0
#         hit = []
#         for j in num:
#             if j in self.targetNumArr: 
#                 hit.append(j)
#                 count += 1
#         print("Match number: {}, total: {}".format(hit, count))

#     def vaildation(self):
#         for num in self.myNumArr:
#             if (type(num) is list):
#                self.mulitple_match(num)

#     def unique(self, list1):
#         x = np.array(list1)
#         return np.unique(x)

#     def show_all_result(self):
#         print(self.unique(self.targetNumArr))

#     def eliminate_match(self):
#         num = []
#         i = 0
#         while i < 6:
#             n = random.randint(1, 49)
#             if n not in self.targetNumArr and n not in num:
#                 num.append(n)
#                 i += 1
#         print("Luck number: {}".format(num))

#     def within_match(self):
#         num = []
#         numOfScope = self.unique(self.targetNumArr)
#         i = 0
#         while i < 6:
#             n = random.randint(1, 49)
#             if n in numOfScope and n not in num:
#                 num.append(n)
#                 i += 1
#         print("Lucky number: {}".format(num))
 