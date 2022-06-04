from data.datasources import NumberDataSourcesImpl

class LocalNumberDataSource(NumberDataSourcesImpl):
    def __init__(self):
        super().__init__()