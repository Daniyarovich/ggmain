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
        insertvalue('USDT',1000,'BUY','TinkoffNew', "B18",a)
       
        insertvalue('BTC',1000,'BUY','TinkoffNew', "C18",a)
       
        insertvalue('BUSD',1000,'BUY','TinkoffNew', "D18",a)
        
        insertvalue('BNB',1000,'BUY','TinkoffNew', "E18",a)
        insertvalue('ETH',1000,'BUY','TinkoffNew', "F18",a)
        insertvalue('RUB',1000,'BUY','TinkoffNew', "G18",a)
        insertvalue('SHIB',1000,'BUY','TinkoffNew', "H18",a)
        matrix.append(a)
        
        
        insertvalue('USDT',1000,'BUY','RosBankNew', "B19",b)
        insertvalue('BTC',1000,'BUY','RosBankNew', "C19",b)
        insertvalue('BUSD',1000,'BUY','RosBankNew', "D19",b)
        insertvalue('BNB',1000,'BUY','RosBankNew', "E19",b)
        insertvalue('ETH',1000,'BUY','RosBankNew', "F19",b)
        insertvalue('RUB',1000,'BUY','RosBankNew', "G19",b)
        insertvalue('SHIB',1000,'BUY','RosBankNew', "H19",b)
        matrix.append(b)
         
        
        insertvalue('USDT',1000,'BUY','QIWI', "B20",c)
        insertvalue('BTC',1000,'BUY','QIWI', "C20",c)
        insertvalue('BUSD',1000,'BUY','QIWI', "D20",c)
        insertvalue('BNB',1000,'BUY','QIWI', "E20",c)
        insertvalue('ETH',1000,'BUY','QIWI', "F20",c)
        insertvalue('RUB',1000,'BUY','QIWI', "G20",c)
        insertvalue('SHIB',1000,'BUY','QIWI', "H20",c)
        matrix.append(c)
        insertvalue('USDT',1000,'BUY','YandexMoneyNew', "B21",d)
        insertvalue('BTC',1000,'BUY','YandexMoneyNew', "C21",d)
        insertvalue('BUSD',1000,'BUY','YandexMoneyNew', "D21",d)
        insertvalue('BNB',1000,'BUY','YandexMoneyNew', "E21",d)
        insertvalue('ETH',1000,'BUY','YandexMoneyNew', "F21",d)
        insertvalue('RUB',1000,'BUY','YandexMoneyNew', "G21",d)
        insertvalue('SHIB',1000,'BUY','YandexMoneyNew', "H21",d)
        matrix.append(d)
        insertvalue('USDT',1000,'BUY','RaiffeisenBank', "B22",e)
        insertvalue('BTC',1000,'BUY','RaiffeisenBank', "C22",e)
        insertvalue('BUSD',1000,'BUY','RaiffeisenBank', "D22",e)
        insertvalue('BNB',1000,'BUY','RaiffeisenBank', "E22",e)
        insertvalue('ETH',1000,'BUY','RaiffeisenBank', "F22",e)
        insertvalue('RUB',1000,'BUY','RaiffeisenBank', "G22",e)
        insertvalue('SHIB',1000,'BUY','RaiffeisenBank', "H22",e)
        matrix.append(e)
        
        insertvalue('USDT',1000,'BUY','PostBankNew', "B23",f)
        insertvalue('BTC',1000,'BUY','PostBankNew', "C23",f)
        insertvalue('BUSD',1000,'BUY','PostBankNew', "D23",f)
        insertvalue('BNB',1000,'BUY','PostBankNew', "E23",f)
        insertvalue('ETH',1000,'BUY','PostBankNew', "F23",f)
        insertvalue('RUB',1000,'BUY','PostBankNew', "G23",f)
        insertvalue('SHIB',1000,'BUY','PostBankNew', "H23",f)
        matrix.append(f)
        
        
        insertvalue('USDT',1000,'BUY','MTSBank', "B24",g)
        insertvalue('BTC',1000,'BUY','MTSBank', "C24",g)
        insertvalue('BUSD',1000,'BUY','MTSBank', "D24",g)
        insertvalue('BNB',1000,'BUY','MTSBank', "E24",g)
        insertvalue('ETH',1000,'BUY','MTSBank', "F24",g)
        insertvalue('RUB',1000,'BUY','MTSBank', "G24",g)
        insertvalue('SHIB',1000,'BUY','MTSBank', "H24",g)
        matrix.append(g)
        
        insertvalue('USDT',1000,'BUY','HomeCreditBank', "B25",r)
        insertvalue('BTC',1000,'BUY','HomeCreditBank', "C25",r)
        insertvalue('BUSD',1000,'BUY','HomeCreditBank', "D25",r)
        insertvalue('BNB',1000,'BUY','HomeCreditBank', "E25",r)
        insertvalue('ETH',1000,'BUY','HomeCreditBank', "F25",r)
        insertvalue('RUB',1000,'BUY','HomeCreditBank', "G25",r)
        insertvalue('SHIB',1000,'BUY','HomeCreditBank', "H25",r)
        matrix.append(r)
        insertvalue('USDT',1000,'BUY','ABank', "B26",n)
        insertvalue('BTC',1000,'BUY','ABank', "C26",n)
        insertvalue('BUSD',1000,'BUY','ABank', "D26",n)
        insertvalue('BNB',1000,'BUY','ABank', "E26",n)
        insertvalue('ETH',1000,'BUY','ABank', "F26",n)
        insertvalue('RUB',1000,'BUY','ABank', "G26",n)
        insertvalue('SHIB',1000,'BUY','ABank', "H26",n)
        matrix.append(n)
        insertvalue('USDT',1000,'BUY','RUBfiatbalance', "B27",q)
        insertvalue('BTC',1000,'BUY','RUBfiatbalance', "C27",q)
        insertvalue('BUSD',1000,'BUY','RUBfiatbalance', "D27",q)
        insertvalue('BNB',1000,'BUY','RUBfiatbalance', "E27",q)
        insertvalue('ETH',1000,'BUY','RUBfiatbalance', "F27",q)
        insertvalue('RUB',1000,'BUY','RUBfiatbalance', "G27",q)
        insertvalue('SHIB',1000,'BUY','RUBfiatbalance', "H27",q)
        matrix.append(q)
        
        insertvalue('USDT',1000,'BUY','Payeer', "B28",l)
        insertvalue('BTC',1000,'BUY','Payeer', "C28",l)
        insertvalue('BUSD',1000,'BUY','Payeer', "D28",l)
        insertvalue('BNB',1000,'BUY','Payeer', "E28",l)
        insertvalue('ETH',1000,'BUY','Payeer', "F28",l)
        insertvalue('RUB',1000,'BUY','Payeer', "G28",l)
        insertvalue('SHIB',1000,'BUY','Payeer', "H28",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',1000,'BUY','Advcash', "B29",h)
        insertvalue('BTC',1000,'BUY','Advcash', "C29",h)
        insertvalue('BUSD',1000,'BUY','Advcash', "D29",h)
        insertvalue('BNB',1000,'BUY','Advcash', "E29",h)
        insertvalue('ETH',1000,'BUY','Advcash', "F29",h)
        insertvalue('RUB',1000,'BUY','Advcash', "G29",h)
        insertvalue('SHIB',1000,'BUY','Advcash', "H29",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B18:H29', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass