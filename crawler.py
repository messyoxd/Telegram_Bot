import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

shalaxasca = False
# from selenium.webdriver.common.alert import Alert

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        os.environ['MOZ_HEADLESS'] = '1'
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.PhantomJS()

    def apertaOPopUp(self, driver):
        try:
            dialog = driver.find_element_by_class_name("vex-dialog-button")
            ActionChains(driver).move_to_element(dialog).click().perform()
            time.sleep(5)
            return True          
            # print("ok2")
        except Exception as e:
            print(e)
            return False

    def apertaOBotao(self, driver):
        try:
            elem = driver.find_element_by_tag_name("button")
            # print("ok")
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
            return True
            
        except Exception as e:
            print(e)
            return False

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.ingresso.com/fortaleza/home")
        time.sleep(5)
        if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
            # return driver.current_url
            pass
        try:
            elem2 = driver.find_element_by_class_name("hd-mm-lnk")
            # print("ok3")
        except Exception as e:
            print(e)
            
            
        ActionChains(driver).move_to_element(elem2).click().perform()
        time.sleep(5)
        if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
            # return driver.current_url
            pass
        
        try:
            elem = driver.find_element_by_id("tab-coming-soon")
            # print("ok6")
        except Exception as e:
            print(e)
            # print("not ok6")
            # return driver.current_url
        ActionChains(driver).move_to_element(elem).click().perform()
        time.sleep(5)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
            # return driver.current_url
            pass
        achei = False
        aux = 0
        while not achei:
            try:
                # elem = driver.find_element_by_xpath('//a[@href="/fortaleza/home/filmes/vingadores-ultimato"]')     
                elem = driver.find_element_by_xpath('//a[@href="/fortaleza/home/filmes/chorar-de-rir"]')
                ActionChains(driver).move_to_element(elem).click().perform() 
                # time.sleep(3)          
                achei = True
            except Exception as e:
                # elem.send_keys(Keys.PAGE_DOWN)
                aux+=300
                driver.execute_script("window.scrollTo(0, "+ str(aux) +");")
                
                # print(aux)
                time.sleep(1)  
        
        time.sleep(10)
        print(driver.current_url)
        try:
            elem = driver.find_element_by_xpath('//img[@src="https://ingresso-a.akamaihd.net/catalog/Content/img/error-img-03176b1a6d.jpg"]')
            # print("ok7")
            shalaxasca = True
            return None
        except Exception as e:
            print(e)
            # print("not ok7")
            time.sleep(5)
            shalaxasca = True
            return None
        


    def tearDown(self):
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main(exit=False)