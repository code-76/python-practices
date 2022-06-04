from data.local.local_number_datasource import LocalNumberDataSource
from data.remote.remote_number_datasource import RemoteNumberDataSource
from utils.analytics import Analytics
from utils.hkjc import HKJCRequest

localDataSource = LocalNumberDataSource()
remoteDataSource = RemoteNumberDataSource()

if __name__ == '__main__':
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
    an.hit(1)
    an.validation([2,8,22,35,40,43], [1,27,32,35,38,44,24])
    an.validation([7,17,25,27,39,46], [1,27,32,35,38,44,24])
    an.result()

    remoteDataSource.load(sd="20220501", ed="20220605")
    an2 = Analytics(remoteDataSource)
    an2.hit(2)
    an2.result()
