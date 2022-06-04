from data.datasources import NumberDataSource
from utils.analytics import Analytics
from utils.extractor import NumberExtractor

dataSources = NumberDataSource()

if __name__ == '__main__':
    dataSources.add([1, 27, 32,35,38,44,24])
    dataSources.add([2, 13, 35, 39, 43, 48, 9])
    dataSources.add([1,17,25,29,42,46,8])
    dataSources.add([5,7,8,17,47,49,34])
    dataSources.add([27,30,36,38,45,46,34])
    dataSources.add([4,7,29,35,40,46,17])
    dataSources.add([1,5,10,22,30,34,42])
    dataSources.add([12,14,19,39,41,48,33])
    dataSources.add([2,15,41,42,44,46,40])
    dataSources.add([3,8,11,15,18,40,41])
    dataSources.add([1,7,16,28,31,48,16])
    dataSources.add([9,23,30,32,34,40,25])
    dataSources.add([8,11,15,19,34,37,25])
    dataSources.add([12,23,28,34,39,46,44])
    dataSources.add([21,25,30,36,37,47,42])
    dataSources.add([8,11,12,20,26,30,28])
    dataSources.add([10,20,36,38,43,48,30])
    dataSources.add([9,11,12,22,29,42,3])
    dataSources.add([4,8,21,40,46,49,34])
    dataSources.add([8,18,21,35,37,38,10])
    dataSources.add([15,20,26,28,29,46,12])
    dataSources.add([6,28,32,33,40,45,1])
    an = Analytics(dataSources)
    an.hitTrace(8)
    an.sizeTrace(2)
    an.vaildation([2,8,22,35,40,43], [1, 27, 32,35,38,44,24])
    an.vaildation([7,17,25,27,39,46], [1, 27, 32,35,38,44,24])
    an.result()

    numberExtractor = NumberExtractor(dataSources)
    sixmark = numberExtractor.within(timeOfBack=5)
    print("Six Mark {}".format(sixmark))
