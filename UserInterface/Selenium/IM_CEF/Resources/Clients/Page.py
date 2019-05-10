import unittest, selenium.webdriver, time,requests,re

class Page(unittest.TestCase):

    APPLICATION_PATH = r'BimIm.exe'
    #TEST_PAGE_PATH = r'file:///config/WebPag/Login.html'
    #TEST_PAGE_PATH = 'http://192.168.13.215:8082/LBIM/index.jsp'
    TEST_PAGE_PATH = 'http://192.168.13.195:8989/dist/#/companyprofile/organization-structure'


    def setUp(self):
        options = selenium.webdriver.ChromeOptions()
        #options.binary_location = self.APPLICATION_PATH
        self.driver = selenium.webdriver.Chrome (chrome_options=options)
        #self.driver.get(self.TEST_PAGE_PATH)
    
    def test_IM_Login(self):
        driver = self.driver    
        self.driver.get(self.TEST_PAGE_PATH)
        a1 =self.driver.get_cookies()
        print(a1)
        self.driver.delete_all_cookies()
        print(a1)
        self.driver.add_cookie({
                'name' : 'JSESSIONID',
                'value' : '22605EDD3CC7E629A72457874D2DA5E7'
            })
        print(a1)
        self.driver.refresh()
        print(a1)
        time.sleep(3)
        '''
        username = driver.find_element_by_xpath('//*[@id="userName"]')
        password = driver.find_element_by_xpath('//*[@id="password"]')
        server_address = driver.find_element_by_xpath('//*[@id="servaddr"]')
        login_Button = driver.find_element_by_xpath('/html/body/form/input[4]');

        username.send_keys('xushenwei')
        password.send_keys('111111')
        server_address.send_keys('192.168.13.215:8082/pds')
       	login_Button.click()
        cookie = self.driver.get_cookies()
        time.sleep(5)
        print(cookie)
        '''
        
    """
    def test_login(self):

        # Login(登录pds-GET)
        PDS_URL = 'http://192.168.13.215:8082/pds'
        r1 = requests.get(url=PDS_URL+'/login')
        # 查询Cookie_pds
        Cookie_pds = r1.headers['Set-Cookie']
        text1 = r1.text
        # 查找含有LT的这行string，截取出来
        compile1 = re.compile(r'      <input type="hidden" name="lt" value="LT.*? />')
        find_LT = compile1.findall(text1)
        ltvalue = find_LT[0]
        ltvalue = list(ltvalue)
        ltvalue = ltvalue[44:-4]
        ltvalue = ('').join(ltvalue)
        # Login(登录pds-POST)
        logindata0 = {
            '_eventId' : 'submit',
            'execution' : 'e1s1',
            'lt' : ltvalue,
            'password' : '96e79218965eb72c92a549dd5a330112',
            'productId' : '40',
            'submit' : '%E7%99%BB%E5%BD%95',
            'username' : 'im测试员',

        }
        loginheaders0 = {
            'Cookie' : Cookie_pds,
            'REQUEST' : 'application/x-www-form-urlencoded'
        }
        r2 = requests.post(url=PDS_URL+'/login', data=logindata0, headers=loginheaders0)
        # 查询TGT
        Set_Cookie = r2.headers['Set-Cookie']
        TGT = list(Set_Cookie)
        TGT = TGT[66:-12]
        TGT = ('').join(TGT)
        # Method1(LBLD跳转)
        logindata1 = {
            'service' : 'http://192.168.13.215:8082/LBIM/webservice/lbws/contractlistservice?wsdl&qwea'

        }
        loginheaders1 = {
            'Cookie' : Cookie_pds+';'+TGT,
        }
        # 这一步会有网页自动跳转，添加参数以防止自动跳转来抓取location
        r3 = requests.post(url=PDS_URL+'/login', data=logindata1, headers=loginheaders1, allow_redirects = False)
        LBLD_URL_302 = r3.headers['Location']
        # LBLD_URL_302(跳转)
        logindata2 = {
            'function' : '登录',
            'functionGroup' : '打开软件'
        }
        r4 = requests.post(url=LBLD_URL_302, data=logindata2, allow_redirects = False)
        Cookie_LBLD = r4.headers['Set-Cookie']
        print(Cookie_LBLD)

        driver = self.driver
        self.driver.get(self.TEST_PAGE_PATH)
        print(driver.get_cookies())
        self.driver.delete_all_cookies()
        #print(driver.get_cookies())
        
        self.driver.add_cookie({
                'name' : 'JSESSIONID',
                'value' : Cookie_LBLD
            })
        print(driver.get_cookies())
        #self.driver.refresh()
        '''
        self.driver.add_cookie({

            })
        '''
        #print(driver.get_cookies())
        #self.driver.get(self.TEST_PAGE_PATH)
        time.sleep(3)
        '''
        driver.get('http://192.168.13.215:8082/LBIM/index.jsp')
        selenium.webdriver.chrome.options.Options().add_experimental_option('Cookie', 'JSESSIONID=E056D300ADF467E075D501A3FED7F12A; route=')
        print(selenium.webdriver.chrome.options.Options().arguments)
        
        driver.add_cookie({
                'name' : 'Cookie',
                'value' : 'JSESSIONID=3E3E108273641A49432A1E881FF75B93',
                'path' : '192.168.13.215:8082'
            })
        driver.get('http://192.168.13.215:8082/LBIM/index.jsp')
        '''
    """

        
   
    



    def tearDown(self):
        self.driver.close()
    

if __name__ == "__main__":
    unittest.main()
