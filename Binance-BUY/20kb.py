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
        insertvalue('USDT',20000,'BUY','TinkoffNew', "B46",a)
       
        insertvalue('BTC',20000,'BUY','TinkoffNew', "C46",a)
       
        insertvalue('BUSD',20000,'BUY','TinkoffNew', "D46",a)
        
        insertvalue('BNB',20000,'BUY','TinkoffNew', "E46",a)
        insertvalue('ETH',20000,'BUY','TinkoffNew', "F46",a)
        insertvalue('RUB',20000,'BUY','TinkoffNew', "G46",a)
        insertvalue('SHIB',20000,'BUY','TinkoffNew', "H46",a)
        matrix.append(a)
        
        
        insertvalue('USDT',20000,'BUY','RosBankNew', "B47",b)
        insertvalue('BTC',20000,'BUY','RosBankNew', "C47",b)
        insertvalue('BUSD',20000,'BUY','RosBankNew', "D47",b)
        insertvalue('BNB',20000,'BUY','RosBankNew', "E47",b)
        insertvalue('ETH',20000,'BUY','RosBankNew', "F47",b)
        insertvalue('RUB',20000,'BUY','RosBankNew', "G47",b)
        insertvalue('SHIB',20000,'BUY','RosBankNew', "H47",b)
        matrix.append(b)
         
        
        insertvalue('USDT',20000,'BUY','QIWI', "B48",c)
        insertvalue('BTC',20000,'BUY','QIWI', "C48",c)
        insertvalue('BUSD',20000,'BUY','QIWI', "D48",c)
        insertvalue('BNB',20000,'BUY','QIWI', "E48",c)
        insertvalue('ETH',20000,'BUY','QIWI', "F48",c)
        insertvalue('RUB',20000,'BUY','QIWI', "G48",c)
        insertvalue('SHIB',20000,'BUY','QIWI', "H48",c)
        matrix.append(c)
        insertvalue('USDT',20000,'BUY','YandexMoneyNew', "B49",d)
        insertvalue('BTC',20000,'BUY','YandexMoneyNew', "C49",d)
        insertvalue('BUSD',20000,'BUY','YandexMoneyNew', "D491",d)
        insertvalue('BNB',20000,'BUY','YandexMoneyNew', "E49",d)
        insertvalue('ETH',20000,'BUY','YandexMoneyNew', "F49",d)
        insertvalue('RUB',20000,'BUY','YandexMoneyNew', "G49",d)
        insertvalue('SHIB',20000,'BUY','YandexMoneyNew', "H49",d)
        matrix.append(d)
        insertvalue('USDT',20000,'BUY','RaiffeisenBank', "B50",e)
        insertvalue('BTC',20000,'BUY','RaiffeisenBank', "C50",e)
        insertvalue('BUSD',20000,'BUY','RaiffeisenBank', "D50",e)
        insertvalue('BNB',20000,'BUY','RaiffeisenBank', "E50",e)
        insertvalue('ETH',20000,'BUY','RaiffeisenBank', "F50",e)
        insertvalue('RUB',20000,'BUY','RaiffeisenBank', "G50",e)
        insertvalue('SHIB',20000,'BUY','RaiffeisenBank', "H50",e)
        matrix.append(e)
        
        insertvalue('USDT',20000,'BUY','PostBankNew', "B51",f)
        insertvalue('BTC',20000,'BUY','PostBankNew', "C51",f)
        insertvalue('BUSD',20000,'BUY','PostBankNew', "D51",f)
        insertvalue('BNB',20000,'BUY','PostBankNew', "E51",f)
        insertvalue('ETH',20000,'BUY','PostBankNew', "F51",f)
        insertvalue('RUB',20000,'BUY','PostBankNew', "G51",f)
        insertvalue('SHIB',20000,'BUY','PostBankNew', "H51",f)
        matrix.append(f)
        
        
        insertvalue('USDT',20000,'BUY','MTSBank', "B52",g)
        insertvalue('BTC',20000,'BUY','MTSBank', "C52",g)
        insertvalue('BUSD',20000,'BUY','MTSBank', "D52",g)
        insertvalue('BNB',20000,'BUY','MTSBank', "E52",g)
        insertvalue('ETH',20000,'BUY','MTSBank', "F52",g)
        insertvalue('RUB',20000,'BUY','MTSBank', "G52",g)
        insertvalue('SHIB',20000,'BUY','MTSBank', "H52",g)
        matrix.append(g)
        
        insertvalue('USDT',20000,'BUY','HomeCreditBank', "B53",r)
        insertvalue('BTC',20000,'BUY','HomeCreditBank', "C53",r)
        insertvalue('BUSD',20000,'BUY','HomeCreditBank', "D53",r)
        insertvalue('BNB',20000,'BUY','HomeCreditBank', "E53",r)
        insertvalue('ETH',20000,'BUY','HomeCreditBank', "F53",r)
        insertvalue('RUB',20000,'BUY','HomeCreditBank', "G53",r)
        insertvalue('SHIB',20000,'BUY','HomeCreditBank', "H53",r)
        matrix.append(r)
        insertvalue('USDT',20000,'BUY','ABank', "B54",n)
        insertvalue('BTC',20000,'BUY','ABank', "C54",n)
        insertvalue('BUSD',20000,'BUY','ABank', "D54",n)
        insertvalue('BNB',20000,'BUY','ABank', "E54",n)
        insertvalue('ETH',20000,'BUY','ABank', "F54",n)
        insertvalue('RUB',20000,'BUY','ABank', "G54",n)
        insertvalue('SHIB',20000,'BUY','ABank', "H54",n)
        matrix.append(n)
        insertvalue('USDT',20000,'BUY','RUBfiatbalance', "B55",q)
        insertvalue('BTC',20000,'BUY','RUBfiatbalance', "C55",q)
        insertvalue('BUSD',20000,'BUY','RUBfiatbalance', "D55",q)
        insertvalue('BNB',20000,'BUY','RUBfiatbalance', "E55",q)
        insertvalue('ETH',20000,'BUY','RUBfiatbalance', "F55",q)
        insertvalue('RUB',20000,'BUY','RUBfiatbalance', "G55",q)
        insertvalue('SHIB',20000,'BUY','RUBfiatbalance', "H55",q)
        matrix.append(q)
        
        insertvalue('USDT',20000,'BUY','Payeer', "B56",l)
        insertvalue('BTC',20000,'BUY','Payeer', "C56",l)
        insertvalue('BUSD',20000,'BUY','Payeer', "D56",l)
        insertvalue('BNB',20000,'BUY','Payeer', "E56",l)
        insertvalue('ETH',20000,'BUY','Payeer', "F56",l)
        insertvalue('RUB',20000,'BUY','Payeer', "G56",l)
        insertvalue('SHIB',20000,'BUY','Payeer', "H56",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',20000,'BUY','Advcash', "B57",h)
        insertvalue('BTC',20000,'BUY','Advcash', "C57",h)
        insertvalue('BUSD',20000,'BUY','Advcash', "D57",h)
        insertvalue('BNB',20000,'BUY','Advcash', "E57",h)
        insertvalue('ETH',20000,'BUY','Advcash', "F57",h)
        insertvalue('RUB',20000,'BUY','Advcash', "G57",h)
        insertvalue('SHIB',20000,'BUY','Advcash', "H57",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B46:H57', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass 