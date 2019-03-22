import json
import requests
import urllib
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import datetime

shalaxasca = False

site = "https://www.ingresso.com/fortaleza/home/filmes/shazam"
#site = "https://www.ingresso.com/fortaleza/home/filmes/dumbo"

# from selenium.webdriver.common.alert import Alert

class PythonOrgSearch(unittest.TestCase):
    results = {}
    def setUp(self):
        # os.environ['MOZ_HEADLESS'] = '1'
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
        driver.get(site)
        # driver.get("https://www.ingresso.com/fortaleza/home/filmes/capita-marvel")
        # time.sleep(5)
        # if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
        #     # return driver.current_url
        #     pass
        # try:
        #     elem2 = driver.find_element_by_class_name("hd-mm-lnk")
        #     print("ok3")
        # except Exception as e:
        #     print(e)
            
            
        # ActionChains(driver).move_to_element(elem2).click().perform()
        # time.sleep(10)
        # if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
        #     # return driver.current_url
        #     pass
        
        # try:
        #     elem = driver.find_element_by_id("tab-coming-soon")
        #     # print("ok6")
        # except Exception as e:
        #     print(e)
        #     # print("not ok6")
        #     # return driver.current_url
        # ActionChains(driver).move_to_element(elem).click().perform()
        # time.sleep(5)
        # # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # if not self.apertaOBotao(driver) and not self.apertaOPopUp(driver):
        #     # return driver.current_url
        #     pass
        # achei = False
        # aux = 0
        # while not achei:
        #     try:
        #         # elem = driver.find_element_by_xpath('//a[@href="/fortaleza/home/filmes/vingadores-ultimato"]')     
        #         elem = driver.find_element_by_xpath('//a[@href="/fortaleza/home/filmes/chorar-de-rir"]')
        #         ActionChains(driver).move_to_element(elem).click().perform() 
        #         # time.sleep(3)          
        #         achei = True
        #     except Exception as e:
        #         # elem.send_keys(Keys.PAGE_DOWN)
        #         aux+=300
        #         driver.execute_script("window.scrollTo(0, "+ str(aux) +");")
                
        #         # print(aux)
        #         time.sleep(1)  
        
        # time.sleep(10)
        # print(driver.current_url)
        # try:
        #     # elem = driver.find_element_by_xpath('//div[@style="display:none;"]')
        #     elem = driver.find_element_by_xpath('//div[]')
        #     # print("ok7")
        #     # shalaxasca = False
        #     # print("aaaaaaaaaaaaaaaaaa")
        #     # return None
        # except Exception as e:
        #     print(e)
        #     # print("not ok7")
        #     time.sleep(5)
        #     # shalaxasca = True
        #     # return None
        #     print("num achou")
        #     return None
        try:
            elem = driver.find_element_by_xpath('//div[@style="display:none;"][@class="angular-dates"]')
            # print("ok7")
            PythonOrgSearch.results["shalaxasca"] = False
            print("aaaaaaaaaaaaaaaaaa")
            return None
        except Exception as e:
            print(e)
            # print("not ok7")
            # time.sleep(5)
            PythonOrgSearch.results["shalaxasca"] = True
            # return None
            print("n tava display none")
            print(PythonOrgSearch.results["shalaxasca"])
            return None
        


    def tearDown(self):
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main(exit=False)


class Creuza:

    def __init__(self, file_path):
        """
        file_path is a path to a .env file that has a telegram bot token
        """
        with open(file_path, 'r') as f:
            aux = []
            for line in f:
                aux.append(line.split("=")[1].split("\n")[0])
            f.close()
        self.token = aux[0]
        self.chat_id = aux[1]
        # self.channel_id = aux[2]
        self.url = "https://api.telegram.org/bot"+self.token+"/"
    
    def getUrl(self, url):
        """
        sends a GET to the url receives it's response and return as a string
        """
        response = requests.get(url)
        return response.content.decode("utf8")

    def getJSON(self, url):
        """
        gets raw json from url and returns as python dictionary
        """
        raw = self.getUrl(url)
        return json.loads(raw)

    def getUpdates(self, offset=None):
        """
        gets the bot's updates
        offset is a parameter that filters to receive only messages after that offset
        """
        url = self.url+"getUpdates?timeout=100"
        if offset:
            url+="&offset="+str(offset)
        return self.getJSON(url)

    def getLastChatIdAndText(self, lastUpdate):
        chat_id = lastUpdate['result'][len(lastUpdate["result"])-1]['message']["chat"]["id"]
        text = lastUpdate['result'][len(lastUpdate["result"])-1]['message']["text"]
        return (chat_id,text)

    def sendMessage(self, chat_id, text):
        chat_id, text = chat_id, text
        text = urllib.parse.quote_plus(text)
        url = self.url+"sendMessage?text="+ text +"&chat_id="+str(chat_id)
        return self.getUrl(url)

    def setChatTitle(self, chat_id, title):
        chat_id, title = chat_id, title
        title = urllib.parse.quote_plus(title)
        url = self.url+"setChatTitle?title="+ title +"&chat_id="+str(chat_id)
        return self.getUrl(url)

    def getLastUpdateId(self, updates):
        return updates["result"][len(updates['result'])-1]["update_id"]

    def echoAll(self, updates):
        for update in updates['result']:
            try:
                chat_id = update['message']["chat"]["id"]
                text = update['message']["text"]
                self.sendMessage(chat_id, text)
            except Exception as ex:
                print(ex)

    def main(self):
        # last_update_id = None
        while True:
            # shalaxasca = False
            unittest.main(exit=False)
            print(PythonOrgSearch.results)
            if not PythonOrgSearch.results["shalaxasca"]:
                # self.sendMessage(self.channel_id,"Já abriu a pré venda de Vingadores?\nainda não fera, foi mal")
                # self.sendMessage(self.chat_id,"Já abriu a pré venda de Vingadores?\nainda não fera, foi mal")
                # self.sendMessage(self.chat_id,"n abriu n")                
                self.setChatTitle(self.chat_id, (str(datetime.datetime.now())).split('.')[0])
                # pass
            else:
                self.sendMessage(self.chat_id,"A pré-estréia abriu -> %s" % site)
            time.sleep(15*60)
            # updates = self.getUpdates(last_update_id)
            # print(updates)
            # if len(updates['result']) > 0:
            #     last_update_id = self.getLastUpdateId(updates)+1
            #     self.echoAll(updates)
            

# if __name__ == "__main__":
bot = Creuza(".env")
bot.main()
