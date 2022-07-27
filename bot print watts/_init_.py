
# comandos a serem executados no pronpt de camonado para instalação de bibliotecas necessarias para
# execussao do script

# pip install --upgrade pip
# pip install selenium
# pip install pyautogui
# pip install pywinautogui

from ast import Try
from ssl import Options
from selenium import webdriver
from PIL import ImageGrab,Image
from pywinauto import keyboard,clipboard
import time
import os
import base64
import json
import pyautogui


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # self.mensagem = "TESTE DE ENVIO 1"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["TRABALHO"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')
       
    def EnviarMensagens(self):
        time.sleep(20)
        self.driver.minimize_window()
        time.sleep(3)
        pyautogui.press('prtsc')
        time.sleep(3)
        pyautogui.press('tab', presses=4)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(5)
        self.driver.maximize_window()
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element("xpath",f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            #<div tabindex="-1" class="p3_M1">
            chat_box = self.driver.find_element("class name",'p3_M1')
            time.sleep(3)
            chat_box.click()
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(5)
            self.driver.minimize_window()
bot = WhatsappBot()
cont = 0
while cont < 24:
    bot.EnviarMensagens()
    time.sleep(3600)
    