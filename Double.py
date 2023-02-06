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
import telebot
import time
import bd
from datetime import datetime
from datetime import timedelta

# Por informações do seu bot.########
api_key = "5823779503:AAEBFeiPWNX1HWquW07zcIETB70uuSJSfmM"  # TOKEN DO SEU BOT
chat_id = '-1001808631930'  # ID DO CANAL
#####################################
bot = telebot.TeleBot(token=api_key)
win = 0
loss = 0
Sg = 0
G1 = 0
Br = 0
Acertividade = 0
Estrategia = ''
now_date = datetime.now()
futuro = datetime.now() + timedelta(hours=12)


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)
bot.send_message(chat_id, text=f'''🤖 Olá, o robô está ativo 🤖 ''')
nav.get('https://blaze.com/pt/games/double')


def qualnum(x):
    if x == '0':
        return 0

    if x == '1':
        return 1

    if x == '2':
        return 2

    if x == '3':
        return 3

    if x == '4':
        return 4

    if x == '5':
        return 5

    if x == '6':
        return 6

    if x == '7':
        return 7

    if x == '8':
        return 8

    if x == '9':
        return 9

    if x == '10':
        return 10

    if x == '11':
        return 11

    if x == '12':
        return 12

    if x == '13':
        return 13

    if x == '14':
        return 14


def qualcor(x):
    if x == '0':
        return 'B'

    if x == '1':
        return 'V'

    if x == '2':
        return 'V'

    if x == '3':
        return 'V'

    if x == '4':
        return 'V'

    if x == '5':
        return 'V'

    if x == '6':
        return 'V'

    if x == '7':
        return 'V'

    if x == '8':
        return 'P'

    if x == '9':
        return 'P'

    if x == '10':
        return 'P'

    if x == '11':
        return 'P'

    if x == '12':
        return 'P'

    if x == '13':
        return 'P'

    if x == '14':
        return 'P'


def reset():
    bd.estrategy_name = 'TRUE'
    bd.direction_color = 'NULL'
    bd.analisar = 0
    bd.gale_atual = 0


def martingales():
    def very_gale(num):
        global win
        global loss
        global Sg
        global G1
        global Br
        global Acertividade
        global Estrategia

        if num[0:1] == [0]:
            if bd.gale_atual == 0:
                win += 1
                Br += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUwdjJtHriZBU8Mq1YHVWZX3QhjXzawACuQMAAn4cwUQtQdOVzqh2GikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return
            if bd.gale_atual == 1:
                win += 1
                Br += 1
                G1 += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUwdjJtHriZBU8Mq1YHVWZX3QhjXzawACuQMAAn4cwUQtQdOVzqh2GikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                win += 1
                Sg += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUv9jJtG4HddqwFwzQGS8CmgYqkGwHAACjwIAAszPyUSvS8rr2dknKikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

            if bd.gale_atual == 1:
                win += 1
                G1 += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUv9jJtG4HddqwFwzQGS8CmgYqkGwHAACjwIAAszPyUSvS8rr2dknKikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                win += 1
                Sg += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUv9jJtG4HddqwFwzQGS8CmgYqkGwHAACjwIAAszPyUSvS8rr2dknKikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

            if bd.gale_atual == 1:
                win += 1
                G1 += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUv9jJtG4HddqwFwzQGS8CmgYqkGwHAACjwIAAszPyUSvS8rr2dknKikE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                bot.send_message(chat_id, text=f'''🐔 VAMOS PARA O GALE 1 🐔''')
                return

            if bd.gale_atual == 1:
                loss += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUwNjJtG6eonw1FyHeOebukQt91ra7gACvgIAAs8JwUQ0kYGUDoRZPSkE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                bot.send_message(chat_id, text=f'''🐔 VAMOS PARA O GALE 1 🐔''')
                return

            if bd.gale_atual == 1:
                loss += 1
                Acertividade = (win/(win+loss))*100
                bot.send_sticker(
                    chat_id, sticker='CAACAgEAAxkBAAEBUwNjJtG6eonw1FyHeOebukQt91ra7gACvgIAAs8JwUQ0kYGUDoRZPSkE')
                bot.send_message(chat_id, text=f'''
🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

''')
                reset()
                return

    very_gale(bd.finalnum)
    return


while futuro > now_date:
    now_date = datetime.now()
    try:
        resulROOL = nav.find_element(
            By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        continue
    except Exception as erro:
        continue

    if resulROOL == 'Girando...':
        bd.analisar_open = 1
        # print('Analisando')
        time.sleep(13)
        c = nav.page_source
        bd.resultsDouble.clear()

        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        print(soup)
        print(go)
        for i in go:
            if i.getText():
                bd.resultsDouble.append(i.getText())
            else:
                bd.resultsDouble.append('0')

        bd.resultsDouble = bd.resultsDouble[:-1]

        if bd.analisar_open == 1:

            default = bd.resultsDouble[0:14]

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            bd.finalnum = list(mapeando)
            bd.finalcor = list(mapeando2)
            print(default)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E1':
            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['V', 'V', 'P']:
                        bd.estrategy_name = 'E1'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        Estrategia = 'E1'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: ⬛️ 
Realizar 1 Gale.
Proteção no ◻️Branco.   
Estrategia: {Estrategia}            
                        ''')
                        return
                    if num[0:3] == ['P', 'P', 'V']:
                        bd.estrategy_name = 'E1'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        Estrategia = 'E1'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: 🟥 Vermelho
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}
                        ''')
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E2':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['P', 'V', 'P']:
                        bd.estrategy_name = 'E2'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        Estrategia = 'E2'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: ⬛️ 
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}            
                        ''')
                        return
                    if num[0:3] == ['V', 'P', 'V']:
                        bd.estrategy_name = 'E2'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        Estrategia = 'E2'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: 🟥 Vermelho
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}  
                        ''')
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E3':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:6] == ['V', 'V', 'V', 'V', 'V', 'P']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        Estrategia = 'E3'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: ⬛️ 
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}              
                        ''')
                        return
                    if num[0:6] == ['P', 'P', 'P', 'P', 'P', 'V']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        Estrategia = 'E3'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: 🟥 Vermelho
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}  
                        ''')
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E4':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:6] == ['V', 'V', 'V', 'V', 'V', 'P']:
                        bd.estrategy_name = 'E4'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        Estrategia = 'E4'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: ⬛️ 
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}             
                        ''')
                        return
                    if num[0:6] == ['P', 'P', 'P', 'P', 'P', 'V']:
                        bd.estrategy_name = 'E4'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        Estrategia = 'E4'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: 🟥 Vermelho
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}  
                        ''')
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E5':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:5] == ['P', 'V', 'V', 'V', 'V']:
                        bd.estrategy_name = 'E5'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        Estrategia = 'E5'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: 🟥 
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}              
                        ''')
                        return
                    if num[0:5] == ['V', 'P', 'P', 'P', 'P']:
                        bd.estrategy_name = 'E5'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        Estrategia = 'E5'
                        bot.send_message(chat_id=chat_id, text=f'''
⚠️ Entrada Confirmada ⚠️
Entrar no: ⬛️ Vermelho
Realizar 1 Gale.
Proteção no ◻️Branco.
Estrategia: {Estrategia}  
                        ''')
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion = CHECK_VERSION(bd.finalcor)
            print(checkVersion)

bot.send_message(chat_id=chat_id, text=f'''
🤖 FINALIZANDO POR HOJE COM OS SEGUINTES RESULTADOS 🤖

🏆  PLACAR  🏆

WINS {win} ✅ e LOSS {loss} ❌

SG: {Sg} 🤑
G1: {G1} 🐔  
BR: {Br} 💃🏼

Acertividade: {round(Acertividade, 2)}% 📈

                        ''')
