#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    for key, value in new_dic.items():
        new_dic[key] = value * 2
    return new_dic
