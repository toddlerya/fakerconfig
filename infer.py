#!/usr/bin/env python
# coding: utf-8
# @Time     : 2019-03-10 12:42
# @Author   : toddlerya 
# @FileName : infer.py
# @Project  : fakerconfig


import codecs
import numpy as np
from collections import defaultdict
from validator import validator


def reader(file_name, sep='\t'):
    """
    读取行列文件返回嵌套列表
    :param file_name:
    :return:
    """
    matrix = list()
    with codecs.open(file_name, mode='r', encoding='utf-8') as r:
        for line in r:
            split_line = line.rstrip('\n').split(sep=sep)
            matrix.append(split_line)

    # 清洗数据，计算每一行的列数，取占比为95%的列数为正确列数，其他舍去
    col_length_dict = defaultdict(list)
    raw_total_line_count = len(matrix)
    most_col_length = 0
    for line, line_list in enumerate(matrix):
        col_length = len(line_list)
        col_length_dict[col_length].append(line)
    for k, v in col_length_dict.items():
        if len(v) / raw_total_line_count > 0.9:
            most_col_length = k
    if most_col_length != 0:
        print('当前行列数据的列数90%都是{}'.format(most_col_length))
    else:
        raise Exception('无法判断当前行列数据的列数应该是多少，请检查数据是否合法！')

    for k, v in col_length_dict.items():
        if k != most_col_length:
            for each in v:
                print('剔除残缺数据：{}'.format(matrix.pop(each)))
    print('==' * 40)
    return matrix


def transpose(matrix):
    """
    对行列数据进行列表转置
    :param matrix:
    :return:
    """
    old_matrix = np.array(matrix)
    new_matrix = old_matrix.T
    return new_matrix


def matcher(item_list):
    """
    计算类型可信度
    :param item_list:
    :return: dict {'data_type': 0.0}
    """
    match_type_dict = defaultdict(list)
    all_ele_count = len(item_list)
    probability = dict()
    for item in item_list:
        if validator.email(item):
            match_type_dict['email'].append(item)
        elif validator.ipv4(item):
            match_type_dict['ipv4'].append(item)
        elif validator.id_card15(item):
            match_type_dict['id_card15'].append(item)
        elif validator.id_card18(item):
            match_type_dict['id_card18'].append(item)
        else:
            match_type_dict['unknown'].append(item)
    most_percent = 0.0
    for k, v in match_type_dict.items():
        percent = len(v) / all_ele_count
        if percent > most_percent:
            most_percent = percent
            probability[k] = percent
    return probability


if __name__ == '__main__':
    match_matrix = transpose(reader('data/demo.nb'))
    for col_index, each in enumerate(match_matrix):
        print('== col index {} =='.format(col_index))
        # matcher(each)
        print(matcher(each))
