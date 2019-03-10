#!/usr/bin/env python
# coding: utf-8
# @Time     : 2019-03-10 13:35
# @Author   : toddlerya 
# @FileName : validator.py
# @Project  : fakerconfig


import re


def chinese_char(str_cc):
    """
    校验是否为中文字符
    :param str_cc:
    :return:
    """
    flag = False
    regex = '^[\\u4e00-\\u9fa5]{0,}$'
    if re.match(regex, str_cc):
        flag = True
    return flag


def email(str_email):
    """
    校验是否为邮箱
    :param str_email:
    :return: bool
    """
    flag = False
    regex = '''[\\w!#$%&'*+/=?^_`{|}~-]+(?:\\.[\\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\\.)+[\\w](?:[\\w-]*[\\w])?'''
    # regex = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(regex, str_email):
        flag = True
    return flag


def ipv4(str_ipv4):
    """
    校验是否为ipv4
    :param str_ipv4:
    :return: bool
    """
    flag = False
    regex = '^([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])$'
    if re.match(regex, str_ipv4):
        flag = True
    return flag


def ipv6(str_ipv6):
    """
    ipv6校验
    :param str_ipv6:
    :return: bool
    """
    flag = False
    regex = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
    if re.match(regex, str_ipv6):
        flag = True
    return flag



# TODO 粗略校验，待精确
def id_card15(str_id15):
    """
    校验是否为15位身份证
    :param str_id15:
    :return: bool
    """
    flag = False
    regex = '^[1-9]\\d{7}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d{3}$'
    if re.match(regex, str_id15):
        flag = True
    return flag


# TODO 粗略校验，待精确
def id_card18(str_id18):
    """
    校验是否为18位身份证
    :param str_id18:
    :return: bool
    """
    flag = False
    regex = '^[1-9]\\d{5}[1-9]\\d{3}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d{3}([0-9]|X)$'
    if re.match(regex, str_id18):
        flag = True
    return flag


# TODO 存在缺陷，没匹配国家代号前缀
def cn_telphone(str_telphone):
    """
    校验国内手机号
    :param str_telphone:
    :return:
    """
    flag = False
    regex = '^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\\d{8}$'
    if re.match(regex, str_telphone):
        flag = True
    return flag


if __name__ == '__main__':
    # EMAIL
    # email_test1 = 'ChetMills1958@sdu.edu.cn'
    # print(email(email_test1))
    pass