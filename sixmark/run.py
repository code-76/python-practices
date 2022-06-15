from audioop import avg
from data.analytics_mode import NumberAnalyticsMode, NumberSearchMode
from data.debug_mode import DebugLogLevel
from data.local.local_number_datasource import LocalNumberDataSource
from data.remote.remote_number_datasource import RemoteNumberDataSource
from utils.analytics import Analytics
from utils.extractor import NumberExtractor

localDataSource = LocalNumberDataSource()
remoteDataSource = RemoteNumberDataSource()
mockLocalNumberDataSource = LocalNumberDataSource()

def analytics(dataSource):
    an = Analytics(dataSource)
    an.result()

def load_mock_datasource(dataSource):
    dataSource.add([1,27,2,35,38,44,24])
    dataSource.add([2,13,35,2,43,48,9])
    dataSource.add([1,17,25,2,42,46,8])
    dataSource.add([5,7,8,17,47,49,34])

def lucky_number(dataSource):
    extractor = NumberExtractor(dataSource)
    an = Analytics(dataSource)
    # an.log_enable(True)
    numCountType = an.recollect()
    an.recollect(mode=NumberAnalyticsMode.TRACE, time=5, scope=5)
    latestList = dataSource.search(mode=NumberSearchMode.SLOTS, size=1, mergeEnable=True)
    pastList = dataSource.search(mode=NumberSearchMode.SLOTS, size=3, mergeEnable=True)
    numHit = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=2,  by=1, to=10)
    odd = numHit["odd"]
    even = numHit["even"]
    diviedList = latestList + [2,19,30,39,42,47] + [27, 32, 7, 40, 15, 48] + [16, 21, 35, 5, 44, 29]
    followList = odd + even
    followList = [x for x in followList if x not in diviedList]
    followList.sort()

    result = extractor.gen(
        followList=followList,
        singleTime=1,
        doubleTime=numCountType["double"]
    )
    print("Lucky number: {}".format(result))

def first_one_conbination(dataSource):
    an = Analytics(dataSource)
    an.log_level(DebugLogLevel.NONE)
    numTypes = an.recollect()
    latestNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=1, mergeEnable=True)
    slotsPastNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=2, mergeEnable=True)
    trace = an.recollect(mode=NumberAnalyticsMode.TRACE, time=20, scope=1)
    hitWithLevel3 = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3)
    # # odd = hitWithLevel3["odd"]
    # # even = hitWithLevel3["even"]
    # an.log()
    # odd, even = an.odd_even_count(slot=latestNumbers)
    # single = an.in_range_count(slot=latestNumbers, by=1, to=10)
    print("Latest numbers: {}".format(latestNumbers))
    # print("Slots: {}, odd: {}, even: {}, single: {}".format(slotsPastNumbers, odd, even, single))
    print("Number Types: {}".format(numTypes))
    an.log()
    for index, hit in enumerate(trace["numbers"]):
        print("{} : {}".format(index, hit))

def validation(dataSource, skip=0, shot=[]):
    latestSlot = dataSource.search(mode=NumberSearchMode.SLOTS, skip=skip, size=1, mergeEnable=True)
    an = Analytics(dataSource)
    print("Today: {} Result: {}".format(latestSlot, an.validation(latestSlot, shot)))

def validation_all(dataSource, skip=0, time=0, shot=[]):
    an = Analytics(dataSource)
    while time > 0:
        latestSlot = dataSource.search(mode=NumberSearchMode.SLOTS, skip=skip, size=1, mergeEnable=True)
        print("Loaded: {} Result: {}".format(latestSlot, an.validation(latestSlot, shot)))
        skip += 1
        time -= 1

if __name__ == '__main__':
    # load_mock_datasource(localDataSource)
    # localDataSource.log()
    remoteDataSource.load(sd="20220401", ed="20220614")
    first_one_conbination(remoteDataSource)
    # remoteDataSource.log()
    # validation(remoteDataSource, shot=[11, 17, 24, 26, 37, 41])
