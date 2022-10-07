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
        insertvalue('USDT',100000,'BUY','TinkoffNew', "B88",a)
       
        insertvalue('BTC',100000,'BUY','TinkoffNew', "C88",a)
       
        insertvalue('BUSD',100000,'BUY','TinkoffNew', "D88",a)
        
        insertvalue('BNB',100000,'BUY','TinkoffNew', "E88",a)
        insertvalue('ETH',100000,'BUY','TinkoffNew', "F88",a)
        insertvalue('RUB',100000,'BUY','TinkoffNew', "G88",a)
        insertvalue('SHIB',100000,'BUY','TinkoffNew', "H88",a)
        matrix.append(a)
        
        
        insertvalue('USDT',100000,'BUY','RosBankNew', "B89",b)
        insertvalue('BTC',100000,'BUY','RosBankNew', "C89",b)
        insertvalue('BUSD',100000,'BUY','RosBankNew', "D89",b)
        insertvalue('BNB',100000,'BUY','RosBankNew', "E89",b)
        insertvalue('ETH',100000,'BUY','RosBankNew', "F89",b)
        insertvalue('RUB',100000,'BUY','RosBankNew', "G89",b)
        insertvalue('SHIB',100000,'BUY','RosBankNew', "H89",b)
        matrix.append(b)
         
        
        insertvalue('USDT',100000,'BUY','QIWI', "B90",c)
        insertvalue('BTC',100000,'BUY','QIWI', "C90",c)
        insertvalue('BUSD',100000,'BUY','QIWI', "D90",c)
        insertvalue('BNB',100000,'BUY','QIWI', "E90",c)
        insertvalue('ETH',100000,'BUY','QIWI', "F90",c)
        insertvalue('RUB',100000,'BUY','QIWI', "G90",c)
        insertvalue('SHIB',100000,'BUY','QIWI', "H90",c)
        matrix.append(c)
        insertvalue('USDT',100000,'BUY','YandexMoneyNew', "B91",d)
        insertvalue('BTC',100000,'BUY','YandexMoneyNew', "C91",d)
        insertvalue('BUSD',100000,'BUY','YandexMoneyNew', "D911",d)
        insertvalue('BNB',100000,'BUY','YandexMoneyNew', "E91",d)
        insertvalue('ETH',100000,'BUY','YandexMoneyNew', "F91",d)
        insertvalue('RUB',100000,'BUY','YandexMoneyNew', "G91",d)
        insertvalue('SHIB',100000,'BUY','YandexMoneyNew', "H91",d)
        matrix.append(d)
        insertvalue('USDT',100000,'BUY','RaiffeisenBank', "B92",e)
        insertvalue('BTC',100000,'BUY','RaiffeisenBank', "C92",e)
        insertvalue('BUSD',100000,'BUY','RaiffeisenBank', "D92",e)
        insertvalue('BNB',100000,'BUY','RaiffeisenBank', "E92",e)
        insertvalue('ETH',100000,'BUY','RaiffeisenBank', "F92",e)
        insertvalue('RUB',100000,'BUY','RaiffeisenBank', "G92",e)
        insertvalue('SHIB',100000,'BUY','RaiffeisenBank', "H92",e)
        matrix.append(e)
        
        insertvalue('USDT',100000,'BUY','PostBankNew', "B93",f)
        insertvalue('BTC',100000,'BUY','PostBankNew', "C93",f)
        insertvalue('BUSD',100000,'BUY','PostBankNew', "D93",f)
        insertvalue('BNB',100000,'BUY','PostBankNew', "E93",f)
        insertvalue('ETH',100000,'BUY','PostBankNew', "F93",f)
        insertvalue('RUB',100000,'BUY','PostBankNew', "G93",f)
        insertvalue('SHIB',100000,'BUY','PostBankNew', "H93",f)
        matrix.append(f)
        
        
        insertvalue('USDT',100000,'BUY','MTSBank', "B94",g)
        insertvalue('BTC',100000,'BUY','MTSBank', "C94",g)
        insertvalue('BUSD',100000,'BUY','MTSBank', "D94",g)
        insertvalue('BNB',100000,'BUY','MTSBank', "E94",g)
        insertvalue('ETH',100000,'BUY','MTSBank', "F94",g)
        insertvalue('RUB',100000,'BUY','MTSBank', "G94",g)
        insertvalue('SHIB',100000,'BUY','MTSBank', "H94",g)
        matrix.append(g)
        
        insertvalue('USDT',100000,'BUY','HomeCreditBank', "B95",r)
        insertvalue('BTC',100000,'BUY','HomeCreditBank', "C95",r)
        insertvalue('BUSD',100000,'BUY','HomeCreditBank', "D95",r)
        insertvalue('BNB',100000,'BUY','HomeCreditBank', "E95",r)
        insertvalue('ETH',100000,'BUY','HomeCreditBank', "F95",r)
        insertvalue('RUB',100000,'BUY','HomeCreditBank', "G95",r)
        insertvalue('SHIB',100000,'BUY','HomeCreditBank', "H95",r)
        matrix.append(r)
        insertvalue('USDT',100000,'BUY','ABank', "B96",n)
        insertvalue('BTC',100000,'BUY','ABank', "C96",n)
        insertvalue('BUSD',100000,'BUY','ABank', "D96",n)
        insertvalue('BNB',100000,'BUY','ABank', "E96",n)
        insertvalue('ETH',100000,'BUY','ABank', "F96",n)
        insertvalue('RUB',100000,'BUY','ABank', "G96",n)
        insertvalue('SHIB',100000,'BUY','ABank', "H96",n)
        matrix.append(n)
        insertvalue('USDT',100000,'BUY','RUBfiatbalance', "B97",q)
        insertvalue('BTC',100000,'BUY','RUBfiatbalance', "C97",q)
        insertvalue('BUSD',100000,'BUY','RUBfiatbalance', "D97",q)
        insertvalue('BNB',100000,'BUY','RUBfiatbalance', "E97",q)
        insertvalue('ETH',100000,'BUY','RUBfiatbalance', "F97",q)
        insertvalue('RUB',100000,'BUY','RUBfiatbalance', "G97",q)
        insertvalue('SHIB',100000,'BUY','RUBfiatbalance', "H97",q)
        matrix.append(q)
        
        insertvalue('USDT',100000,'BUY','Payeer', "B98",l)
        insertvalue('BTC',100000,'BUY','Payeer', "C98",l)
        insertvalue('BUSD',100000,'BUY','Payeer', "D98",l)
        insertvalue('BNB',100000,'BUY','Payeer', "E98",l)
        insertvalue('ETH',100000,'BUY','Payeer', "F98",l)
        insertvalue('RUB',100000,'BUY','Payeer', "G98",l)
        insertvalue('SHIB',100000,'BUY','Payeer', "H98",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',100000,'BUY','Advcash', "B99",h)
        insertvalue('BTC',100000,'BUY','Advcash', "C99",h)
        insertvalue('BUSD',100000,'BUY','Advcash', "D99",h)
        insertvalue('BNB',100000,'BUY','Advcash', "E99",h)
        insertvalue('ETH',100000,'BUY','Advcash', "F99",h)
        insertvalue('RUB',100000,'BUY','Advcash', "G99",h)
        insertvalue('SHIB',100000,'BUY','Advcash', "H99",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B88:H99', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass