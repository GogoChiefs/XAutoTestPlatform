global_dict={}

def _init():
    global global_dict
    global_dict = {}

def set_value(key,value):
    """ 定义一个全局变量 """
    global_dict[key] = value

def get_value(key,defValue=None):
    try:
        return global_dict[key]
    except KeyError:
        return defValue