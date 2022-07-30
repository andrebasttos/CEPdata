from curses.ascii import isdigit
import webbrowser
import json
import requests

def valida_CEP(CEP):
    if CEP.isdigit() and len(CEP) == 8:
        return True
    else:
        return False

def data_CEP(CEP):
    if valida_CEP(CEP):
        #webbrowser.open('http://www.viacep.com.br/ws/%s/json/' %(CEP))
        data_JSON = requests.get("http://www.viacep.com.br/ws/%s/json/" %(CEP))
        data_dic = data_JSON.text
        print(type(data_dic))        
    else:
        print('Digite somente os oito dígitos do CEP')

    
    CEP = input("CEP: ")
    data_CEP(CEP)
