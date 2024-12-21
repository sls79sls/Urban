import sys
import requests
import inspect




def introspection_info(obj):

    return type(obj), requests.__name__, dir(requests), inspect.ismodule(obj), sys.argv


if __name__ == '__main__':

    number_info = introspection_info(requests)
    for i in number_info:
        print(i)
        #print(number_info)
