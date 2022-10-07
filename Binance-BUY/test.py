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
        insertvalue('USDT',1000,'BUY','TinkoffNew', "B~",a)
       
        insertvalue('BTC',1000,'BUY','TinkoffNew', "C~",a)
       
        insertvalue('BUSD',1000,'BUY','TinkoffNew', "D~",a)
        
        insertvalue('BNB',1000,'BUY','TinkoffNew', "E~",a)
        insertvalue('ETH',1000,'BUY','TinkoffNew', "F~",a)
        insertvalue('RUB',1000,'BUY','TinkoffNew', "G~",a)
        insertvalue('SHIB',1000,'BUY','TinkoffNew', "H~",a)
        matrix.append(a)
        
        
        insertvalue('USDT',1000,'BUY','RosBankNew', "B!",b)
        insertvalue('BTC',1000,'BUY','RosBankNew', "C!",b)
        insertvalue('BUSD',1000,'BUY','RosBankNew', "D!",b)
        insertvalue('BNB',1000,'BUY','RosBankNew', "E!",b)
        insertvalue('ETH',1000,'BUY','RosBankNew', "F!",b)
        insertvalue('RUB',1000,'BUY','RosBankNew', "G!",b)
        insertvalue('SHIB',1000,'BUY','RosBankNew', "H!",b)
        matrix.append(b)
         
        
        insertvalue('USDT',1000,'BUY','QIWI', "B+",c)
        insertvalue('BTC',1000,'BUY','QIWI', "C+",c)
        insertvalue('BUSD',1000,'BUY','QIWI', "D+",c)
        insertvalue('BNB',1000,'BUY','QIWI', "E+",c)
        insertvalue('ETH',1000,'BUY','QIWI', "F+",c)
        insertvalue('RUB',1000,'BUY','QIWI', "G+",c)
        insertvalue('SHIB',1000,'BUY','QIWI', "H+",c)
        matrix.append(c)
        insertvalue('USDT',1000,'BUY','YandexMoneyNew', "B_",d)
        insertvalue('BTC',1000,'BUY','YandexMoneyNew', "C_",d)
        insertvalue('BUSD',1000,'BUY','YandexMoneyNew', "D_1",d)
        insertvalue('BNB',1000,'BUY','YandexMoneyNew', "E_",d)
        insertvalue('ETH',1000,'BUY','YandexMoneyNew', "F_",d)
        insertvalue('RUB',1000,'BUY','YandexMoneyNew', "G_",d)
        insertvalue('SHIB',1000,'BUY','YandexMoneyNew', "H_",d)
        matrix.append(d)
        insertvalue('USDT',1000,'BUY','RaiffeisenBank', "B\",e)
        insertvalue('BTC',1000,'BUY','RaiffeisenBank', "C\",e)
        insertvalue('BUSD',1000,'BUY','RaiffeisenBank', "D\",e)
        insertvalue('BNB',1000,'BUY','RaiffeisenBank', "E\",e)
        insertvalue('ETH',1000,'BUY','RaiffeisenBank', "F\",e)
        insertvalue('RUB',1000,'BUY','RaiffeisenBank', "G\",e)
        insertvalue('SHIB',1000,'BUY','RaiffeisenBank', "H\",e)
        matrix.append(e)
        
        insertvalue('USDT',1000,'BUY','PostBankNew', "B=",f)
        insertvalue('BTC',1000,'BUY','PostBankNew', "C=",f)
        insertvalue('BUSD',1000,'BUY','PostBankNew', "D=",f)
        insertvalue('BNB',1000,'BUY','PostBankNew', "E=",f)
        insertvalue('ETH',1000,'BUY','PostBankNew', "F=",f)
        insertvalue('RUB',1000,'BUY','PostBankNew', "G=",f)
        insertvalue('SHIB',1000,'BUY','PostBankNew', "H=",f)
        matrix.append(f)
        
        
        insertvalue('USDT',1000,'BUY','MTSBank', "B^",g)
        insertvalue('BTC',1000,'BUY','MTSBank', "C^",g)
        insertvalue('BUSD',1000,'BUY','MTSBank', "D^",g)
        insertvalue('BNB',1000,'BUY','MTSBank', "E^",g)
        insertvalue('ETH',1000,'BUY','MTSBank', "F^",g)
        insertvalue('RUB',1000,'BUY','MTSBank', "G^",g)
        insertvalue('SHIB',1000,'BUY','MTSBank', "H^",g)
        matrix.append(g)
        
        insertvalue('USDT',1000,'BUY','HomeCreditBank', "B|",r)
        insertvalue('BTC',1000,'BUY','HomeCreditBank', "C|",r)
        insertvalue('BUSD',1000,'BUY','HomeCreditBank', "D|",r)
        insertvalue('BNB',1000,'BUY','HomeCreditBank', "E|",r)
        insertvalue('ETH',1000,'BUY','HomeCreditBank', "F|",r)
        insertvalue('RUB',1000,'BUY','HomeCreditBank', "G|",r)
        insertvalue('SHIB',1000,'BUY','HomeCreditBank', "H|",r)
        matrix.append(r)
        insertvalue('USDT',1000,'BUY','ABank', "B@",n)
        insertvalue('BTC',1000,'BUY','ABank', "C@",n)
        insertvalue('BUSD',1000,'BUY','ABank', "D@",n)
        insertvalue('BNB',1000,'BUY','ABank', "E@",n)
        insertvalue('ETH',1000,'BUY','ABank', "F@",n)
        insertvalue('RUB',1000,'BUY','ABank', "G@",n)
        insertvalue('SHIB',1000,'BUY','ABank', "H@",n)
        matrix.append(n)
        insertvalue('USDT',1000,'BUY','RUBfiatbalance', "B#",q)
        insertvalue('BTC',1000,'BUY','RUBfiatbalance', "C#",q)
        insertvalue('BUSD',1000,'BUY','RUBfiatbalance', "D#",q)
        insertvalue('BNB',1000,'BUY','RUBfiatbalance', "E#",q)
        insertvalue('ETH',1000,'BUY','RUBfiatbalance', "F#",q)
        insertvalue('RUB',1000,'BUY','RUBfiatbalance', "G#",q)
        insertvalue('SHIB',1000,'BUY','RUBfiatbalance', "H#",q)
        matrix.append(q)
        
        insertvalue('USDT',1000,'BUY','Payeer', "B&",l)
        insertvalue('BTC',1000,'BUY','Payeer', "C&",l)
        insertvalue('BUSD',1000,'BUY','Payeer', "D&",l)
        insertvalue('BNB',1000,'BUY','Payeer', "E&",l)
        insertvalue('ETH',1000,'BUY','Payeer', "F&",l)
        insertvalue('RUB',1000,'BUY','Payeer', "G&",l)
        insertvalue('SHIB',1000,'BUY','Payeer', "H&",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',1000,'BUY','Advcash', "B*",h)
        insertvalue('BTC',1000,'BUY','Advcash', "C*",h)
        insertvalue('BUSD',1000,'BUY','Advcash', "D*",h)
        insertvalue('BNB',1000,'BUY','Advcash', "E*",h)
        insertvalue('ETH',1000,'BUY','Advcash', "F*",h)
        insertvalue('RUB',1000,'BUY','Advcash', "G*",h)
        insertvalue('SHIB',1000,'BUY','Advcash', "H*",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B18:H29', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(10)
    pass