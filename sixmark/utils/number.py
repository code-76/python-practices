from cgitb import reset
import numpy as np

class NumberHandler:
    def merge(self, result: list, *args):
        for arg in args:
            for i in arg:
                if type(i) is int:
                    result.append(i)
                elif type(i) is list:
                    result += i
        return result

    def toList(self, *args):
        result = []
        for arg in args:
            for i in arg:
                if type(i) is int:
                    result.append(i)
                elif type(i) is list:
                    result += i
        return result

    def add(self, *args):
        result = []
        if type(args) is tuple:
            for arg in args:
                for i in arg:
                    if type(i) is int:
                        result.append(i)
                    elif type(i) is list:
                        result += i
        return result
        
    def distinct(self, list):
        x = np.array(list)
        return np.unique(x)

    def log(self, message, **kwargs):
        print(message.format(kwargs))