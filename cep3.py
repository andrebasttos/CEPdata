import re
import requests

def prepare_cep(cep: str):
    _cep = re.findall('[0-9]+', cep)
    _cep = _cep and "".join(_cep)
    return _cep

def is_valid(cep):
    return bool(len(cep) == 8)

def call_viacep(cep):

    try:
        response = requests.get(f"http://www.viacep.com.br/ws/{cep}/json/", timeout=10)

        if not response.status_code == 200 or 'erro' in response.json():
            return {'error': 'Cep não encontrato'}
        return response.json()

    except Exception as e:
        return {'error': e} 

def handle_cep(cep: str) -> str:
    
    cep = prepare_cep(cep)

    if is_valid(cep):

        endereco = call_viacep(cep)
        if not 'error' in endereco:
            return endereco

        return endereco['error']

    return "Errouu!"


def main():
    continua = True
    while continua:
        print("""
            Digite um CEP válido ou X para sair
        """)

        cep = input(": ")
        if cep == 'x' or cep == 'X':
            # Poderia ser apenas um break
            continua = False
            continue

        response = handle_cep(cep)
        print('\n', response)


if "__main__" == __name__:
    main()
    
