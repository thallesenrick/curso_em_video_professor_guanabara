import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site PUDIM nao está acessivel no momento')
else:
    print('\033[33mConsegui acessar o site PUDIM com sucesso!')
    print(site.read())