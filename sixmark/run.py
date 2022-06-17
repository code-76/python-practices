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

def conbination(dataSource):
    an = Analytics(dataSource)
    an.log_level(DebugLogLevel.NONE)
    numTypes = an.recollect(scope=20, level=3)
    latestNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=1, mergeEnable=True)
    slotsPastNumbers = dataSource.search(mode=NumberSearchMode.SLOTS, size=6, mergeEnable=True)
    traceOneByOne = an.recollect(mode=NumberAnalyticsMode.TRACE, time=20, scope=3)
    range10WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=1, to=10)
    range20WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=10, to=19)
    range30WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=2, by=20, to=29)
    range40WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=30, to=39)
    range49WithLevel = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=40, to=49)
    level1 = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=1, by=1, to=49)
    level2 = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=2, by=1, to=49)
    level3 = an.recollect(mode=NumberAnalyticsMode.RANGE, scope=20, level=3, by=1, to=49)
    hitWithLevel = an.recollect(mode=NumberAnalyticsMode.HIT, scope=20, level=3)
    dividePastNumbers = [x for x in level2["in_range"] if x not in slotsPastNumbers]
    divideLatestLevel3 = [x for x in level3["in_range"] if x not in latestNumbers]
    traceByList = an.recollect(mode=NumberAnalyticsMode.TRACE, time=20, scope=1, followList=slotsPastNumbers)
    divideMyList = [x for x in level1["in_range"] if x not in [1,2,3,4,5]]

    print("Latest numbers: {}".format(latestNumbers))
    print("Past Numbers: {}".format(slotsPastNumbers))
    print("Number Types: {}".format(numTypes))
    print("Number Hits: {}".format(hitWithLevel))
    print("Level 1 Numbers: {}".format(level1))
    print("Level 2 Numbers: {}".format(level2))
    print("Level 3 Numbers: {}".format(level3))
    print("Divide Latest with Level 3 Numbers: {}".format(divideLatestLevel3))
    print("Divide Past Number: {}".format(dividePastNumbers))
    print("Range Numbers 1-10: {}".format(range10WithLevel))
    print("Range Numbers 10-29: {}".format(range20WithLevel))
    print("Range Numbers 20-29: {}".format(range30WithLevel))
    print("Range Numbers 30-39: {}".format(range40WithLevel))
    print("Range Numbers 40-49: {}".format(range49WithLevel))
    an.log()
    # for index, hit in enumerate(traceOneByOne["numbers"]):
    #     print("{} : {}".format(index, hit))
    # print("==========================================")
    for index, hit in enumerate(traceByList["numbers"]):
        print("{} : {}".format(index, hit))        
    extractor = NumberExtractor(dataSource)
    result = extractor.gen(
        followList=level1["in_range"],
        singularPoint=1,
        tenPoint=1,
        twoPoint=2,
        threePoint=1,
        fourPoint=1
    )
    print("Lucky number: {}".format(result))

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
    remoteDataSource.load(sd="20220401", ed="20220617")
    mockLocalNumberDataSource = LocalNumberDataSource()
    # load_mock_datasource(localDataSource)
    # localDataSource.log()
    # remoteDataSource.log()

    conbination(remoteDataSource)
    # validation(remoteDataSource, shot=[11, 17, 24, 26, 37, 41])
