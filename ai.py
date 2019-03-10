#!/usr/bin/env python
# coding: utf-8
# @Time     : 2019-03-09 23:06
# @Author   : toddlerya 
# @FileName : ai.py
# @Project  : fakerconfig

import numpy as np
import pandas as pd


def read_sample(file_name):
    table_dataframe = pd.read_csv(file_name, sep='\t')
    print(table_dataframe.head())


if __name__ == '__main__':
    read_sample('data/demo.nb')