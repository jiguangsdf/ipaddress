# -*- coding:utf-8 -*-
import sys
import requests
import json

def ip_info(ip):
    url='http://api.map.baidu.com/highacciploc/v1?qcip='+ip+'&qterm=pc&ak=tKcMHDudt3Akb0sAaqSIXnZl80bvuTF6&coord=bd09ll&extensions=3'
    poiss=''
    request = requests.get(url)

    info_json= request.content
    info_dic = json.loads(info_json)
    if(
        info_dic.has_key('content')):
        content=info_dic['content']
        country=content['address_component']
        address=content['formatted_address']
        print '该IP地址的具体位置为：'
        print country['country']
        print address
        if (content.has_key('pois')):
            print '该IP地址附近POI信息如下：'
            pois = content['pois']
            for index in range(len(pois)):
                pois_name = pois[index]['name']
                pois_address = pois[index]['address']
                pois_tag= pois[index]['tag']
                print pois_name, pois_address,pois_tag
    else:
        print 'IP地址定位失败'
if __name__ == '__main__':
    ip=raw_input('Please enter the ip :')
    ip_info(ip)
