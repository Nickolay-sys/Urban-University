import inspect
from pprint import pprint

def introspection_info(obj):
    info_dict: dict = {}
    info_dict["Type"] = type(obj)
    info_dict["attributes"] = dir(obj)
    methods = []
    for attrs in dir(obj):
        attr = getattr(obj, attrs)
        if callable(attr):
            methods.append(attrs)
    info_dict["methods"] = methods
    info_dict["module"] = inspect.getmodule(obj)
    return info_dict

number_info = introspection_info(42)
pprint(number_info)