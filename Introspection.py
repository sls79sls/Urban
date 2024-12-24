import sys
import requests
import inspect




def introspection_info(obj):
    dict_intro["Type"] = type(obj)
    dict_intro["Names"] = requests.__name__
    dict_intro["Attribute"] = dir(requests)
    dict_intro["Module"] = inspect.ismodule(obj)
    dict_intro["List_arg"] = sys.argv

    return dict_intro

if __name__ == '__main__':
    dict_intro = {}
    number_info = introspection_info(requests)
    print (dict_intro)
    # for i in number_info:
    #     print(i)
    #     #print(number_info)
