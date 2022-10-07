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
        insertvalue('USDT',30000,'SELL','Ziraat', "B~",a1)
        insertvalue('BTC',30000,'SELL','Ziraat', "C~",a1)
        insertvalue('BUSD',30000,'SELL','Ziraat', "D~",a1)
        insertvalue('BNB',30000,'SELL','Ziraat', "E~",a1)
        insertvalue('ETH',30000,'SELL','Ziraat', "F~",a1)
        insertvalue('DAI',30000,'SELL','Ziraat', "G~",a1)
        insertvalue('ADA',30000,'SELL','Ziraat', "H~",a1)
        insertvalue('SHIB',30000,'SELL','Ziraat', "H~",a1)
        insertvalue('DOGE',30000,'SELL','Ziraat', "H~",a1)
        insertvalue('TRX',30000,'SELL','Ziraat', "H~",a1)
        matrix.append(a1)
        
        insertvalue('USDT',30000,'SELL','BANK', "B~",a2)
        insertvalue('BTC',30000,'SELL','BANK', "C~",a2)
        insertvalue('BUSD',30000,'SELL','BANK', "D~",a2)
        insertvalue('BNB',30000,'SELL','BANK', "E~",a2)
        insertvalue('ETH',30000,'SELL','BANK', "F~",a2)
        insertvalue('DAI',30000,'SELL','BANK', "G~",a2)
        insertvalue('ADA',30000,'SELL','BANK', "H~",a2)
        insertvalue('SHIB',30000,'SELL','BANK', "H~",a2)
        insertvalue('DOGE',30000,'SELL','BANK', "H~",a2)
        insertvalue('TRX',30000,'SELL','BANK', "H~",a2)
        matrix.append(a2)
        
        
        insertvalue('USDT',30000,'SELL','Garanti', "B~",a3)
        insertvalue('BTC',30000,'SELL','Garanti', "C~",a3)
        insertvalue('BUSD',30000,'SELL','Garanti', "D~",a3)
        insertvalue('BNB',30000,'SELL','Garanti', "E~",a3)
        insertvalue('ETH',30000,'SELL','Garanti', "F~",a3)
        insertvalue('DAI',30000,'SELL','Garanti', "G~",a3)
        insertvalue('ADA',30000,'SELL','Garanti', "H~",a3)
        insertvalue('SHIB',30000,'SELL','Garanti', "H~",a3)
        insertvalue('DOGE',30000,'SELL','Garanti', "H~",a3)
        insertvalue('TRX',30000,'SELL','Garanti', "H~",a3)
        matrix.append(a3)
        insertvalue('USDT',30000,'SELL','KuveytTurk', "B~",a4)
        insertvalue('BTC',30000,'SELL','KuveytTurk', "C~",a4)
        insertvalue('BUSD',30000,'SELL','KuveytTurk', "D~",a4)
        insertvalue('BNB',30000,'SELL','KuveytTurk', "E~",a4)
        insertvalue('ETH',30000,'SELL','KuveytTurk', "F~",a4)
        insertvalue('DAI',30000,'SELL','KuveytTurk', "G~",a4)
        insertvalue('ADA',30000,'SELL','KuveytTurk', "H~",a4)
        insertvalue('SHIB',30000,'SELL','KuveytTurk', "H~",a4)
        insertvalue('DOGE',30000,'SELL','KuveytTurk', "H~",a4)
        insertvalue('TRX',30000,'SELL','KuveytTurk', "H~",a4)
        matrix.append(a4)
        insertvalue('USDT',30000,'SELL','DenizBank', "B~",a5)
        insertvalue('BTC',30000,'SELL','DenizBank', "C~",a5)
        insertvalue('BUSD',30000,'SELL','DenizBank', "D~",a5)
        insertvalue('BNB',30000,'SELL','DenizBank', "E~",a5)
        insertvalue('ETH',30000,'SELL','DenizBank', "F~",a5)
        insertvalue('DAI',30000,'SELL','DenizBank', "G~",a5)
        insertvalue('ADA',30000,'SELL','DenizBank', "H~",a5)
        insertvalue('SHIB',30000,'SELL','DenizBank', "H~",a5)
        insertvalue('DOGE',30000,'SELL','DenizBank', "H~",a5)
        insertvalue('TRX',30000,'SELL','DenizBank', "H~",a5)
        matrix.append(a5)
        insertvalue('USDT',30000,'SELL','BanktransferTurkey', "B~",a6)
        insertvalue('BTC',30000,'SELL','BanktransferTurkey', "C~",a6)
        insertvalue('BUSD',30000,'SELL','BanktransferTurkey', "D~",a6)
        insertvalue('BNB',30000,'SELL','BanktransferTurkey', "E~",a6)
        insertvalue('ETH',30000,'SELL','BanktransferTurkey', "F~",a6)
        insertvalue('DAI',30000,'SELL','BanktransferTurkey', "G~",a6)
        insertvalue('ADA',30000,'SELL','BanktransferTurkey', "H~",a6)
        insertvalue('SHIB',30000,'SELL','BanktransferTurkey', "H~",a6)
        insertvalue('DOGE',30000,'SELL','BanktransferTurkey', "H~",a6)
        insertvalue('TRX',30000,'SELL','BanktransferTurkey', "H~",a6)
        matrix.append(a6)
        insertvalue('USDT',30000,'SELL','Papara', "B~",a7)
        insertvalue('BTC',30000,'SELL','Papara', "C~",a7)
        insertvalue('BUSD',30000,'SELL','Papara', "D~",a7)
        insertvalue('BNB',30000,'SELL','Papara', "E~",a7)
        insertvalue('ETH',30000,'SELL','Papara', "F~",a7)
        insertvalue('DAI',30000,'SELL','Papara', "G~",a7)
        insertvalue('ADA',30000,'SELL','Papara', "H~",a7)
        insertvalue('SHIB',30000,'SELL','Papara', "H~",a7)
        insertvalue('DOGE',30000,'SELL','Papara', "H~",a7)
        insertvalue('TRX',30000,'SELL','Papara', "H~",a7)
        matrix.append(a7)
        insertvalue('USDT',30000,'SELL','VakifBank', "B~",a8)
        insertvalue('BTC',30000,'SELL','VakifBank', "C~",a8)
        insertvalue('BUSD',30000,'SELL','VakifBank', "D~",a8)
        insertvalue('BNB',30000,'SELL','VakifBank', "E~",a8)
        insertvalue('ETH',30000,'SELL','VakifBank', "F~",a8)
        insertvalue('DAI',30000,'SELL','VakifBank', "G~",a8)
        insertvalue('ADA',30000,'SELL','VakifBank', "H~",a8)
        insertvalue('SHIB',30000,'SELL','VakifBank', "H~",a8)
        insertvalue('DOGE',30000,'SELL','VakifBank', "H~",a8)
        insertvalue('TRX',30000,'SELL','VakifBank', "H~",a8)
        matrix.append(a8)
        insertvalue('USDT',30000,'SELL','ISBANK', "B~",a9)
        insertvalue('BTC',30000,'SELL','ISBANK', "C~",a9)
        insertvalue('BUSD',30000,'SELL','ISBANK', "D~",a9)
        insertvalue('BNB',30000,'SELL','ISBANK', "E~",a9)
        insertvalue('ETH',30000,'SELL','ISBANK', "F~",a9)
        insertvalue('DAI',30000,'SELL','ISBANK', "G~",a9)
        insertvalue('ADA',30000,'SELL','ISBANK', "H~",a9)
        insertvalue('SHIB',30000,'SELL','ISBANK', "H~",a9)
        insertvalue('DOGE',30000,'SELL','ISBANK', "H~",a9)
        insertvalue('TRX',30000,'SELL','ISBANK', "H~",a9)
        matrix.append(a9)
        insertvalue('USDT',30000,'SELL','QNB', "B~",a10)
        insertvalue('BTC',30000,'SELL','QNB', "C~",a10)
        insertvalue('BUSD',30000,'SELL','QNB', "D~",a10)
        insertvalue('BNB',30000,'SELL','QNB', "E~",a10)
        insertvalue('ETH',30000,'SELL','QNB', "F~",a10)
        insertvalue('DAI',30000,'SELL','QNB', "G~",a10)
        insertvalue('ADA',30000,'SELL','QNB', "H~",a10)
        insertvalue('SHIB',30000,'SELL','QNB', "H~",a10)
        insertvalue('DOGE',30000,'SELL','QNB', "H~",a10)
        insertvalue('TRX',30000,'SELL','QNB', "H~",a10)
        matrix.append(a10)
        insertvalue('USDT',30000,'SELL','Akbank', "B~",a11)
        insertvalue('BTC',30000,'SELL','Akbank', "C~",a11)
        insertvalue('BUSD',30000,'SELL','Akbank', "D~",a11)
        insertvalue('BNB',30000,'SELL','Akbank', "E~",a11)
        insertvalue('ETH',30000,'SELL','Akbank', "F~",a11)
        insertvalue('DAI',30000,'SELL','Akbank', "G~",a11)
        insertvalue('ADA',30000,'SELL','Akbank', "H~",a11)
        insertvalue('SHIB',30000,'SELL','Akbank', "H~",a11)
        insertvalue('DOGE',30000,'SELL','Akbank', "H~",a11)
        insertvalue('TRX',30000,'SELL','Akbank', "H~",a11)
        matrix.append(a11)
        insertvalue('USDT',30000,'SELL','KoronaPay', "B~",a12)
        insertvalue('BTC',30000,'SELL','KoronaPay', "C~",a12)
        insertvalue('BUSD',30000,'SELL','KoronaPay', "D~",a12)
        insertvalue('BNB',30000,'SELL','KoronaPay', "E~",a12)
        insertvalue('ETH',30000,'SELL','KoronaPay', "F~",a12)
        insertvalue('DAI',30000,'SELL','KoronaPay', "G~",a12)
        insertvalue('ADA',30000,'SELL','KoronaPay', "H~",a12)
        insertvalue('SHIB',30000,'SELL','KoronaPay', "H~",a12)
        insertvalue('DOGE',30000,'SELL','KoronaPay', "H~",a12)
        insertvalue('TRX',30000,'SELL','KoronaPay', "H~",a12)
        matrix.append(a12)
        insertvalue('USDT',30000,'SELL','Revolut', "B~",a13)
        insertvalue('BTC',30000,'SELL','Revolut', "C~",a13)
        insertvalue('BUSD',30000,'SELL','Revolut', "D~",a13)
        insertvalue('BNB',30000,'SELL','Revolut', "E~",a13)
        insertvalue('ETH',30000,'SELL','Revolut', "F~",a13)
        insertvalue('DAI',30000,'SELL','Revolut', "G~",a13)
        insertvalue('ADA',30000,'SELL','Revolut', "H~",a13)
        insertvalue('SHIB',30000,'SELL','Revolut', "H~",a13)
        insertvalue('DOGE',30000,'SELL','Revolut', "H~",a13)
        insertvalue('TRX',30000,'SELL','Revolut', "H~",a13)
        matrix.append(a13)
        insertvalue('USDT',30000,'SELL','BAKAIBANK', "B~",a14)
        insertvalue('BTC',30000,'SELL','BAKAIBANK', "C~",a14)
        insertvalue('BUSD',30000,'SELL','BAKAIBANK', "D~",a14)
        insertvalue('BNB',30000,'SELL','BAKAIBANK', "E~",a14)
        insertvalue('ETH',30000,'SELL','BAKAIBANK', "F~",a14)
        insertvalue('DAI',30000,'SELL','BAKAIBANK', "G~",a14)
        insertvalue('ADA',30000,'SELL','BAKAIBANK', "H~",a14)
        insertvalue('SHIB',30000,'SELL','BAKAIBANK', "H~",a14)
        insertvalue('DOGE',30000,'SELL','BAKAIBANK', "H~",a14)
        insertvalue('TRX',30000,'SELL','BAKAIBANK', "H~",a14)
        matrix.append(a14)
        insertvalue('USDT',30000,'SELL','Fibabanka', "B~",a15)
        insertvalue('BTC',30000,'SELL','Fibabanka', "C~",a15)
        insertvalue('BUSD',30000,'SELL','Fibabanka', "D~",a15)
        insertvalue('BNB',30000,'SELL','Fibabanka', "E~",a15)
        insertvalue('ETH',30000,'SELL','Fibabanka', "F~",a15)
        insertvalue('DAI',30000,'SELL','Fibabanka', "G~",a15)
        insertvalue('ADA',30000,'SELL','Fibabanka', "H~",a15)
        insertvalue('SHIB',30000,'SELL','Fibabanka', "H~",a15)
        insertvalue('DOGE',30000,'SELL','Fibabanka', "H~",a15)
        insertvalue('TRX',30000,'SELL','Fibabanka', "H~",a15)
        matrix.append(a15)
        insertvalue('USDT',30000,'SELL','Paysend', "B~",a16)
        insertvalue('BTC',30000,'SELL','Paysend', "C~",a16)
        insertvalue('BUSD',30000,'SELL','Paysend', "D~",a16)
        insertvalue('BNB',30000,'SELL','Paysend', "E~",a16)
        insertvalue('ETH',30000,'SELL','Paysend', "F~",a16)
        insertvalue('DAI',30000,'SELL','Paysend', "G~",a16)
        insertvalue('ADA',30000,'SELL','Paysend', "H~",a16)
        insertvalue('SHIB',30000,'SELL','Paysend', "H~",a16)
        insertvalue('DOGE',30000,'SELL','Paysend', "H~",a16)
        insertvalue('TRX',30000,'SELL','Paysend', "H~",a16)
        matrix.append(a16)
        insertvalue('USDT',30000,'SELL','RUBfiatbalance', "B~",a17)
        insertvalue('BTC',30000,'SELL','RUBfiatbalance', "C~",a17)
        insertvalue('BUSD',30000,'SELL','RUBfiatbalance', "D~",a17)
        insertvalue('BNB',30000,'SELL','RUBfiatbalance', "E~",a17)
        insertvalue('ETH',30000,'SELL','RUBfiatbalance', "F~",a17)
        insertvalue('DAI',30000,'SELL','RUBfiatbalance', "G~",a17)
        insertvalue('ADA',30000,'SELL','RUBfiatbalance', "H~",a17)
        insertvalue('SHIB',30000,'SELL','RUBfiatbalance', "H~",a17)
        insertvalue('DOGE',30000,'SELL','RUBfiatbalance', "H~",a17)
        insertvalue('TRX',30000,'SELL','RUBfiatbalance', "H~",a17)
        matrix.append(a17)
        insertvalue('USDT',30000,'SELL','CashDeposit', "B~",a18)
        insertvalue('BTC',30000,'SELL','CashDeposit', "C~",a18)
        insertvalue('BUSD',30000,'SELL','CashDeposit', "D~",a18)
        insertvalue('BNB',30000,'SELL','CashDeposit', "E~",a18)
        insertvalue('ETH',30000,'SELL','CashDeposit', "F~",a18)
        insertvalue('DAI',30000,'SELL','CashDeposit', "G~",a18)
        insertvalue('ADA',30000,'SELL','CashDeposit', "H~",a18)
        insertvalue('SHIB',30000,'SELL','CashDeposit', "H~",a18)
        insertvalue('DOGE',30000,'SELL','CashDeposit', "H~",a18)
        insertvalue('TRX',30000,'SELL','CashDeposit', "H~",a18)
        matrix.append(a18)
        insertvalue('USDT',30000,'SELL','Wise', "B~",a19)
        insertvalue('BTC',30000,'SELL','Wise', "C~",a19)
        insertvalue('BUSD',30000,'SELL','Wise', "D~",a19)
        insertvalue('BNB',30000,'SELL','Wise', "E~",a19)
        insertvalue('ETH',30000,'SELL','Wise', "F~",a19)
        insertvalue('DAI',30000,'SELL','Wise', "G~",a19)
        insertvalue('ADA',30000,'SELL','Wise', "H~",a19)
        insertvalue('SHIB',30000,'SELL','Wise', "H~",a19)
        insertvalue('DOGE',30000,'SELL','Wise', "H~",a19)
        insertvalue('TRX',30000,'SELL','Wise', "H~",a19)
        matrix.append(a19)
       
        
        
        
        
        
        wks1.update_values('M104:V122', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass