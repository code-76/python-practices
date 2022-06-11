from data.analytics_mode import NumberAnalytcsMode, NumberSearchMode
from data.extractor_mode import NumberExtractorMode
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

def loadMockDataSource(dataSource):
    dataSource.add([1,27,2,35,38,44,24])
    dataSource.add([2,13,35,2,43,48,9])
    dataSource.add([1,17,25,2,42,46,8])
    dataSource.add([5,7,8,17,47,49,34])

def testAvg(dataSource):
    extractor = NumberExtractor(dataSource)
    odd_avg = extractor.get_average_by(size=20)
    even_avg = extractor.get_average_by(size=20, mode=NumberExtractorMode.EVEN)
    single_avg = extractor.get_average_by(size=20, to=10)
    double_avg = extractor.get_average_by(size=20, by=10)
    print("Avg odd({}), even({}), single({}), double({})".format(odd_avg, even_avg, single_avg, double_avg))

def luckyNumber(dataSource):
    extractor = NumberExtractor(dataSource)
    an = Analytics(dataSource)
    an.log_enable(True)
    collectByType = an.recollect()
    collectByNumbers = an.recollect(mode=NumberAnalytcsMode.RANGE, scope=20, level=2)
    result = extractor.gen(
        followList=collectByNumbers["odd"] + collectByNumbers["even"],
        singleTime=collectByType["single"],
        oddTime=collectByType["odd"]
    )
    print("Lucky number: {}".format(result))

def validation(dataSource):
    myNum = [45, 17, 23, 5, 33, 39]
    latestSlot = dataSource.search(mode=NumberSearchMode.SLOTS, size=1, mergeEnable=True)
    an = Analytics(dataSource)
    print("Today: {} Result: {}".format(latestSlot, an.validation(latestSlot, myNum)))

if __name__ == '__main__':
    # loadMockDataSource(localDataSource)
    # localDataSource.log()
    remoteDataSource.load(sd="20220401", ed="20220610")
    # remoteDataSource.log()
    # testAvg(remoteDataSource)
    luckyNumber(remoteDataSource)
    # validation(remoteDataSource)
