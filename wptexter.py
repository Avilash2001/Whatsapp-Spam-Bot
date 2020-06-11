from selenium import webdriver
from time import sleep
from random import randint

class WPBot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get("https://web.whatsapp.com/")
        print("Scan the QR from your phone within 20 seconds and after you scan wait!")
        sleep(20)
    
    def action(self,i,times):    
        text=self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        if i==0:
            text.send_keys(f'Hi! I am an intelligent software created by Avilash Ghosh. \nI will now send you {times} texts!\nThank You for your time!')
        else:
            text.send_keys(f'Text no: {i}')
        
        send_btn=self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_btn.click()

bot=WPBot()
bot.login()
while True:
    print("Click on the person you want to text")
    times=int(input("Enter the no of texts: "))
    for i in range(times+1):
        bot.action(i,times)
    choice=input("Wanna Go again?? (Y/N) ")
    if choice == 'N' or choice == 'n':
        break
