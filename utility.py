vars = set()
classes = set()
types = {'bool': "boolean",
         'char': "char",
         'byte': "byte",
         'short': "short",
         'int': "int",
         'long': "long",
         'double': "double",
         'float': "float"}


def findVar(name):
    return name in vars


def addVar(name):
    if name not in vars:
        vars.add(name)
        return True
    return False


def addclass(name):
    classes.add(name)


def isType(type):
    return type in (list(classes) + types)


def convert(type):
    return types[type]
