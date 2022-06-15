from data.debug_mode import DebugLogLevel

class DebugLogger:
    def __init__(self, debug_level=DebugLogLevel.NONE):
        self.debug_level = debug_level
        self.log_mssage = {"debug": "", "info": ""}

    def log_level(self, level):
        self.debug_level = level

    def log(self):
        match self.debug_level:
            case DebugLogLevel.ALL:
                for k, v in self.log_mssage.items():
                    print("{} : {}\n".format(k, v))
            case DebugLogLevel.INFO:
                print("{}".format(self.log_mssage["info"]))
            case DebugLogLevel.DEBUG:
                print("{}".format(self.log_mssage["debug"]))
            case _:
                pass

    def info(self, level, info):
        message = self.log_mssage.get(level)
        self.log_mssage.update({level: "{}\n{}".format("" if message is None else message, info)})