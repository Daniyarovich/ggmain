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

    def BUYUAH():
        insertvalue('USDT',0,'BUY','TinkoffNew', "B4",a)
       
        insertvalue('BTC',0,'BUY','TinkoffNew', "C4",a)
       
        insertvalue('BUSD',0,'BUY','TinkoffNew', "D4",a)
        
        insertvalue('BNB',0,'BUY','TinkoffNew', "E4",a)
        insertvalue('ETH',0,'BUY','TinkoffNew', "F4",a)
        insertvalue('RUB',0,'BUY','TinkoffNew', "G4",a)
        insertvalue('SHIB',0,'BUY','TinkoffNew', "H4",a)
        matrix.append(a)
        
        
        insertvalue('USDT',0,'BUY','RosBankNew', "B5",b)
        insertvalue('BTC',0,'BUY','RosBankNew', "C5",b)
        insertvalue('BUSD',0,'BUY','RosBankNew', "D5",b)
        insertvalue('BNB',0,'BUY','RosBankNew', "E5",b)
        insertvalue('ETH',0,'BUY','RosBankNew', "F5",b)
        insertvalue('RUB',0,'BUY','RosBankNew', "G5",b)
        insertvalue('SHIB',0,'BUY','RosBankNew', "H5",b)
        matrix.append(b)
         
        
        insertvalue('USDT',0,'BUY','QIWI', "B6",c)
        insertvalue('BTC',0,'BUY','QIWI', "C6",c)
        insertvalue('BUSD',0,'BUY','QIWI', "D6",c)
        insertvalue('BNB',0,'BUY','QIWI', "E6",c)
        insertvalue('ETH',0,'BUY','QIWI', "F6",c)
        insertvalue('RUB',0,'BUY','QIWI', "G6",c)
        insertvalue('SHIB',0,'BUY','QIWI', "H6",c)
        matrix.append(c)
        insertvalue('USDT',0,'BUY','YandexMoneyNew', "B7",d)
        insertvalue('BTC',0,'BUY','YandexMoneyNew', "C7",d)
        insertvalue('BUSD',0,'BUY','YandexMoneyNew', "D7",d)
        insertvalue('BNB',0,'BUY','YandexMoneyNew', "E7",d)
        insertvalue('ETH',0,'BUY','YandexMoneyNew', "F7",d)
        insertvalue('RUB',0,'BUY','YandexMoneyNew', "G7",d)
        insertvalue('SHIB',0,'BUY','YandexMoneyNew', "H7",d)
        matrix.append(d)
        insertvalue('USDT',0,'BUY','RaiffeisenBank', "B8",e)
        insertvalue('BTC',0,'BUY','RaiffeisenBank', "C8",e)
        insertvalue('BUSD',0,'BUY','RaiffeisenBank', "D8",e)
        insertvalue('BNB',0,'BUY','RaiffeisenBank', "E8",e)
        insertvalue('ETH',0,'BUY','RaiffeisenBank', "F8",e)
        insertvalue('RUB',0,'BUY','RaiffeisenBank', "G8",e)
        insertvalue('SHIB',0,'BUY','RaiffeisenBank', "H8",e)
        matrix.append(e)
        
        insertvalue('USDT',0,'BUY','PostBankNew', "B9",f)
        insertvalue('BTC',0,'BUY','PostBankNew', "C9",f)
        insertvalue('BUSD',0,'BUY','PostBankNew', "D9",f)
        insertvalue('BNB',0,'BUY','PostBankNew', "E9",f)
        insertvalue('ETH',0,'BUY','PostBankNew', "F9",f)
        insertvalue('RUB',0,'BUY','PostBankNew', "G9",f)
        insertvalue('SHIB',0,'BUY','PostBankNew', "H9",f)
        matrix.append(f)
        
        
        insertvalue('USDT',0,'BUY','MTSBank', "B10",g)
        insertvalue('BTC',0,'BUY','MTSBank', "C10",g)
        insertvalue('BUSD',0,'BUY','MTSBank', "D10",g)
        insertvalue('BNB',0,'BUY','MTSBank', "E10",g)
        insertvalue('ETH',0,'BUY','MTSBank', "F10",g)
        insertvalue('RUB',0,'BUY','MTSBank', "G10",g)
        insertvalue('SHIB',0,'BUY','MTSBank', "H10",g)
        matrix.append(g)
        
        insertvalue('USDT',0,'BUY','HomeCreditBank', "B11",r)
        insertvalue('BTC',0,'BUY','HomeCreditBank', "C11",r)
        insertvalue('BUSD',0,'BUY','HomeCreditBank', "D11",r)
        insertvalue('BNB',0,'BUY','HomeCreditBank', "E11",r)
        insertvalue('ETH',0,'BUY','HomeCreditBank', "F11",r)
        insertvalue('RUB',0,'BUY','HomeCreditBank', "G11",r)
        insertvalue('SHIB',0,'BUY','HomeCreditBank', "H11",r)
        matrix.append(r)
        insertvalue('USDT',0,'BUY','ABank', "B12",n)
        insertvalue('BTC',0,'BUY','ABank', "C12",n)
        insertvalue('BUSD',0,'BUY','ABank', "D12",n)
        insertvalue('BNB',0,'BUY','ABank', "E12",n)
        insertvalue('ETH',0,'BUY','ABank', "F12",n)
        insertvalue('RUB',0,'BUY','ABank', "G12",n)
        insertvalue('SHIB',0,'BUY','ABank', "H12",n)
        matrix.append(n)
        insertvalue('USDT',0,'BUY','RUBfiatbalance', "B13",q)
        insertvalue('BTC',0,'BUY','RUBfiatbalance', "C13",q)
        insertvalue('BUSD',0,'BUY','RUBfiatbalance', "D13",q)
        insertvalue('BNB',0,'BUY','RUBfiatbalance', "E13",q)
        insertvalue('ETH',0,'BUY','RUBfiatbalance', "F13",q)
        insertvalue('RUB',0,'BUY','RUBfiatbalance', "G13",q)
        insertvalue('SHIB',0,'BUY','RUBfiatbalance', "H13",q)
        matrix.append(q)
        
        insertvalue('USDT',0,'BUY','Payeer', "B14",l)
        insertvalue('BTC',0,'BUY','Payeer', "C14",l)
        insertvalue('BUSD',0,'BUY','Payeer', "D14",l)
        insertvalue('BNB',0,'BUY','Payeer', "E14",l)
        insertvalue('ETH',0,'BUY','Payeer', "F14",l)
        insertvalue('RUB',0,'BUY','Payeer', "G14",l)
        insertvalue('SHIB',0,'BUY','Payeer', "H14",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',0,'BUY','Advcash', "B15",h)
        insertvalue('BTC',0,'BUY','Advcash', "C15",h)
        insertvalue('BUSD',0,'BUY','Advcash', "D15",h)
        insertvalue('BNB',0,'BUY','Advcash', "E15",h)
        insertvalue('ETH',0,'BUY','Advcash', "F15",h)
        insertvalue('RUB',0,'BUY','Advcash', "G15",h)
        insertvalue('SHIB',0,'BUY','Advcash', "H15",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B4:H15', matrix ) 
        
        


         


    BUYUAH()
while True:
    newmain()
    time.sleep(200)
    pass