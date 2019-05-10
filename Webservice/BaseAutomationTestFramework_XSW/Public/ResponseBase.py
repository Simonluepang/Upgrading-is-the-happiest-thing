#coding=utf-8

import xmltodict
import json

def pythonXmlToJson(xmlStr):

    convertedDict = xmltodict.parse(xmlStr)
    jsonStr = json.dumps(convertedDict, indent=1)
    return jsonStr


def resp_base(data):
    result = {}
    result["status_code"] = data.status_code
    result['headers'] = data.headers
    return result


def Recombition_list(keys,data_list):
    '''
    :将list根据key重组
    :param keys:["epid","orgId"]
    :param data_list:
         [{
            "epid": 1,
            "orgId": "7c01a75941549a705cf7275e41b21f0b"

        }, {
            "epid": 713,
            "orgId": "8c01a75941549a705cf7275e41b21f0d"
        }]
    :return:
            result = {'epid_list': [1, 713], 'orgId_list': ['7c01a75941549a705cf7275e41b21f0b', '8c01a75941549a705cf7275e41b21f0d']}
    '''

    result = {}

    for key in keys:
        result[key+"_list"] = []

    for data in data_list:
        for key in keys:
            result[key +"_list"].append(data.get(key))
    return result
