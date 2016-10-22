from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import json
import random
import time

class NavegacaoMap(object):

    def __init__(self, browser):
        self.browser = browser


    def Logar(self, usuario, senha, url_email):
        self.browser.get(url_email)

        txtEmail = self.browser.find_element_by_id('rcmloginuser')
        txtEmail.send_keys(usuario)

        txtSenha = self.browser.find_element_by_id('rcmloginpwd')
        txtSenha.send_keys(senha)
        try:
            btnEntrar = self.browser.find_element_by_class_name('mainaction')
            btnEntrar.click()
        except:
            print('ocorreu erro durante o login')

    def EncaminharEmails(self, email_encaminhar):
        time.sleep(5)
        emails_list = self.browser.find_elements_by_class_name('message')
        emails_enviar = len(emails_list)
        for i in range(0, emails_enviar):
            time.sleep(5)
            self.ChecaPopupMaldito()
            list_emails = self.browser.find_elements_by_class_name('message')
            email_item = list_emails[i]
            email_item.click()
            email_item.click()
            try:
                btnEncaminhar = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.ID, "rcmbtn110"))
                )
                self.ChecaPopupMaldito()
            except:
                print('Erro ao localizar btnEcaminhar')
                self.browser.quit()

            self.ChecaPopupMaldito()
            btnEncaminhar.click()
            try:
                txtEncaminhar = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.ID, "_to"))
                )
            except:
                print('Erro ao localizar txtEncaminhar')
                self.browser.quit()

            self.ChecaPopupMaldito()
            txtEncaminhar.send_keys(email_encaminhar)
            btn_enviar = self.browser.find_element_by_id('rcmbtn107')
            btn_enviar.click()

    def ExcluirEmails(self):
        time.sleep(5)
        emails_list = self.browser.find_elements_by_class_name('message')
        btn_excluir = self.browser.find_element_by_id('rcmbtn111')
        for email in emails_list:
            email.click()
            btn_excluir.click()

    def ChecaPopupMaldito(self):
        try:
            popup_maldito = WebDriverWait(self.browser, 2).until(
                EC.presence_of_element_located((By.ID, "cl0seCtx"))
            )
            popup_maldito.click()
        except:
            print('não apareceu o popup maldito')

    def Encerrar(self):
        self.browser.close()