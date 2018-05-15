from config import configuration


def method1():
    configuration["db"] = "amwater"
    return configuration["db"]


def method2():
    return 2
