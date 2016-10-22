from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Mapping import NavegacaoMap
import os


print(os.getcwd() + 'chromedriver.exe')
browser = webdriver.Chrome(os.getcwd() + '\chromedriver.exe') 
proc = NavegacaoMap(browser)
proc.Logar('email','senha', 'url_email')
proc.EncaminharEmails('email_encaminhar')
proc.ExcluirEmails()
proc.Encerrar()