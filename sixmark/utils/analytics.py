from data.local.local_number_datasource import LocalNumberDataSource
from data.analytics_mode import NumberHitMode, NumberSearchMode, NumberTraceMode

class Analytics:
    def __init__(self, dataSources: LocalNumberDataSource):
        self.dataSources = dataSources
        self.log_msg = "Number of slots: {}".format(self.dataSources.get_slots())

    def hit(self, mode=NumberHitMode.Default, **kwargs):
        match mode:
            case NumberHitMode.Default:
                self.trace_back(previous=kwargs.get("previous", 0),time=kwargs.get("time", 0))
            case NumberHitMode.VALIDATION:
                self.validation(fromNum=kwargs.get("fromNum", []), toNum=kwargs.get("toNum", []))
            case NumberHitMode.ODD_AND_EVEN:
                self.trace_back(previous=kwargs.get("previous", 0), time=kwargs.get("time", 0), traceMode=kwargs.get("traceMode", NumberTraceMode.HIT))
        
    def trace_back(self, previous=0, time=0, traceMode=NumberTraceMode.HIT):
        record_hits = []
        count = 0
        start = 0
        skip = 1
        to = previous + skip
        is_running = True
        number_slots = self.dataSources.get_slots()
        while is_running:
            first_slot = number_slots[start]
            trace_list = self.dataSources.search(mode=NumberSearchMode.SLOTS, skip=skip, to=to, mergeEnable=True)

            if len(trace_list) <= 0 or (time > 0 and count >= time):
                is_running = False
                break

            match traceMode:
                case NumberTraceMode.HIT:
                    count = self.trace_back_hits(fromNum=first_slot, toNum=trace_list)
                    record_hits.append(count)
                case NumberTraceMode.ODD_AND_EVEN:
                    record = self.trace_back_odd_even(fromNum=first_slot, toNum=trace_list)
                    record_hits.append(record)
            
            to += 1
            skip += 1
            start += 1
            count += 1

        self.log_msg += "\nTrace Back Hit {}".format(record_hits)
        pass

    def trace_back_hits(self, fromNum, toNum):
        count = 0
        for i in fromNum:
            if i in toNum:
                count += 1
        return count

    def trace_back_odd_even(self, fromNum, toNum):
        odd = []
        even = []
        for i in fromNum:
            if i in toNum:
                if i % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)

        return "[odd({}), even({})]".format(odd, even)

    def validation(self, fromNum: list, toNum: list):
        record_hits = 0
        numbers = []
        for i in fromNum:
            if i in toNum:
                numbers.append(i)
                record_hits += 1

        self.log_msg += "\nHit: {}, Number: {}".format(record_hits, numbers)

    def result(self):
        print(self.log_msg)