from django.shortcuts import render
from django.http import HttpResponseRedirect
from xmlrpc.client import ServerProxy
import time
import json
def home_page(request):
    if request.method == "GET":
        return render(request, "home.html", context={})
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponseRedirect('/bancaweb-a/'+ username +'/')

def banca(request, username):
    context = {}
   #data = request_read_file(username)
    context['user'] = username
    #context['bankA'] = data['bankA']
    #context['bankB'] = data['bankB']
    #context['bankC'] = data['bankC']
    if request.method == "GET":
        return render(request, "banca.html", context)
    elif request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'transfer':
            user2 = request.POST.get('user2')
            account = request.POST.get('account')
            account2 = request.POST.get('account2')
            bank = request.POST.get('bank')
            bank2 = request.POST.get('bank1')
            mount = request.POST.get('mount')
            #request_transfer(username, account, bank, user2, account2, bank2, mount)
        return HttpResponseRedirect('/bancaweb1/'+ username +'/')
'''
def request_transfer(username, account, bank, user2, account2, bank2, mount):
    point = [
        {'ip':'192.168.1.3', 'path': '/home/bank1/share1/'}, 
        {'ip':'192.168.1.5', 'path': '/home/bank1/mnt/bank2/'},
        {'ip':'192.168.1.7', 'path': '/home/bank1/mnt/bank3/'}
        ]
    client = ServerProxy(point[0]['ip']+':20064', allow_none=True)
    data = update_data_transfer(client, point, username, account, bank, user2, account2, bank2, mount)
    
def update_data_transfer(client, point, username, account, bank, user2, account2, bank2, mount):
    nro = client.request_bank()
    while True:
        nro_get = client.get()
        if nro == nro_get:
            path_file_bank = point[bank]['path']+''+username+'.json'
            path_file_bank2 = point[bank2]['path']+''+user2+'.json'
            file = open(path_file_bank)
            file2 = open(path_file_bank2)
            file_json = json.loads(file)
            file_json2 = json.loads(file2)
            for obj in file_json:
                if obj['nro'] == account:
                    obj['mount'] = obj['mount'] - mount
            for obj in file_json2:
                if obj['nro'] == account2:       
                    obj['mount'] = obj['mount'] + mount
            json.dump(file_json, file, indent=2)
            json.dump(file_json2, file2, indent=2)
            file.close()
            file.close()
            rpta = client.relase(nro)
            if rpta == 0:
                break


def request_read_file(username):
    point = [
        {'ip':'192.168.1.3', 'path': '/home/bank1/share1/'}, 
        {'ip':'192.168.1.5', 'path': '/home/bank1/mnt/bank2/'},
        {'ip':'192.168.1.7', 'path': '/home/bank1/mnt/bank3/'}
        ]
    client = ServerProxy(point[0]['ip']+':20064', allow_none=True)
    data = read_data(client, username, point)
    return data

def read_data(client, username, point):
    nro = client.request_bank()
    data = {'bankA': [], 'bankB': [], 'bankC': []}
    while True:
        nro_get = client.get()
        if nro == nro_get:
            path_file_bank = point[0]['path']+''+username+'.json'
            try:
                file = open(path_file_bank)
                file_json = json.loads(file)
                data['bankA'] = file_json
                file.close()
            except FileNotFoundError:
                print('Error: Not Found')
            
            path_file_bank = point[1]['path']+''+username+'.json'
            try:
                file = open(path_file_bank)
                file_json = json.loads(file)
                data['bankB'] = file_json
                file.close()
            except FileNotFoundError:
                print('Error: Not Found')
                
            path_file_bank = point[2]['path']+''+username+'.json'
            try:
                file = open(path_file_bank)
                file_json = json.loads(file)
                data['bankC'] = file_json
                file.close()
            except FileNotFoundError:
                print('Error: Not Found')
             
            rpta = client.relase(nro)
            if rpta == 0:
                break
    return data
'''
