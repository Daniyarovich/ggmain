import pygsheets
import numpy as np
import requests
import sys 
import time
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('ТЗ на таблицу')
wks1 = sh.worksheet_by_title("Binance-TRY")
def newmain():
    a1= []
    a2= []
    a3= []
    a4= []
    a5= []
    a6= []
    a7= []
    a8= []
    a9= []
    a10= []
    a11= []
    a12= []
    a13= []
    a14= []
    a15= []
    a16= []
    a17= []
    a18= []
    a19= []
    

    
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
            "fiat":"TRY",
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
        insertvalue('USDT',10000,'BUY','Ziraat', "B~",a1)
        insertvalue('BTC',10000,'BUY','Ziraat', "C~",a1)
        insertvalue('BUSD',10000,'BUY','Ziraat', "D~",a1)
        insertvalue('BNB',10000,'BUY','Ziraat', "E~",a1)
        insertvalue('ETH',10000,'BUY','Ziraat', "F~",a1)
        insertvalue('DAI',10000,'BUY','Ziraat', "G~",a1)
        insertvalue('ADA',10000,'BUY','Ziraat', "H~",a1)
        insertvalue('SHIB',10000,'BUY','Ziraat', "H~",a1)
        insertvalue('DOGE',10000,'BUY','Ziraat', "H~",a1)
        insertvalue('TRX',10000,'BUY','Ziraat', "H~",a1)
        matrix.append(a1)
        
        insertvalue('USDT',10000,'BUY','BANK', "B~",a2)
        insertvalue('BTC',10000,'BUY','BANK', "C~",a2)
        insertvalue('BUSD',10000,'BUY','BANK', "D~",a2)
        insertvalue('BNB',10000,'BUY','BANK', "E~",a2)
        insertvalue('ETH',10000,'BUY','BANK', "F~",a2)
        insertvalue('DAI',10000,'BUY','BANK', "G~",a2)
        insertvalue('ADA',10000,'BUY','BANK', "H~",a2)
        insertvalue('SHIB',10000,'BUY','BANK', "H~",a2)
        insertvalue('DOGE',10000,'BUY','BANK', "H~",a2)
        insertvalue('TRX',10000,'BUY','BANK', "H~",a2)
        matrix.append(a2)
        
        
        insertvalue('USDT',10000,'BUY','Garanti', "B~",a3)
        insertvalue('BTC',10000,'BUY','Garanti', "C~",a3)
        insertvalue('BUSD',10000,'BUY','Garanti', "D~",a3)
        insertvalue('BNB',10000,'BUY','Garanti', "E~",a3)
        insertvalue('ETH',10000,'BUY','Garanti', "F~",a3)
        insertvalue('DAI',10000,'BUY','Garanti', "G~",a3)
        insertvalue('ADA',10000,'BUY','Garanti', "H~",a3)
        insertvalue('SHIB',10000,'BUY','Garanti', "H~",a3)
        insertvalue('DOGE',10000,'BUY','Garanti', "H~",a3)
        insertvalue('TRX',10000,'BUY','Garanti', "H~",a3)
        matrix.append(a3)
        insertvalue('USDT',10000,'BUY','KuveytTurk', "B~",a4)
        insertvalue('BTC',10000,'BUY','KuveytTurk', "C~",a4)
        insertvalue('BUSD',10000,'BUY','KuveytTurk', "D~",a4)
        insertvalue('BNB',10000,'BUY','KuveytTurk', "E~",a4)
        insertvalue('ETH',10000,'BUY','KuveytTurk', "F~",a4)
        insertvalue('DAI',10000,'BUY','KuveytTurk', "G~",a4)
        insertvalue('ADA',10000,'BUY','KuveytTurk', "H~",a4)
        insertvalue('SHIB',10000,'BUY','KuveytTurk', "H~",a4)
        insertvalue('DOGE',10000,'BUY','KuveytTurk', "H~",a4)
        insertvalue('TRX',10000,'BUY','KuveytTurk', "H~",a4)
        matrix.append(a4)
        insertvalue('USDT',10000,'BUY','DenizBank', "B~",a5)
        insertvalue('BTC',10000,'BUY','DenizBank', "C~",a5)
        insertvalue('BUSD',10000,'BUY','DenizBank', "D~",a5)
        insertvalue('BNB',10000,'BUY','DenizBank', "E~",a5)
        insertvalue('ETH',10000,'BUY','DenizBank', "F~",a5)
        insertvalue('DAI',10000,'BUY','DenizBank', "G~",a5)
        insertvalue('ADA',10000,'BUY','DenizBank', "H~",a5)
        insertvalue('SHIB',10000,'BUY','DenizBank', "H~",a5)
        insertvalue('DOGE',10000,'BUY','DenizBank', "H~",a5)
        insertvalue('TRX',10000,'BUY','DenizBank', "H~",a5)
        matrix.append(a5)
        insertvalue('USDT',10000,'BUY','BanktransferTurkey', "B~",a6)
        insertvalue('BTC',10000,'BUY','BanktransferTurkey', "C~",a6)
        insertvalue('BUSD',10000,'BUY','BanktransferTurkey', "D~",a6)
        insertvalue('BNB',10000,'BUY','BanktransferTurkey', "E~",a6)
        insertvalue('ETH',10000,'BUY','BanktransferTurkey', "F~",a6)
        insertvalue('DAI',10000,'BUY','BanktransferTurkey', "G~",a6)
        insertvalue('ADA',10000,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('SHIB',10000,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('DOGE',10000,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('TRX',10000,'BUY','BanktransferTurkey', "H~",a6)
        matrix.append(a6)
        insertvalue('USDT',10000,'BUY','Papara', "B~",a7)
        insertvalue('BTC',10000,'BUY','Papara', "C~",a7)
        insertvalue('BUSD',10000,'BUY','Papara', "D~",a7)
        insertvalue('BNB',10000,'BUY','Papara', "E~",a7)
        insertvalue('ETH',10000,'BUY','Papara', "F~",a7)
        insertvalue('DAI',10000,'BUY','Papara', "G~",a7)
        insertvalue('ADA',10000,'BUY','Papara', "H~",a7)
        insertvalue('SHIB',10000,'BUY','Papara', "H~",a7)
        insertvalue('DOGE',10000,'BUY','Papara', "H~",a7)
        insertvalue('TRX',10000,'BUY','Papara', "H~",a7)
        matrix.append(a7)
        insertvalue('USDT',10000,'BUY','VakifBank', "B~",a8)
        insertvalue('BTC',10000,'BUY','VakifBank', "C~",a8)
        insertvalue('BUSD',10000,'BUY','VakifBank', "D~",a8)
        insertvalue('BNB',10000,'BUY','VakifBank', "E~",a8)
        insertvalue('ETH',10000,'BUY','VakifBank', "F~",a8)
        insertvalue('DAI',10000,'BUY','VakifBank', "G~",a8)
        insertvalue('ADA',10000,'BUY','VakifBank', "H~",a8)
        insertvalue('SHIB',10000,'BUY','VakifBank', "H~",a8)
        insertvalue('DOGE',10000,'BUY','VakifBank', "H~",a8)
        insertvalue('TRX',10000,'BUY','VakifBank', "H~",a8)
        matrix.append(a8)
        insertvalue('USDT',10000,'BUY','ISBANK', "B~",a9)
        insertvalue('BTC',10000,'BUY','ISBANK', "C~",a9)
        insertvalue('BUSD',10000,'BUY','ISBANK', "D~",a9)
        insertvalue('BNB',10000,'BUY','ISBANK', "E~",a9)
        insertvalue('ETH',10000,'BUY','ISBANK', "F~",a9)
        insertvalue('DAI',10000,'BUY','ISBANK', "G~",a9)
        insertvalue('ADA',10000,'BUY','ISBANK', "H~",a9)
        insertvalue('SHIB',10000,'BUY','ISBANK', "H~",a9)
        insertvalue('DOGE',10000,'BUY','ISBANK', "H~",a9)
        insertvalue('TRX',10000,'BUY','ISBANK', "H~",a9)
        matrix.append(a9)
        insertvalue('USDT',10000,'BUY','QNB', "B~",a10)
        insertvalue('BTC',10000,'BUY','QNB', "C~",a10)
        insertvalue('BUSD',10000,'BUY','QNB', "D~",a10)
        insertvalue('BNB',10000,'BUY','QNB', "E~",a10)
        insertvalue('ETH',10000,'BUY','QNB', "F~",a10)
        insertvalue('DAI',10000,'BUY','QNB', "G~",a10)
        insertvalue('ADA',10000,'BUY','QNB', "H~",a10)
        insertvalue('SHIB',10000,'BUY','QNB', "H~",a10)
        insertvalue('DOGE',10000,'BUY','QNB', "H~",a10)
        insertvalue('TRX',10000,'BUY','QNB', "H~",a10)
        matrix.append(a10)
        insertvalue('USDT',10000,'BUY','Akbank', "B~",a11)
        insertvalue('BTC',10000,'BUY','Akbank', "C~",a11)
        insertvalue('BUSD',10000,'BUY','Akbank', "D~",a11)
        insertvalue('BNB',10000,'BUY','Akbank', "E~",a11)
        insertvalue('ETH',10000,'BUY','Akbank', "F~",a11)
        insertvalue('DAI',10000,'BUY','Akbank', "G~",a11)
        insertvalue('ADA',10000,'BUY','Akbank', "H~",a11)
        insertvalue('SHIB',10000,'BUY','Akbank', "H~",a11)
        insertvalue('DOGE',10000,'BUY','Akbank', "H~",a11)
        insertvalue('TRX',10000,'BUY','Akbank', "H~",a11)
        matrix.append(a11)
        insertvalue('USDT',10000,'BUY','KoronaPay', "B~",a12)
        insertvalue('BTC',10000,'BUY','KoronaPay', "C~",a12)
        insertvalue('BUSD',10000,'BUY','KoronaPay', "D~",a12)
        insertvalue('BNB',10000,'BUY','KoronaPay', "E~",a12)
        insertvalue('ETH',10000,'BUY','KoronaPay', "F~",a12)
        insertvalue('DAI',10000,'BUY','KoronaPay', "G~",a12)
        insertvalue('ADA',10000,'BUY','KoronaPay', "H~",a12)
        insertvalue('SHIB',10000,'BUY','KoronaPay', "H~",a12)
        insertvalue('DOGE',10000,'BUY','KoronaPay', "H~",a12)
        insertvalue('TRX',10000,'BUY','KoronaPay', "H~",a12)
        matrix.append(a12)
        insertvalue('USDT',10000,'BUY','Revolut', "B~",a13)
        insertvalue('BTC',10000,'BUY','Revolut', "C~",a13)
        insertvalue('BUSD',10000,'BUY','Revolut', "D~",a13)
        insertvalue('BNB',10000,'BUY','Revolut', "E~",a13)
        insertvalue('ETH',10000,'BUY','Revolut', "F~",a13)
        insertvalue('DAI',10000,'BUY','Revolut', "G~",a13)
        insertvalue('ADA',10000,'BUY','Revolut', "H~",a13)
        insertvalue('SHIB',10000,'BUY','Revolut', "H~",a13)
        insertvalue('DOGE',10000,'BUY','Revolut', "H~",a13)
        insertvalue('TRX',10000,'BUY','Revolut', "H~",a13)
        matrix.append(a13)
        insertvalue('USDT',10000,'BUY','BAKAIBANK', "B~",a14)
        insertvalue('BTC',10000,'BUY','BAKAIBANK', "C~",a14)
        insertvalue('BUSD',10000,'BUY','BAKAIBANK', "D~",a14)
        insertvalue('BNB',10000,'BUY','BAKAIBANK', "E~",a14)
        insertvalue('ETH',10000,'BUY','BAKAIBANK', "F~",a14)
        insertvalue('DAI',10000,'BUY','BAKAIBANK', "G~",a14)
        insertvalue('ADA',10000,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('SHIB',10000,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('DOGE',10000,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('TRX',10000,'BUY','BAKAIBANK', "H~",a14)
        matrix.append(a14)
        insertvalue('USDT',10000,'BUY','Fibabanka', "B~",a15)
        insertvalue('BTC',10000,'BUY','Fibabanka', "C~",a15)
        insertvalue('BUSD',10000,'BUY','Fibabanka', "D~",a15)
        insertvalue('BNB',10000,'BUY','Fibabanka', "E~",a15)
        insertvalue('ETH',10000,'BUY','Fibabanka', "F~",a15)
        insertvalue('DAI',10000,'BUY','Fibabanka', "G~",a15)
        insertvalue('ADA',10000,'BUY','Fibabanka', "H~",a15)
        insertvalue('SHIB',10000,'BUY','Fibabanka', "H~",a15)
        insertvalue('DOGE',10000,'BUY','Fibabanka', "H~",a15)
        insertvalue('TRX',10000,'BUY','Fibabanka', "H~",a15)
        matrix.append(a15)
        insertvalue('USDT',10000,'BUY','Paysend', "B~",a16)
        insertvalue('BTC',10000,'BUY','Paysend', "C~",a16)
        insertvalue('BUSD',10000,'BUY','Paysend', "D~",a16)
        insertvalue('BNB',10000,'BUY','Paysend', "E~",a16)
        insertvalue('ETH',10000,'BUY','Paysend', "F~",a16)
        insertvalue('DAI',10000,'BUY','Paysend', "G~",a16)
        insertvalue('ADA',10000,'BUY','Paysend', "H~",a16)
        insertvalue('SHIB',10000,'BUY','Paysend', "H~",a16)
        insertvalue('DOGE',10000,'BUY','Paysend', "H~",a16)
        insertvalue('TRX',10000,'BUY','Paysend', "H~",a16)
        matrix.append(a16)
        insertvalue('USDT',10000,'BUY','RUBfiatbalance', "B~",a17)
        insertvalue('BTC',10000,'BUY','RUBfiatbalance', "C~",a17)
        insertvalue('BUSD',10000,'BUY','RUBfiatbalance', "D~",a17)
        insertvalue('BNB',10000,'BUY','RUBfiatbalance', "E~",a17)
        insertvalue('ETH',10000,'BUY','RUBfiatbalance', "F~",a17)
        insertvalue('DAI',10000,'BUY','RUBfiatbalance', "G~",a17)
        insertvalue('ADA',10000,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('SHIB',10000,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('DOGE',10000,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('TRX',10000,'BUY','RUBfiatbalance', "H~",a17)
        matrix.append(a17)
        insertvalue('USDT',10000,'BUY','CashDeposit', "B~",a18)
        insertvalue('BTC',10000,'BUY','CashDeposit', "C~",a18)
        insertvalue('BUSD',10000,'BUY','CashDeposit', "D~",a18)
        insertvalue('BNB',10000,'BUY','CashDeposit', "E~",a18)
        insertvalue('ETH',10000,'BUY','CashDeposit', "F~",a18)
        insertvalue('DAI',10000,'BUY','CashDeposit', "G~",a18)
        insertvalue('ADA',10000,'BUY','CashDeposit', "H~",a18)
        insertvalue('SHIB',10000,'BUY','CashDeposit', "H~",a18)
        insertvalue('DOGE',10000,'BUY','CashDeposit', "H~",a18)
        insertvalue('TRX',10000,'BUY','CashDeposit', "H~",a18)
        matrix.append(a18)
        insertvalue('USDT',10000,'BUY','Wise', "B~",a19)
        insertvalue('BTC',10000,'BUY','Wise', "C~",a19)
        insertvalue('BUSD',10000,'BUY','Wise', "D~",a19)
        insertvalue('BNB',10000,'BUY','Wise', "E~",a19)
        insertvalue('ETH',10000,'BUY','Wise', "F~",a19)
        insertvalue('DAI',10000,'BUY','Wise', "G~",a19)
        insertvalue('ADA',10000,'BUY','Wise', "H~",a19)
        insertvalue('SHIB',10000,'BUY','Wise', "H~",a19)
        insertvalue('DOGE',10000,'BUY','Wise', "H~",a19)
        insertvalue('TRX',10000,'BUY','Wise', "H~",a19)
        matrix.append(a19)
       
        
        
        
        
        
        wks1.update_values('B64:K82', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass