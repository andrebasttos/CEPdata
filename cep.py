from curses.ascii import isdigit
import webbrowser
import json
import requests

def valida_CEP(CEP):
    if CEP.isdigit() and len(CEP) == 8:
        return True
    else:
        return False

def busca_CEP(CEP):
    if valida_CEP(CEP):
        webbrowser.open('http://www.viacep.com.br/ws/%s/json/' %(CEP))
        #dados = requests.get('http://www.viacep.com.br/ws/%s/json/' %(CEP))
    else:
        print('Digite somente os oito dígitos do CEP')

    
while True:
    CEP = input("CEP: ")
    busca_CEP(CEP)

