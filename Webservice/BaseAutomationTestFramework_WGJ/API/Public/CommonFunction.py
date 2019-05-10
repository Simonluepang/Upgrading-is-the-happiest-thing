import warnings,pymysql,yaml, xmltodict,random,time,requests,json,csv
from datetime import datetime,timedelta
warnings.filterwarnings("ignore")
from API.Public.AssertFunction import *
from API.Setting import *



#创建cookie文件
try:
    open(Path["cookieRoot"],'r')
except:
    open(Path["cookieRoot"], 'w')

if open(Path['cookieRoot'],'r').readline()!="":
    token = eval(open(Path['cookieRoot'],'r').readline())['cookies']

global URL
URL =Config['mainUrl']
g_APICoverage,g_InterfacePerformance=[],[]

class Headers:
    def headers(self):

        headers = {
                    "Cookie": token}

        return headers

    def headers_application_json(self):

        headers = {
                    "Cookie": token,
                    'Content-type': 'application/json'}

        return headers

    def headers_token(self,tokenProject):
        headers = {
                    "Cookie": token,
                    'token': tokenProject}
        return headers

    def headers_token_aplication_json(self,tokenProject):
        headers = {
                    "Cookie": token,
                    'token': tokenProject,
                   'Content-type': 'application/json'}
        return headers

class MySQL:
    def __GetConnect(self):
        conn=pymysql.connect(host=MySQLDB[Config['Env']]['host'],port=int(MySQLDB[Config['Env']]['port']),user=MySQLDB[Config['Env']]['user'],password=MySQLDB[Config['Env']]['password'],database=MySQLDB[Config['Env']]['database'],charset='gbk')
        cur=conn.cursor()  #将数据库连接信息，赋值给cur。
        if not cur:raise(NameError,"连接数据库失败")
        else:return cur

    def queryMySql(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.__GetConnect().close()
        if resList ==() : assert False,'数据找不到'
        return resList

class TimeRange:
    def get_recenct_days(self,days):
        '''
        根据输入的天数来获得最近n天的日期
        :param days: 7
        :return: 2018-09-07
        '''
        startDate = (datetime.now() - timedelta(days=days)).date()
        endDate = datetime.now().date()
        return startDate,endDate

def getGlobalParams():
    context = open(Path['globalParams'],'r').read()
    result =  eval(context)
    result['token']=json.dumps(eval(result['token']))
    return result

def yamlinterpreter(documentname,filename,caseName):
    filepath = Path['Data']+os.sep+documentname+os.sep+filename
    f =  open(filepath,"r",encoding='gbk')
    result = yaml.load(f.read())
    return result[caseName]

def dict_generator(indict, pre=None):
    try:
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    if len(value) == 0:yield ["_".join(pre)+'_'+key, '{}']
                    else:
                        for d in dict_generator(value, pre + [key]):yield d
                elif isinstance(value, list):
                    if len(value) == 0:yield ["_".join(pre)+'_'+key, '[]']
                    else:
                        for v in value:
                            for d in dict_generator(v, pre + [key]):yield d
                elif isinstance(value, tuple):
                    if len(value) == 0:yield ["_".join(pre)+'_'+key, '()']
                    else:
                        for v in value:
                            for d in dict_generator(v, pre + [key]):yield d
                else:
                    if pre!=[]:yield ["_".join(pre)+'_'+key, value]
                    else:yield [key, value]
        elif isinstance(indict, list):
            for values in indict:
                for d in dict_generator(values):yield d
    except BaseException as e:
        print(str(e))

def response(data):
    try:
        templist,result,key =[],{},[]
        result["status_code"] = data.status_code
        result['headers'] = data.headers
        result['responsetime'] = data.elapsed.microseconds/1000
        try:
            for i in dict_generator(data.json()):templist.append(i)
        except:
            for i in dict_generator(eval(json.dumps(dict(xmltodict.parse(data))))):templist.append(i)
        for value in templist:key.append(value[0])
        for keys in list(set(key)):
            result[keys]=[]
            for values in templist:
                if keys == values[0]:result[keys].append(values[1])
        return result
    except BaseException as e:
        print(str(e))

def CallAPI(documentname,filename,caseName,operationName,globalParams={}):
    value = yamlinterpreter(documentname,filename,caseName=caseName)
    filepath = Path['swagger']+os.sep+documentname+'.json'
    with open(filepath,'r',encoding='gbk') as load_f:temp =load_f.read()
    params = getGlobalParams()
    APIDetail =eval(temp)
    tempdetail=APIDetail[operationName]
    #填充YAML的字段
    if value[operationName]!="None":
        for eachparams in value[operationName]:
            if ("@"+str(list(eachparams.keys())[0])+"@") in str(APIDetail[operationName]):
                tempdetail=str(tempdetail).replace("@"+str(list(eachparams.keys())[0])+"@",eachparams[str(list(eachparams.keys())[0])])
    #填充手动填入的全局字段
    if globalParams!={}:
        for key in globalParams:
            if ("@"+str(key)+"@") in str(APIDetail[operationName]):
                    tempdetail=str(tempdetail).replace("@"+str(key)+"@",str(globalParams[key]))
    #填充全局字段
    for globalkey in params:
        if ("@"+str(globalkey)+"@") in str(APIDetail[operationName]):
            tempdetail=str(tempdetail).replace("@"+str(globalkey)+"@",str(params[globalkey]))
    tempdetail=tempdetail.replace('@Cookie@',token)
    results = interface(eval(tempdetail))
    return results

def interface(params):
    url =URL +params['URL']
    if str(params['Type']).upper() =='GET':
        result = response(WebRequests().get(url,json.dumps(params['Body']),params['Headers']))
    elif str(params['Type']).upper() =='POST':
        result = response(WebRequests().post(url,json.dumps(params['Body']),params['Headers']))
    elif  str(params['Type']).upper() =='DELETE':
        result = response(WebRequests().delete(url,json.dumps(params['Body']),params['Headers']))
    return result

def getYAMLValue(documentname,filename,caseName,operationName):
    value = yamlinterpreter(documentname,filename,caseName)
    return value[operationName]

def generate_random_str(randomlength=8):
    random_str,base_str  = '','ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def createInterfacePerformance():
    #接口性能代码
    global g_InterfacePerformance
    Path['InterfacePerformance'],context = Path['InterfacePerformance']+time.strftime("%Y%m%d_%H_%M", time.localtime(int(time.time())))+'_InterfacePerformance.csv', '模块名,接口名,预期时间(ms),实际时间（ms）'+'\n'
    if g_InterfacePerformance!=[]:
        allInfo = context+"".join(g_InterfacePerformance)
        if  os.path.exists(Path['InterfacePerformance']):
            with open(Path['InterfacePerformance'],"a+") as f:
                f.write("".join(g_InterfacePerformance))
        else:
            with open(Path['InterfacePerformance'],"a+") as f:
                f.write(allInfo)

def checkAPICoverageRate(status='check'):
    global g_APICoverage
    headers=['Module','Interface','Coverage','Note']
    if status=='check':
        APIList_called = list(set(g_APICoverage))
        with open(Path['APICoverageRate'],encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row for row in reader]
        APIList_csv=[value['Interface'] for value in column]
        if APIList_called!=[]:
            for name in APIList_called:
                if name.split('.')[1] in APIList_csv:column[APIList_csv.index(name.split('.')[1])]['Coverage']='Y'
                else: column.append({'Module':name.split('.')[0],'Interface':name.split('.')[1],'Coverage':'Y','Note':'Please Check!'})
            with open(Path['APICoverageRate'], 'w+', newline='') as f:
                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                for row in column:
                    writer.writerow(row)
    elif status=='Init':
        with open(Path['APICoverageRate'],encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row for row in reader]
        for value in column:
            value['Coverage'],value['Note']="",""
        with open(Path['APICoverageRate'], 'w+', newline='') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for row in column:
                writer.writerow(row)

def deleteRedundantPerformanceCSVFile():
    if not os.path.exists(Path['InterfacePerformance']):os.makedirs(Path['InterfacePerformance'])
    dir_list = os.listdir(Path['InterfacePerformance'])
    if int(Config['PerformanceStatistics'])<(len([lists for lists in os.listdir(Path['InterfacePerformance']) if os.path.isfile(os.path.join(Path['InterfacePerformance'], lists))])):
        if not dir_list:pass
        else:
            dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(Path['InterfacePerformance'], x)),reverse=True)[int(Config['PerformanceStatistics']):]
            for filename in dir_list:
                os.remove(Path['InterfacePerformance']+filename)

if __name__ == '__main__':
    #yamlinterpreter(r'D:\AutomationTest_myluban\AutomationTest_myluban\Data\ExpectedValue')
    #CallAPI('photoAlbum_controller','addAlbum','addAlbum_success')
    #getYAMLValue('photoAlbum_controller','addAlbum','addAlbum_success','a')
    checkAPICoverageRate(status='Init')




