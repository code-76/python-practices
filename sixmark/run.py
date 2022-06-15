from audioop import avg
from data.analytics_mode import NumberAnalyticsMode, NumberSearchMode
from data.debug_mode import DebugLogLevel
from data.local.local_number_datasource import LocalNumberDataSource
from data.remote.remote_number_datasource import RemoteNumberDataSource
from utils.analytics import Analytics
from utils.extractor import NumberExtractor

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
    numTypes = an.recollect(scope=5, level=2)
    latestNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=1, mergeEnable=True)
    slotsPastNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=2, mergeEnable=True)
    trace = an.recollect(mode=NumberAnalyticsMode.TRACE, time=20, scope=1)
    range10WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=1, to=10)
    range20WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=10, to=19)
    range30WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=20, to=29)
    range40WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=30, to=39)
    range49WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=40, to=49)
    hitWithLevel = an.recollect(mode=NumberAnalyticsMode.HIT, scope=20, level=3)
    print("Latest numbers: {}".format(latestNumbers))
    print("Number Types: {}".format(numTypes))
    print("Number Hits: {}".format(hitWithLevel))
    print("Range Numbers 1-10: {}".format(range10WithLevel))
    print("Range Numbers 10-29: {}".format(range20WithLevel))
    print("Range Numbers 20-29: {}".format(range30WithLevel))
    print("Range Numbers 30-39: {}".format(range40WithLevel))
    print("Range Numbers 40-49: {}".format(range49WithLevel))
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
    localDataSource = LocalNumberDataSource()
    remoteDataSource = RemoteNumberDataSource()
    remoteDataSource.load(sd="20220401", ed="20220614")
    mockLocalNumberDataSource = LocalNumberDataSource()
    # load_mock_datasource(localDataSource)
    # localDataSource.log()
    # remoteDataSource.log()

    first_one_conbination(remoteDataSource)
    # validation(remoteDataSource, shot=[11, 17, 24, 26, 37, 41])
