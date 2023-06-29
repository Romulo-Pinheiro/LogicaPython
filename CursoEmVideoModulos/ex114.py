import requests

try:
    pudim = requests.get('http://pudim.com.br')
    print('\033[1;32mCONSEGUI ACESSAR O SITE DO PUDIM COM SUCESSO!\033[m')
except:
    print('\033[1;31mO SITE DO PUDIM NÃO ESTÁ ACESSÍVEL NO MOMENTO :( \033[m')


