Webdriver的工作原理
--
在new一个webdriver的过程中，selenium首先会确认浏览器的native component是否存在可用并且版本匹配。然后会在目标浏览
器里启动一整套的webservice。

由于客户端脚本不能直接与浏览器通信，所以此时webservice充当了一个翻译器的作用，它可以把客户端岱庙翻译成浏览器可以识别的代码（比如js）。客户端创建一个session，在该session中通过http请求向webservice发送restful请求，webservice翻译成浏览器懂得的脚本传给浏览器，浏览器再把执行结果返回给webservice，webservice把返回的结果做一些封装（一般都是json格式）再返回给client，然后根据返回值就能判断对浏览器的操作是不是成功。

selenium如何操作隐藏元素
--
元素的属性隐藏和显示，主要是 type="hidden"和 style="display: none;"属性来控制的，隐藏的元素是可以定位到的。

现在来操作一下隐藏的元素，selenium是不支持操作隐藏元素的，所以需要用JS来操作隐藏元素

    js = 'document.getElementById("baidu").click()'
    
    driver.execute_script(js)
    
selenium如何切换iframe
--
1.切入iframe

    driver.switch_to_frame("")
    
    driver.switch_to.frame("")
    
2.从子iframe切回父iframe

    driver.switch_to.parent_frame()
    
3.从iframe中切回主文档

    driver.switch_to.default_content()
    
判断元素是否存在
--
```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def isElementExsist(driver,location):
    try:
        WebDriverWait(driver,30,1).until(EC.presence_of_element_located(location))
        return True
    except:
        return False
```

子元素定位父元素
--

    elementParent = driver.find_element_by_name("son").parent