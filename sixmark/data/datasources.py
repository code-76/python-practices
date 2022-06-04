from utils.number import NumberHandler

class NumberDataSource:
    def __init__(self):
        self.numberSlots = []
        self.numberList = []
        self.numberHandler = NumberHandler()
        
    def add(self, *args):
        self.numberList = self.numberHandler.merge(self.numberList, args)
        self.numberSlots.append(self.numberHandler.add(args))

    def getNumberList(self):
        return self.numberList
        
    def getNumberSlots(self, skip=None, to=None, merge=False):
        if skip is not None and skip > 0 and to is not None and to > 0:
            slots = self.numberSlots[skip:to]
            if len(slots) < to - skip:
                return []
            if merge:
                return self.numberHandler.toList(slots)
            else:
                return slots
        elif to is not None and to > 0:
            slots = self.numberSlots[:to]
            if merge:
                return self.numberHandler.toList(slots)
            else:
                return slots
        else:
            return self.numberSlots
        
