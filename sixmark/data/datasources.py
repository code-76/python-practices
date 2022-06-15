
from data.datasources_interface import NumberDataSourcesInterface
from data.analytics_mode import NumberSearchMode
from utils.number import NumberHandler

class NumberDataSourcesImpl(NumberDataSourcesInterface):
    def __init__(self):
        NumberDataSourcesInterface.__init__(self)
        self.number_slots = []
        self.number_list = []
        self.number_handler = NumberHandler()
    
    def add(self, *slots):
        if type(slots) is int:
            self.number_list.append(slots)
        else:
            self.number_list = self.number_handler.merge(self.number_list, slots)
            self.number_slots.append(self.number_handler.add(slots))

    def get_list(self) -> list:
        return self.number_list

    def get_slots(self) -> tuple:
        return self.number_slots

    def search(self, mode=NumberSearchMode.LIST, skip=None, size=None, mergeEnable=False):
        match mode: 
            case NumberSearchMode.LIST: 
                return self._search_list(skip, size)
            case NumberSearchMode.SLOTS:
                return self._search_slots(skip, size, mergeEnable)
            case _: 
                return []       

    def _search_slots(self, skip=None, size=None, mergeEnable=False):
        if skip is None and size is None:
            return self.number_handler.to_list(self.number_slots) if mergeEnable else self.number_slots
        else:
            skip = 0 if skip is None else skip
            size = len(self.number_slots) if size is None else size
            result = self.number_slots[skip:size+skip]
            return result if mergeEnable == False else self.number_handler.to_list(result)

    def _search_list(self, skip=None, size=None):
        if skip is None and size is None:
            return self.number_list
        else:
            skip = 0 if skip is None else skip
            size = len(self.number_list) if size is None else size
            return self.number_list[skip:size+skip]

    def clear(self):
        self.log_msg = ""
        self.number_slots = []
        self.number_list = []

    def log(self):
        print("\n{}".format(self.number_list))