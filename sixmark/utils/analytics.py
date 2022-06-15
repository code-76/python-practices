import numpy as np
from data.local.local_number_datasource import LocalNumberDataSource
from data.analytics_mode import NumberAnalyticsMode, NumberSearchMode
from data.remote.remote_number_datasource import RemoteNumberDataSource
from utils.debug import DebugLogger

class Analytics:
    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.debugLogger = DebugLogger()
        self.dataSource.__class__ = LocalNumberDataSource if type(dataSource) is LocalNumberDataSource else RemoteNumberDataSource

    def log_level(self, level):
        self.debugLogger.log_level(level)

    def in_range_count(self, slot, by=0, to=0):
        count = 0
        for num in slot:
            if num in range(by, to):
                count += 1
        return count

    def odd_even_count(self, slot):
        odd = 0; even = 0
        for num in slot:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        return odd, even

    def recollect(self, **kwargs):
        match kwargs.get("mode", NumberAnalyticsMode.TYPE):
            case NumberAnalyticsMode.TYPE:
                return self._collect_number_type(
                    skip=kwargs.get("skip", 0), 
                    size=kwargs.get("size", len(self.dataSource.get_slots()) - 1), 
                    avg=kwargs.get("avg", True)
                )
            case NumberAnalyticsMode.TRACE:
                return self._collect_trace(
                    by=kwargs.get("by", 0),
                    scope=kwargs.get("scope", 2),
                    skip=kwargs.get("skip", 1),
                    time=kwargs.get("time", 1)
                )
            case NumberAnalyticsMode.RANGE:
                return self._collect_number_by(
                    scope=kwargs.get("scope", 1),
                    level=kwargs.get("level", 0),
                    by=kwargs.get("by", 0),
                    to=kwargs.get("to", 0)
                )
            case _:
                return {}
          
    def validation(self, fromNum: list, toNum: list):
        collect = {}; hits = 0; numbers = []
        for i in fromNum:
            if i in toNum:
                numbers.append(i)
                hits += 1
        collect.update({"hits": hits, "numbers": numbers})
        self._log("debug", "validation: {}".format(collect))
        return collect

    def _hit_number(self, fromNum, toNum):
        result = []
        for i in fromNum:
            if i in toNum and i not in result:
                result.append(i)
        return result
      
    def _trace_hit_one_by_one(self, slots=[]):
        result = []; slotBy = slots[0]
        self._log("debug", "_trace_hit_one_by_one by: {}".format(slotBy))
        for slot in slots[1:]:
            self._log("debug", "_trace_hit_one_by_one slot: {}".format(slot))
            result = result + self._hit_number(slotBy, slot)

        self._log("debug", "_trace_hit_one_by_one: {}".format(result))
        return self._distinct_count(result)

    def _collect_trace(self, by = 0, scope = 0, skip = 0, time=0):
        collect = {}; hitNumbers = []
        scope = scope + 1 if by <= 0 else by
        skip = skip - 1 if by <= 0 else by
        while time > 0:
            slots = self.dataSource.search(mode=NumberSearchMode.SLOTS, skip=skip, size=scope)
            if slots is None or len(slots) <= 0:
                break

            self._log("debug", "_collect_trace slots: {}".format(slots))
            hitNumbers.append(self._trace_hit_one_by_one(slots))
            skip += 1
            time -= 1

        collect.update({"numbers": hitNumbers})
        self._log("info", "_collect_trace collect: {}".format(collect))
        return collect
  
    def _in_range(self, slot, by, to):
        result = []
        for num in slot:
            if num in range(by, to):
                result.append(num)
        return result

    def _in_number_type(self, slot):
        collect = {}; odd = []; even = []
        for num in slot:
            if num % 2 == 1:
                odd.append(num)
            elif num % 2 == 0:
                even.append(num)
        
        collect.update({"odd": odd, "even": even})
        self._log("debug", "_in_number_type: {}".format(collect))
        return collect

    def _collect_number_by(self, scope=0, level=0, by=0, to=0):
        collect = {}; odd = []; even = []; inRange = []
        slots = self.dataSource.search(mode=NumberSearchMode.SLOTS, size=scope)
        if slots is None or len(slots) <= 0:
            return {}

        self._log("debug", "_collect_number_by slots: {}".format(slots))
        
        for slot in slots:
            inRange = inRange + self._in_range(slot, by, to)
            numbers = self._in_number_type(slot)
            odd = odd + numbers["odd"]
            even = even + numbers["even"]

        if level > 0:
            oddWithLevel = [x[0] for x in self._distinct_count(odd) if x[1] >= level]
            evenWithLevel = [x[0] for x in self._distinct_count(even) if x[1] >= level]
            inRangeWithLevel = [x[0] for x in self._distinct_count(inRange) if x[1] >= level]
            collect.update({"odd": oddWithLevel, "even": evenWithLevel, "in_range": inRangeWithLevel})
            self._log("info", "_collect_number_by with level: {}".format(collect))
        else:
            collect.update({"odd": odd, "even": even, "in_range": inRange})
            self._log("info", "_collect_number_by: {}".format(collect))
        return collect

    def _collect_number_type(self, skip=0, size=0, avg=True):
        colloct = {}; single = []; double10 = []; double20 = []; double30 = []; double40 = []; odd = []; even = []
        while slots := self.dataSource.search(mode=NumberSearchMode.SLOTS, skip=skip, size=size):
            for slot in slots:
                self._log("debug", "_collect_number_type slot: {}".format(slot))
                single.append(self.in_range_count(slot, by=1, to=9))
                double10.append(self.in_range_count(slot, by=10, to=19))
                double20.append(self.in_range_count(slot, by=20, to=29))
                double30.append(self.in_range_count(slot, by=30, to=39))
                double40.append(self.in_range_count(slot, by=40, to=49))
                oddAndEven = self.odd_even_count(slot)
                odd.append(oddAndEven[0])
                even.append(oddAndEven[1])

            skip = skip + size

        colloct.update({"odd": odd, "even": even, "single": single, "double10": double10, "double20": double20, "double30": double30, "double40": double40})
        self._log("debug", "_collect_number_type: original {}".format(colloct))

        odd = [] if len(odd) == 0 else round(np.average(odd)) if avg else np.max(odd) 
        even = [] if len(even) == 0 else round(np.average(even)) if avg else np.max(even)
        single = [] if len(single) == 0 else round(np.average(single)) if avg else np.max(single)
        double10 = [] if len(double10) == 0 else round(np.average(double10)) if avg else np.max(double10)
        double20 = [] if len(double20) == 0 else round(np.average(double20)) if avg else np.max(double20)
        double30 = [] if len(double30) == 0 else round(np.average(double30)) if avg else np.max(double30)
        double40 = [] if len(double40) == 0 else round(np.average(double40)) if avg else np.max(double40)

        colloct.update({"odd": odd, "even": even, "single": single, "double10": double10, "double20": double20, "double30": double30, "double40": double40})
        self._log("info", "_collect_number_type avg: {}".format(colloct))
        return colloct

    def _distinct(self, lists1, lists2):
        return np.unique(lists1, lists2)

    def _distinct_count(self, lists):
        unique, counts = np.unique(lists, return_counts=True)
        result = np.column_stack((unique, counts)).tolist()
        self._log("debug", "_distinct_count: {}".format(result))
        return result

    def log(self):
        self.debugLogger.log()

    def _log(self, level, message):
        self.debugLogger.info(level, message)