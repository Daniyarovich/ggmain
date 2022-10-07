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
        insertvalue('USDT',80000,'BUY','TinkoffNew', "B74",a)
       
        insertvalue('BTC',80000,'BUY','TinkoffNew', "C74",a)
       
        insertvalue('BUSD',80000,'BUY','TinkoffNew', "D74",a)
        
        insertvalue('BNB',80000,'BUY','TinkoffNew', "E74",a)
        insertvalue('ETH',80000,'BUY','TinkoffNew', "F74",a)
        insertvalue('RUB',80000,'BUY','TinkoffNew', "G74",a)
        insertvalue('SHIB',80000,'BUY','TinkoffNew', "H74",a)
        matrix.append(a)
        
        
        insertvalue('USDT',80000,'BUY','RosBankNew', "B75",b)
        insertvalue('BTC',80000,'BUY','RosBankNew', "C75",b)
        insertvalue('BUSD',80000,'BUY','RosBankNew', "D75",b)
        insertvalue('BNB',80000,'BUY','RosBankNew', "E75",b)
        insertvalue('ETH',80000,'BUY','RosBankNew', "F75",b)
        insertvalue('RUB',80000,'BUY','RosBankNew', "G75",b)
        insertvalue('SHIB',80000,'BUY','RosBankNew', "H75",b)
        matrix.append(b)
         
        
        insertvalue('USDT',80000,'BUY','QIWI', "B76",c)
        insertvalue('BTC',80000,'BUY','QIWI', "C76",c)
        insertvalue('BUSD',80000,'BUY','QIWI', "D76",c)
        insertvalue('BNB',80000,'BUY','QIWI', "E76",c)
        insertvalue('ETH',80000,'BUY','QIWI', "F76",c)
        insertvalue('RUB',80000,'BUY','QIWI', "G76",c)
        insertvalue('SHIB',80000,'BUY','QIWI', "H76",c)
        matrix.append(c)
        insertvalue('USDT',80000,'BUY','YandexMoneyNew', "B77",d)
        insertvalue('BTC',80000,'BUY','YandexMoneyNew', "C77",d)
        insertvalue('BUSD',80000,'BUY','YandexMoneyNew', "D771",d)
        insertvalue('BNB',80000,'BUY','YandexMoneyNew', "E77",d)
        insertvalue('ETH',80000,'BUY','YandexMoneyNew', "F77",d)
        insertvalue('RUB',80000,'BUY','YandexMoneyNew', "G77",d)
        insertvalue('SHIB',80000,'BUY','YandexMoneyNew', "H77",d)
        matrix.append(d)
        insertvalue('USDT',80000,'BUY','RaiffeisenBank', "B78",e)
        insertvalue('BTC',80000,'BUY','RaiffeisenBank', "C78",e)
        insertvalue('BUSD',80000,'BUY','RaiffeisenBank', "D78",e)
        insertvalue('BNB',80000,'BUY','RaiffeisenBank', "E78",e)
        insertvalue('ETH',80000,'BUY','RaiffeisenBank', "F78",e)
        insertvalue('RUB',80000,'BUY','RaiffeisenBank', "G78",e)
        insertvalue('SHIB',80000,'BUY','RaiffeisenBank', "H78",e)
        matrix.append(e)
        
        insertvalue('USDT',80000,'BUY','PostBankNew', "B79",f)
        insertvalue('BTC',80000,'BUY','PostBankNew', "C79",f)
        insertvalue('BUSD',80000,'BUY','PostBankNew', "D79",f)
        insertvalue('BNB',80000,'BUY','PostBankNew', "E79",f)
        insertvalue('ETH',80000,'BUY','PostBankNew', "F79",f)
        insertvalue('RUB',80000,'BUY','PostBankNew', "G79",f)
        insertvalue('SHIB',80000,'BUY','PostBankNew', "H79",f)
        matrix.append(f)
        
        
        insertvalue('USDT',80000,'BUY','MTSBank', "B80",g)
        insertvalue('BTC',80000,'BUY','MTSBank', "C80",g)
        insertvalue('BUSD',80000,'BUY','MTSBank', "D80",g)
        insertvalue('BNB',80000,'BUY','MTSBank', "E80",g)
        insertvalue('ETH',80000,'BUY','MTSBank', "F80",g)
        insertvalue('RUB',80000,'BUY','MTSBank', "G80",g)
        insertvalue('SHIB',80000,'BUY','MTSBank', "H80",g)
        matrix.append(g)
        
        insertvalue('USDT',80000,'BUY','HomeCreditBank', "B81",r)
        insertvalue('BTC',80000,'BUY','HomeCreditBank', "C81",r)
        insertvalue('BUSD',80000,'BUY','HomeCreditBank', "D81",r)
        insertvalue('BNB',80000,'BUY','HomeCreditBank', "E81",r)
        insertvalue('ETH',80000,'BUY','HomeCreditBank', "F81",r)
        insertvalue('RUB',80000,'BUY','HomeCreditBank', "G81",r)
        insertvalue('SHIB',80000,'BUY','HomeCreditBank', "H81",r)
        matrix.append(r)
        insertvalue('USDT',80000,'BUY','ABank', "B82",n)
        insertvalue('BTC',80000,'BUY','ABank', "C82",n)
        insertvalue('BUSD',80000,'BUY','ABank', "D82",n)
        insertvalue('BNB',80000,'BUY','ABank', "E82",n)
        insertvalue('ETH',80000,'BUY','ABank', "F82",n)
        insertvalue('RUB',80000,'BUY','ABank', "G82",n)
        insertvalue('SHIB',80000,'BUY','ABank', "H82",n)
        matrix.append(n)
        insertvalue('USDT',80000,'BUY','RUBfiatbalance', "B83",q)
        insertvalue('BTC',80000,'BUY','RUBfiatbalance', "C83",q)
        insertvalue('BUSD',80000,'BUY','RUBfiatbalance', "D83",q)
        insertvalue('BNB',80000,'BUY','RUBfiatbalance', "E83",q)
        insertvalue('ETH',80000,'BUY','RUBfiatbalance', "F83",q)
        insertvalue('RUB',80000,'BUY','RUBfiatbalance', "G83",q)
        insertvalue('SHIB',80000,'BUY','RUBfiatbalance', "H83",q)
        matrix.append(q)
        
        insertvalue('USDT',80000,'BUY','Payeer', "B84",l)
        insertvalue('BTC',80000,'BUY','Payeer', "C84",l)
        insertvalue('BUSD',80000,'BUY','Payeer', "D84",l)
        insertvalue('BNB',80000,'BUY','Payeer', "E84",l)
        insertvalue('ETH',80000,'BUY','Payeer', "F84",l)
        insertvalue('RUB',80000,'BUY','Payeer', "G84",l)
        insertvalue('SHIB',80000,'BUY','Payeer', "H84",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',80000,'BUY','Advcash', "B85",h)
        insertvalue('BTC',80000,'BUY','Advcash', "C85",h)
        insertvalue('BUSD',80000,'BUY','Advcash', "D85",h)
        insertvalue('BNB',80000,'BUY','Advcash', "E85",h)
        insertvalue('ETH',80000,'BUY','Advcash', "F85",h)
        insertvalue('RUB',80000,'BUY','Advcash', "G85",h)
        insertvalue('SHIB',80000,'BUY','Advcash', "H85",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('B74:H85', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass