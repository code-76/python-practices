from ast import Pass
from cmath import log
from data.datasources import NumberDataSource

class Analytics:
    def __init__(self, dataSource: NumberDataSource):
        self.numberSlots = []
        self.numberDataSource = dataSource
        self.log = "Number slots {}".format(self.numberDataSource.getNumberSlots())

    def sizeTrace(self, timeOfBack=0):
        recordSize = []
        skip = 0
        to = timeOfBack
        isRunning = True

        while isRunning:
            listOfTrace = self.numberDataSource.getNumberSlots(skip=skip, to=to)

            if len(listOfTrace) == 0:
                isRunning = False
                break

            if self.isBigSize(listOfTrace):
                recordSize.append("Big")
            else:
                recordSize.append("Small")

            print("list of range {}".format(listOfTrace))

            skip += to
            to += timeOfBack

        self.log += "\nTrace Size {}".format(recordSize)

    def isBigSize(self, listOfTrace):
        small = 0
        big = 0

        for num in listOfTrace:
            if type(num) is int:
                if num <= 30:
                    small += 1
                else:
                    big += 1
            if type(num) is list:
                for i in num:
                    if i <= 30:
                        small += 1
                    else:
                        big += 1
        return big > small


    def hitTrace(self, timeOfBack=0):
        recordHits = []
        start = 0
        skip = 1
        to = timeOfBack + 1
        isRunning = True
        numberSlots = self.numberDataSource.getNumberSlots()

        while isRunning:
            firstOfSlot = numberSlots[start]
            listOfTrace = self.numberDataSource.getNumberSlots(skip=skip, to=to, merge=True)

            if len(listOfTrace) <= 0:
                isRunning = False
                break

            count = 0   
            for i in firstOfSlot:
                if i in listOfTrace:
                    count += 1
            
            to += 1
            skip += 1
            start += 1
            recordHits.append(count)

        self.log += "\nTrace Hit {}".format(recordHits)

    def vaildation(self, list, list2):
        recordHits = 0
        for i in list:
            if i in list2:
                recordHits += 1
        self.log += "\n Vaildation hit {}".format(recordHits)

    def result(self):
        print(self.log)

