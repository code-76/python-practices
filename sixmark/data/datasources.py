
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

    def search(self, mode=NumberSearchMode.LIST, skip=None, to=None, mergeEnable=False):
        match mode: 
            case NumberSearchMode.LIST: 
                return self.__search_list(skip, to)
            case NumberSearchMode.SLOTS:
                return self.__search_slots(skip, to, mergeEnable)
            case _: 
                return []       

    def __search_slots(self, skip=None, to=None, mergeEnable=False):
        if skip is None and to is None:
            if mergeEnable:
                return self.number_handler.to_list(self.number_slots)
            else:
                return self.number_slots
        else:
            if skip is None:
                skip = 0
            if to is None:
                to = len(self.number_slots)
             
            result = self.number_slots[skip:to]
            if mergeEnable:
                return self.number_handler.to_list(result)
            else:
                return result

    def __search_list(self, skip=None, to=None):
        if skip is None and to is None:
            return self.number_list
        else:
            if skip is None:
                skip = 0
            if to is None:
                to = len(self.number_list)
            return self.number_list[skip:to]  

    def clear(self):
        self.log_msg = ""
        self.number_slots = []
        self.number_list = []