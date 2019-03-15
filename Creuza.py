import json
import requests
import urllib
from crawler import *
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
        self.channel_id = aux[2]
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
            unittest.main(exit=False)
            print(shalaxasca)
            if shalaxasca:
                # self.sendMessage(self.channel_id,"Já abriu a pré venda de Vingadores?\nainda não fera, foi mal")
                # self.sendMessage(self.chat_id,"Já abriu a pré venda de Vingadores?\nainda não fera, foi mal")
                self.sendMessage(self.channel_id,"Já abriu a pré venda de chorar-de-rir(é o teste pro vingadores)?\nainda não fera, foi mal")
            else:
                self.sendMessage(self.channel_id,"A pré-estréia abriu -> https://www.ingresso.com/fortaleza/home/filmes/chorar-de-rir")
            time.sleep(15*60)
            # updates = self.getUpdates(last_update_id)
            # print(updates)
            # if len(updates['result']) > 0:
            #     last_update_id = self.getLastUpdateId(updates)+1
            #     self.echoAll(updates)
            

if __name__ == "__main__":
    bot = Creuza(".env")
    bot.main()
