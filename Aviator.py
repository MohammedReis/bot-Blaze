from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telebot
import time
import bd


# Por informações do seu bot.########
api_key = "5823779503:AAEBFeiPWNX1HWquW07zcIETB70uuSJSfmM"  # TOKEN DO SEU BOT
chat_id = '-1001797642890'  # ID DO CANAL
#####################################
bot = telebot.TeleBot(token=api_key)
analise_open = False
max_gale = 1
entrada_atual = 0
wins = 0
losss = 0
G1 = 0
Sg = 0
Estrategia = 0
meta_ganho = 0
lista = []

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)
bot.send_message(chat_id, text=f'''🤖 Olá, o robô está ativo 🤖 ''')
nav.get('https://blaze.com/pt/games/aviator')
check_crash = []
results_crash = []


def reset():
    global analise_open
    global entrada_atual
    analise_open = False
    entrada_atual = 0
    return


def win(results_crash):
    global wins
    global G1
    global Sg
    wins += 1
    Sg = wins - G1
    bot.send_message(chat_id, text=f'''
✅✅✅  WIN  ✅✅✅

WINS {wins} ✅ e LOSS {losss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  

results_crash{results_crash}
        ''')
    return


def loss():
    global G1
    G1 -= 1
    bot.send_message(chat_id, text=f'''
❌❌❌  LOSS  ❌❌❌

WINS {wins} ✅ e LOSS {losss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  

        ''')
    return


def martingale():
    global entrada_atual
    global max_gale
    global G1
    global Sg
    global losss
    global Estrategia
    entrada_atual += 1
    if entrada_atual <= max_gale:
        bot.send_message(chat_id, text=f'''
🐔 Vamos para o gale: {entrada_atual} 🐔
    ''')
        G1 += 1

    else:

        losss += 1
        reset()
        loss()
    return


def send_sinal(color, E):
    bot.send_message(chat_id, text=f'''
    
⚠️ Entrada Confirmada ⚠️
    🏃🏽 SAIR EM {color}X 🏃🏽
    🐔 REALIZAR 1 GALE 🐔
    👨🏽‍💻 Estrategia = {E} 👨🏽‍💻

    ''')
    print('Mandei o sinal')
    return


def send_resulto(results_crash, sinal,estrategia):
    global losss
    if results_crash[0] >= float(sinal):
        reset()
        win(results_crash[0])
    elif estrategia =='7':
        losss += 1
        reset()
        loss()
    else:
        martingale()


while True:
    try:
        time.sleep(60)
        iframe = nav.find_element(By.XPATH,"//*[@id='game_wrapper']/iframe")
        nav.switch_to.frame(iframe)
        time.sleep(10)
    except NameError as erro:
        continue
    except Exception as erro:
        continue
    if iframe != 'Girando...':
        bd.analisar_open = 1
        time.sleep(30)
        while True:    
            bd.resultsCrash.clear()
            go = nav.find_element(By.XPATH,"//div[@class='payouts-wrapper']").text
            lista = go.split('\n')
            for i in lista:
                bd.resultsCrash.append(i)
            if bd.analisar_open == 1:
                default = bd.resultsCrash[0:14]
                results_crash = []
                for x in default:
                    item = x
                    item = float(item.replace('x', ""))
                    results_crash.append(item)

            if results_crash != check_crash:

                check_crash = results_crash
                print(results_crash)
                if analise_open == True:
                    send_resulto(results_crash, meta_ganho,Estrategia)
                else:
                    print('verificando as estrategias')
                    if results_crash[0] < 1.2 and results_crash[1] <= 1.4 and results_crash[2] <= 1.5:
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '1'
                        send_sinal(meta_ganho, Estrategia)
                        
                    elif results_crash[0] <= 1.3 and results_crash[1] < 1.5 and results_crash[2] < 2.0 and results_crash[3] < 2.0:
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '2'
                        send_sinal(meta_ganho, Estrategia)
                    elif results_crash[0] < 1.3 and results_crash[1] < 1.7 and results_crash[2] < 1.7 and results_crash[3] < 2.0 and results_crash[4] < 2.0:
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '3'
                        send_sinal(meta_ganho, Estrategia)
                    elif results_crash[0] < 1.55 and results_crash[1] < 1.7 and results_crash[2] < 1.7 and results_crash[3] < 2.0 and results_crash[4] > 2.0:
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '4'
                        send_sinal(meta_ganho, Estrategia)
                    elif results_crash[0] < 2.0 and results_crash[1] < 2.0 and results_crash[2] > 2.0 and results_crash[3] < 2.0 and results_crash[4] > 2.0 :
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '5'
                        send_sinal(meta_ganho, Estrategia)
                    elif results_crash[0] < 1.5 and results_crash[1] < 1.5 and results_crash[2] < 1.5 and results_crash[3] < 1.5 and results_crash[4] < 1.5:
                        meta_ganho = 1.5
                        analise_open = True
                        Estrategia = '6'
                        send_sinal(meta_ganho, Estrategia)
                    elif results_crash[0] <= 1.0 and results_crash[1] > 2 :
                        meta_ganho = 3
                        analise_open = True
                        Estrategia = '7'
                        send_sinal(meta_ganho, Estrategia)
