def get_dict_value(date, keys, default=None):
    #default=None，在key值不存在的情况下，返回None
    keys_list = keys.split('.')
    #以“.”为间隔，将字符串分裂为多个字符串，其实字符串为字典的键，保存在列表keys_list里
    if isinstance(date,dict):
        #如果传入的数据为字典
        dictionary = dict(date)
        #初始化字典
        for i in keys_list:
            #按照keys_list顺序循环键值
            try:
                if dictionary.get(i) != None:
                    dict_values = dictionary.get(i)
                #如果键对应的值不为空，返回对应的值
                # elif dictionary.get(i) == None:
                #     dict_values = dictionary.get(str(i))
                #如果键对应的值为空，将字符串型的键转换为整数型，返回对应的值
            except:
                return default
                    #如果字符串型的键转换整数型错误，返回None
            dictionary = dict_values
        return dictionary
    # else: 
    #     #如果传入的数据为非字典
    #     try:
    #         dictionary = dict(eval(date))
    #         #如果传入的字符串数据格式为字典格式，转字典类型，不然返回None
    #         if isinstance(dictionary,dict):
    #             for i in keys_list:
    #                 #按照keys_list顺序循环键值
    #                 try:
    #                     if dictionary.get(i) != None:
    #                         dict_values = dictionary.get(i)
    #                     #如果键对应的值不为空，返回对应的值
    #                     elif dictionary.get(i) == None:
    #                         dict_values = dictionary.get(int(i))
    #                     #如果键对应的值为空，将字符串型的键转换为整数型，返回对应的值
    #                 except:
    #                     return default
    #                         #如果字符串型的键转换整数型错误，返回None
    #                 dictionary = dict_values
    #             return dictionary
    #     except:
    #         return default
 

dicttest={"result":{"code":"110002","msg":"设备设备序列号或验证码错误"}}
ret=get_dict_value(dicttest, 'result.msg')
print(ret)