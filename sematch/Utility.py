import json
import ConfigParser
import os

class Configuration:

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('settings.cfg')

    def getConfig(self,section,variable):
        return self.config.get(section,variable)


class FileIO:

    @staticmethod
    def path():
        return os.path.dirname(__file__)

    @staticmethod
    def filename(name):
        if FileIO.path() not in name:
            name = os.path.join(FileIO.path(), name)
        return name

    @staticmethod
    def read_json_file(name):
        data = []
        with open(FileIO.filename(name),'r') as f:
            for line in f:
                data.append(json.loads(line))
        return data

    @staticmethod
    def save_json_file(name, data):
        with open(FileIO.filename(name), 'w') as f:
            for d in data:
                json.dump(d, f)
                f.write("\n")

    @staticmethod
    def append_json_file(name, data):
        with open(FileIO.filename(name), 'a') as f:
            for d in data:
                json.dump(d, f)
                f.write("\n")

    @staticmethod
    def save_list_file(name, data):
        with open(FileIO.filename(name),'w') as f:
            for d in data:
                f.write(d)
                f.write('\n')

    @staticmethod
    def read_list_file(name):
        with open(FileIO.filename(name),'r') as f:
            data = [line.strip() for line in f]
        return data


def trace(f):
    def g(x):
        print f.__name__, x
        value = f(x)
        print 'return', repr(value)
        return value
    return g


# config = Configuration()
# print type(config.getConfig('expansion','sim'))
# print type(config.getConfig('expansion', 'th'))
# print config.getConfig('expansion','gpcs')