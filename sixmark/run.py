from heapq import merge
from operator import mod
from time import time
from traceback import format_tb

from numpy import array, extract
from data.analytics_mode import NumberHitMode, NumberSearchMode, NumberTraceMode
from data.extractor_mode import NumberExtractorMode
from data.local.local_number_datasource import LocalNumberDataSource
from data.remote.remote_number_datasource import RemoteNumberDataSource
from utils.analytics import Analytics
from utils.extractor import NumberExtractor
from utils.hkjc import HKJCRequest


def testRemoteDataSourcces():
    remoteDataSource = RemoteNumberDataSource()
    remoteDataSource.load(sd="20220401", ed="20220605")
    lists = remoteDataSource.search(mode=NumberSearchMode.SLOTS, to=3, mergeEnable=True)
    print(lists)
    an2 = Analytics(remoteDataSource)
    an2.hit(previous=3, time=20)
    an2.result()

def testLocalDataSources():
    localDataSource = LocalNumberDataSource()
    localDataSource.add([1,27,2,35,38,44,24])
    localDataSource.add([2,13,35,39,43,48,9])
    localDataSource.add([1,17,25,29,42,46,8])
    localDataSource.add([5,7,8,17,47,49,34])
    localDataSource.add([27,30,36,38,45,46,34])
    localDataSource.add([4,7,29,35,40,46,17])
    localDataSource.add([1,5,10,22,30,34,42])
    localDataSource.add([12,14,19,39,41,48,33])
    localDataSource.add([2,15,41,42,44,46,40])
    localDataSource.add([3,8,11,15,18,40,41])
    localDataSource.add([1,7,16,28,31,48,16])
    localDataSource.add([9,23,30,32,34,40,25])
    localDataSource.add([8,11,15,19,34,37,25])
    localDataSource.add([12,23,28,34,39,46,44])
    localDataSource.add([21,25,30,36,37,47,42])
    localDataSource.add([8,11,12,20,26,30,28])
    localDataSource.add([10,20,36,38,43,48,30])
    localDataSource.add([9,11,12,22,29,42,3])
    localDataSource.add([4,8,21,40,46,49,34])
    localDataSource.add([8,18,21,35,37,38,10])
    localDataSource.add([15,20,26,28,29,46,12])
    localDataSource.add([6,28,32,33,40,45,1])
    an = Analytics(localDataSource)
    an.hit(mode=NumberHitMode.Default, previous=1)
    an.hit(mode=NumberHitMode.VALIDATION, fromNum=[2,8,22,35,40,43], toNum=[1,27,32,35,38,44,24])
    an.hit(mode=NumberHitMode.VALIDATION, fromNum=[7,17,25,27,39,46], toNum=[1,27,32,35,38,44,24])
    an.hit(mode=NumberHitMode.ODD_AND_EVEN, previous=8, time=5, traceMode=NumberTraceMode.ODD_AND_EVEN)
    an.result()

def testLocalExtractor():
    localDataSource = LocalNumberDataSource()
    localDataSource.add([1,27,2,35,38,12,24])
    localDataSource.add([2,35,35,12,43,48,9])
    extractor = NumberExtractor(localDataSource)
    extractor.get_with_level(to=2, max=20, level=2, mode=NumberTraceMode.EVEN)

def testRemoteExtractor():
    remoteDataSource = RemoteNumberDataSource()
    remoteDataSource.load(sd="20220301", ed="20220605")
    extractor = NumberExtractor(remoteDataSource)
    extractor.get_with_level(to=10, max=50, level=2, mode=NumberTraceMode.ODD_AND_EVEN)

def testDivideExtractor():
    remoteDataSource = RemoteNumberDataSource()
    remoteDataSource.load(sd="20220301", ed="20220605")
    divideLists = remoteDataSource.search(mode=NumberSearchMode.SLOTS, skip=2, to=3, mergeEnable=True)
    extractor = NumberExtractor(remoteDataSource)
    oddLists = extractor.get_with_level(to=10, level=2, mode=NumberTraceMode.ODD)
    evenLists = extractor.get_with_level(to=10, level=2, mode=NumberTraceMode.EVEN)
    withinLists = oddLists + evenLists
    # withinLists = extractor.get_with_level(to=10, level=2, mode=NumberTraceMode.ODD_AND_EVEN)

    withinLists = [x for x in withinLists if x not in divideLists]
    print("Divide {}".format(divideLists))
    print("Within {}".format(withinLists))

    an = Analytics(remoteDataSource)
    lucky_num = extractor.gen(withinList=withinLists, divideList=divideLists)
    an.hit(mode=NumberHitMode.VALIDATION, fromNum=lucky_num, toNum=[2,13,35,39,43,48,9])
    an.result()
    
def testRange(odd, even):
    return "{}:{}".format(odd, even)

def test():
    a = [x for x in range(1,10) if x % 2 == 0]
    b = [testRange(x, y) for x in range(1,4) for y in range(1,8) if x % 2 > 0]
    print("{}, {}".format(a, b))

if __name__ == '__main__':
    testDivideExtractor()
    # testRemoteExtractor()
    # testLocalExtractor()
    # test()
    # testLocalDataSources()
    # testRemoteDataSourcces()
