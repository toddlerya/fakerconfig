#!/usr/bin/env python
# coding: utf-8
# @Time     : 2019-03-09 22:31
# @Author   : toddlerya 
# @FileName : generator.py
# @Project  : fakerconfig

import codecs
import requests


base_url = 'http://localhost:8001/api/v1/fakerfactory?number=100&columns=color,job,name,sex,address,idcard,age,mobilephone,email,imid,nickname,username,password,website,url,airport,voyage,airlineinfo,traintrips,trainseat,flightseat,ipv4,ipv6,useragent,mac,imsi,imei,meid,deviceid,telphone,citycode,specialphone,capturetime,date'


def get_data_from_api():
    r = requests.get(base_url)
    if r.status_code != 200:
        raise requests.RequestException(r.status_code)
    resp = r.json()
    data_status = resp['status']['status']
    if data_status != 'ok':
        raise Exception('Server API error: {}'.format(data_status))
    records = resp['data']['records']
    return records


def generator_data(record_list):
    """
    根据api生产的列表字典提取测试数据
    :param record_list:
    :return:
    """
    data_list = list()
    for record in record_list:
        # area_code = record['address']['area_code']
        city_code = record['address']['city_code']
        lat = record['address']['lat']
        lng = record['address']['lng']
        # zip_code = record['address']['zip_code']
        email = record['email']
        idcard = record['idcard']
        job = record['job']
        ipv4 = record['ipv4']
        mobilephone = record['mobilephone']
        telphone = record['telphone']
        # specialphone = record['specialphone']
        # line_data = '\t'.join([area_code, city_code, lat, lng, zip_code, email, idcard, job, ipv4, mobilephone, telphone, specialphone])
        line_data = '\t'.join([city_code, lat, lng, email, idcard, job, ipv4, mobilephone, telphone])
        data_list.append(line_data + '\n')
    return data_list


def write_file(file_name, data_list):
    with codecs.open(file_name, mode='w', encoding='utf-8') as w:
        w.writelines(data_list)


if __name__ == '__main__':
    write_file('data/demo.nb', generator_data(get_data_from_api()))
