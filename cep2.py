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
        url = requests.get('http://www.viacep.com.br/ws/%s/json/' %(CEP))
        text = url.text
        #data = json.loads(text)
        data = json.dump(text,indent=4)
        print(data)       
    else:
        print('Digite somente os oito dígitos do CEP')

while True:
    CEP = input("CEP: ")
    busca_CEP(CEP)   
    
