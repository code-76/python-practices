from data.search_mode import NumberSearchMode

class NumberDataSourcesInterface:

    def __init__(self):
        self.log_msg = ""

    def add(self, *slots):
        pass

    def clear(self):
        pass

    def get_List(self) -> list:
        pass

    def get_slots(self) -> tuple:
        pass

    def search(self, mode=NumberSearchMode.LIST, skip=None, to=None, mergeEnable=False):
        pass

    def add_log(self, **kwargs):
        self.log_msg += "\n{}".format(kwargs)

    def log(self):
        print(self.log_msg)