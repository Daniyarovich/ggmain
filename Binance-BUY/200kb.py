import pygsheets
import numpy as np
import requests
import sys 
import time
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('ТЗ на таблицу')
wks1 = sh.worksheet_by_title("Binance-RUB")
def newmain():
    a= []
    b= []
    c= []
    d= []
    e= []
    f= []
    g= []
    r=[]
    n=[]
    q=[]
    l=[]
    h=[]
    
    # update the sheet with array
    matrix = [] 
    # share the sheet with your friend

    def insertvalue(asset, amount, tradetype, bank, row, sde):
        e = ''
        try:

            headers = {
            "Accept": "*/*",

            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com"
            }
            data = {
            "page": 1,
            "rows":1,
            "asset":asset,
            "tradeType":tradetype,
            "fiat":"RUB",
            "payTypes":[bank],
            "transAmount":amount
            }
            r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            sp = r.text
            allinfo = sp.split('"price"');
            someinfo = allinfo[1].split('"');
            line = someinfo[1].replace('.', ',')
            
            sde.append(line)
                 
        except:
            sde.append("Пусто")

    def SELLUAH():
        insertvalue('USDT',200000,'BUY','TinkoffNew', "B102",a)
       
        insertvalue('BTC',200000,'BUY','TinkoffNew', "C102",a)
       
        insertvalue('BUSD',200000,'BUY','TinkoffNew', "D102",a)
        
        insertvalue('BNB',200000,'BUY','TinkoffNew', "E102",a)
        insertvalue('ETH',200000,'BUY','TinkoffNew', "F102",a)
        insertvalue('RUB',200000,'BUY','TinkoffNew', "G102",a)
        insertvalue('SHIB',200000,'BUY','TinkoffNew', "H102",a)
        matrix.append(a)
        
        
        insertvalue('USDT',200000,'BUY','RosBankNew', "B103",b)
        insertvalue('BTC',200000,'BUY','RosBankNew', "C103",b)
        insertvalue('BUSD',200000,'BUY','RosBankNew', "D103",b)
        insertvalue('BNB',200000,'BUY','RosBankNew', "E103",b)
        insertvalue('ETH',200000,'BUY','RosBankNew', "F103",b)
        insertvalue('RUB',200000,'BUY','RosBankNew', "G103",b)
        insertvalue('SHIB',200000,'BUY','RosBankNew', "H103",b)
        matrix.append(b)
         
        
        insertvalue('USDT',200000,'BUY','QIWI', "B104",c)
        insertvalue('BTC',200000,'BUY','QIWI', "C104",c)
        insertvalue('BUSD',200000,'BUY','QIWI', "D104",c)
        insertvalue('BNB',200000,'BUY','QIWI', "E104",c)
        insertvalue('ETH',200000,'BUY','QIWI', "F104",c)
        insertvalue('RUB',200000,'BUY','QIWI', "G104",c)
        insertvalue('SHIB',200000,'BUY','QIWI', "H104",c)
        matrix.append(c)
        insertvalue('USDT',200000,'BUY','YandexMoneyNew', "B105",d)
        insertvalue('BTC',200000,'BUY','YandexMoneyNew', "C105",d)
        insertvalue('BUSD',200000,'BUY','YandexMoneyNew', "D1051",d)
        insertvalue('BNB',200000,'BUY','YandexMoneyNew', "E105",d)
        insertvalue('ETH',200000,'BUY','YandexMoneyNew', "F105",d)
        insertvalue('RUB',200000,'BUY','YandexMoneyNew', "G105",d)
        insertvalue('SHIB',200000,'BUY','YandexMoneyNew', "H105",d)
        matrix.append(d)
        insertvalue('USDT',200000,'BUY','RaiffeisenBank', "B106",e)
        insertvalue('BTC',200000,'BUY','RaiffeisenBank', "C106",e)
        insertvalue('BUSD',200000,'BUY','RaiffeisenBank', "D106",e)
        insertvalue('BNB',200000,'BUY','RaiffeisenBank', "E106",e)
        insertvalue('ETH',200000,'BUY','RaiffeisenBank', "F106",e)
        insertvalue('RUB',200000,'BUY','RaiffeisenBank', "G106",e)
        insertvalue('SHIB',200000,'BUY','RaiffeisenBank', "H106",e)
        matrix.append(e)
        
        insertvalue('USDT',200000,'BUY','PostBankNew', "B107",f)
        insertvalue('BTC',200000,'BUY','PostBankNew', "C107",f)
        insertvalue('BUSD',200000,'BUY','PostBankNew', "D107",f)
        insertvalue('BNB',200000,'BUY','PostBankNew', "E107",f)
        insertvalue('ETH',200000,'BUY','PostBankNew', "F107",f)
        insertvalue('RUB',200000,'BUY','PostBankNew', "G107",f)
        insertvalue('SHIB',200000,'BUY','PostBankNew', "H107",f)
        matrix.append(f)
        
        
        insertvalue('USDT',200000,'BUY','MTSBank', "B108",g)
        insertvalue('BTC',200000,'BUY','MTSBank', "C108",g)
        insertvalue('BUSD',200000,'BUY','MTSBank', "D108",g)
        insertvalue('BNB',200000,'BUY','MTSBank', "E108",g)
        insertvalue('ETH',200000,'BUY','MTSBank', "F108",g)
        insertvalue('RUB',200000,'BUY','MTSBank', "G108",g)
        insertvalue('SHIB',200000,'BUY','MTSBank', "H108",g)
        matrix.append(g)
        
        insertvalue('USDT',200000,'BUY','HomeCreditBank', "B109",r)
        insertvalue('BTC',200000,'BUY','HomeCreditBank', "C109",r)
        insertvalue('BUSD',200000,'BUY','HomeCreditBank', "D109",r)
        insertvalue('BNB',200000,'BUY','HomeCreditBank', "E109",r)
        insertvalue('ETH',200000,'BUY','HomeCreditBank', "F109",r)
        insertvalue('RUB',200000,'BUY','HomeCreditBank', "G109",r)
        insertvalue('SHIB',200000,'BUY','HomeCreditBank', "H109",r)
        matrix.append(r)
        insertvalue('USDT',200000,'BUY','ABank', "B110",n)
        insertvalue('BTC',200000,'BUY','ABank', "C110",n)
        insertvalue('BUSD',200000,'BUY','ABank', "D110",n)
        insertvalue('BNB',200000,'BUY','ABank', "E110",n)
        insertvalue('ETH',200000,'BUY','ABank', "F110",n)
        insertvalue('RUB',200000,'BUY','ABank', "G110",n)
        insertvalue('SHIB',200000,'BUY','ABank', "H110",n)
        matrix.append(n)
        insertvalue('USDT',200000,'BUY','RUBfiatbalance', "B111",q)
        insertvalue('BTC',200000,'BUY','RUBfiatbalance', "C111",q)
        insertvalue('BUSD',200000,'BUY','RUBfiatbalance', "D111",q)
        insertvalue('BNB',200000,'BUY','RUBfiatbalance', "E111",q)
        insertvalue('ETH',200000,'BUY','RUBfiatbalance', "F111",q)
        insertvalue('RUB',200000,'BUY','RUBfiatbalance', "G111",q)
        insertvalue('SHIB',200000,'BUY','RUBfiatbalance', "H111",q)
        matrix.append(q)
        
        insertvalue('USDT',200000,'BUY','Payeer', "B112",l)
        insertvalue('BTC',200000,'BUY','Payeer', "C112",l)
        insertvalue('BUSD',200000,'BUY','Payeer', "D112",l)
        insertvalue('BNB',200000,'BUY','Payeer', "E112",l)
        insertvalue('ETH',200000,'BUY','Payeer', "F112",l)
        insertvalue('RUB',200000,'BUY','Payeer', "G112",l)
        insertvalue('SHIB',200000,'BUY','Payeer', "H112",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',200000,'BUY','Advcash', "B113",h)
        insertvalue('BTC',200000,'BUY','Advcash', "C113",h)
        insertvalue('BUSD',200000,'BUY','Advcash', "D113",h)
        insertvalue('BNB',200000,'BUY','Advcash', "E113",h)
        insertvalue('ETH',200000,'BUY','Advcash', "F113",h)
        insertvalue('RUB',200000,'BUY','Advcash', "G113",h)
        insertvalue('SHIB',200000,'BUY','Advcash', "H113",h)
        matrix.append(h)
        
        
        
        
        wks1.update_values('B102:H113', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass