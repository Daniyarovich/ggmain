import pygsheets
import numpy as np
import requests
import sys 
import time
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('ТЗ на таблицу')
wks1 = sh.worksheet_by_title("Binance-RUB")
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
    a20= []
    a21= []
    a22= []
    a23= []
    a24= []
    a25= []
    a26= []
    a27= []

    
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
        insertvalue('USDT',+,'BUY','Ziraat', "B~",a1)
        insertvalue('BTC',+,'BUY','Ziraat', "C~",a1)
        insertvalue('BUSD',+,'BUY','Ziraat', "D~",a1)
        insertvalue('BNB',+,'BUY','Ziraat', "E~",a1)
        insertvalue('ETH',+,'BUY','Ziraat', "F~",a1)
        insertvalue('DAI',+,'BUY','Ziraat', "G~",a1)
        insertvalue('ADA',+,'BUY','Ziraat', "H~",a1)
        insertvalue('SHIB',+,'BUY','Ziraat', "H~",a1)
        insertvalue('DOGE',+,'BUY','Ziraat', "H~",a1)
        insertvalue('TRX',+,'BUY','Ziraat', "H~",a1)
        matrix.append(a1)
        
        insertvalue('USDT',+,'BUY','BANK', "B~",a2)
        insertvalue('BTC',+,'BUY','BANK', "C~",a2)
        insertvalue('BUSD',+,'BUY','BANK', "D~",a2)
        insertvalue('BNB',+,'BUY','BANK', "E~",a2)
        insertvalue('ETH',+,'BUY','BANK', "F~",a2)
        insertvalue('DAI',+,'BUY','BANK', "G~",a2)
        insertvalue('ADA',+,'BUY','BANK', "H~",a2)
        insertvalue('SHIB',+,'BUY','BANK', "H~",a2)
        insertvalue('DOGE',+,'BUY','BANK', "H~",a2)
        insertvalue('TRX',+,'BUY','BANK', "H~",a2)
        matrix.append(a2)
        
        
        insertvalue('USDT',+,'BUY','Garanti', "B~",a3)
        insertvalue('BTC',+,'BUY','Garanti', "C~",a3)
        insertvalue('BUSD',+,'BUY','Garanti', "D~",a3)
        insertvalue('BNB',+,'BUY','Garanti', "E~",a3)
        insertvalue('ETH',+,'BUY','Garanti', "F~",a3)
        insertvalue('DAI',+,'BUY','Garanti', "G~",a3)
        insertvalue('ADA',+,'BUY','Garanti', "H~",a3)
        insertvalue('SHIB',+,'BUY','Garanti', "H~",a3)
        insertvalue('DOGE',+,'BUY','Garanti', "H~",a3)
        insertvalue('TRX',+,'BUY','Garanti', "H~",a3)
        matrix.append(a3)
        insertvalue('USDT',+,'BUY','KuveytTurk', "B~",a4)
        insertvalue('BTC',+,'BUY','KuveytTurk', "C~",a4)
        insertvalue('BUSD',+,'BUY','KuveytTurk', "D~",a4)
        insertvalue('BNB',+,'BUY','KuveytTurk', "E~",a4)
        insertvalue('ETH',+,'BUY','KuveytTurk', "F~",a4)
        insertvalue('DAI',+,'BUY','KuveytTurk', "G~",a4)
        insertvalue('ADA',+,'BUY','KuveytTurk', "H~",a4)
        insertvalue('SHIB',+,'BUY','KuveytTurk', "H~",a4)
        insertvalue('DOGE',+,'BUY','KuveytTurk', "H~",a4)
        insertvalue('TRX',+,'BUY','KuveytTurk', "H~",a4)
        matrix.append(a4)
        insertvalue('USDT',+,'BUY','DenizBank', "B~",a5)
        insertvalue('BTC',+,'BUY','DenizBank', "C~",a5)
        insertvalue('BUSD',+,'BUY','DenizBank', "D~",a5)
        insertvalue('BNB',+,'BUY','DenizBank', "E~",a5)
        insertvalue('ETH',+,'BUY','DenizBank', "F~",a5)
        insertvalue('DAI',+,'BUY','DenizBank', "G~",a5)
        insertvalue('ADA',+,'BUY','DenizBank', "H~",a5)
        insertvalue('SHIB',+,'BUY','DenizBank', "H~",a5)
        insertvalue('DOGE',+,'BUY','DenizBank', "H~",a5)
        insertvalue('TRX',+,'BUY','DenizBank', "H~",a5)
        matrix.append(a5)
        insertvalue('USDT',+,'BUY','BanktransferTurkey', "B~",a6)
        insertvalue('BTC',+,'BUY','BanktransferTurkey', "C~",a6)
        insertvalue('BUSD',+,'BUY','BanktransferTurkey', "D~",a6)
        insertvalue('BNB',+,'BUY','BanktransferTurkey', "E~",a6)
        insertvalue('ETH',+,'BUY','BanktransferTurkey', "F~",a6)
        insertvalue('DAI',+,'BUY','BanktransferTurkey', "G~",a6)
        insertvalue('ADA',+,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('SHIB',+,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('DOGE',+,'BUY','BanktransferTurkey', "H~",a6)
        insertvalue('TRX',+,'BUY','BanktransferTurkey', "H~",a6)
        matrix.append(a6)
        insertvalue('USDT',+,'BUY','Papara', "B~",a7)
        insertvalue('BTC',+,'BUY','Papara', "C~",a7)
        insertvalue('BUSD',+,'BUY','Papara', "D~",a7)
        insertvalue('BNB',+,'BUY','Papara', "E~",a7)
        insertvalue('ETH',+,'BUY','Papara', "F~",a7)
        insertvalue('DAI',+,'BUY','Papara', "G~",a7)
        insertvalue('ADA',+,'BUY','Papara', "H~",a7)
        insertvalue('SHIB',+,'BUY','Papara', "H~",a7)
        insertvalue('DOGE',+,'BUY','Papara', "H~",a7)
        insertvalue('TRX',+,'BUY','Papara', "H~",a7)
        matrix.append(a7)
        insertvalue('USDT',+,'BUY','VakifBank', "B~",a8)
        insertvalue('BTC',+,'BUY','VakifBank', "C~",a8)
        insertvalue('BUSD',+,'BUY','VakifBank', "D~",a8)
        insertvalue('BNB',+,'BUY','VakifBank', "E~",a8)
        insertvalue('ETH',+,'BUY','VakifBank', "F~",a8)
        insertvalue('DAI',+,'BUY','VakifBank', "G~",a8)
        insertvalue('ADA',+,'BUY','VakifBank', "H~",a8)
        insertvalue('SHIB',+,'BUY','VakifBank', "H~",a8)
        insertvalue('DOGE',+,'BUY','VakifBank', "H~",a8)
        insertvalue('TRX',+,'BUY','VakifBank', "H~",a8)
        matrix.append(a8)
        insertvalue('USDT',+,'BUY','ISBANK', "B~",a9)
        insertvalue('BTC',+,'BUY','ISBANK', "C~",a9)
        insertvalue('BUSD',+,'BUY','ISBANK', "D~",a9)
        insertvalue('BNB',+,'BUY','ISBANK', "E~",a9)
        insertvalue('ETH',+,'BUY','ISBANK', "F~",a9)
        insertvalue('DAI',+,'BUY','ISBANK', "G~",a9)
        insertvalue('ADA',+,'BUY','ISBANK', "H~",a9)
        insertvalue('SHIB',+,'BUY','ISBANK', "H~",a9)
        insertvalue('DOGE',+,'BUY','ISBANK', "H~",a9)
        insertvalue('TRX',+,'BUY','ISBANK', "H~",a9)
        matrix.append(a9)
        insertvalue('USDT',+,'BUY','QNB', "B~",a10)
        insertvalue('BTC',+,'BUY','QNB', "C~",a10)
        insertvalue('BUSD',+,'BUY','QNB', "D~",a10)
        insertvalue('BNB',+,'BUY','QNB', "E~",a10)
        insertvalue('ETH',+,'BUY','QNB', "F~",a10)
        insertvalue('DAI',+,'BUY','QNB', "G~",a10)
        insertvalue('ADA',+,'BUY','QNB', "H~",a10)
        insertvalue('SHIB',+,'BUY','QNB', "H~",a10)
        insertvalue('DOGE',+,'BUY','QNB', "H~",a10)
        insertvalue('TRX',+,'BUY','QNB', "H~",a10)
        matrix.append(a10)
        insertvalue('USDT',+,'BUY','Akbank', "B~",a11)
        insertvalue('BTC',+,'BUY','Akbank', "C~",a11)
        insertvalue('BUSD',+,'BUY','Akbank', "D~",a11)
        insertvalue('BNB',+,'BUY','Akbank', "E~",a11)
        insertvalue('ETH',+,'BUY','Akbank', "F~",a11)
        insertvalue('DAI',+,'BUY','Akbank', "G~",a11)
        insertvalue('ADA',+,'BUY','Akbank', "H~",a11)
        insertvalue('SHIB',+,'BUY','Akbank', "H~",a11)
        insertvalue('DOGE',+,'BUY','Akbank', "H~",a11)
        insertvalue('TRX',+,'BUY','Akbank', "H~",a11)
        matrix.append(a11)
        insertvalue('USDT',+,'BUY','KoronaPay', "B~",a12)
        insertvalue('BTC',+,'BUY','KoronaPay', "C~",a12)
        insertvalue('BUSD',+,'BUY','KoronaPay', "D~",a12)
        insertvalue('BNB',+,'BUY','KoronaPay', "E~",a12)
        insertvalue('ETH',+,'BUY','KoronaPay', "F~",a12)
        insertvalue('DAI',+,'BUY','KoronaPay', "G~",a12)
        insertvalue('ADA',+,'BUY','KoronaPay', "H~",a12)
        insertvalue('SHIB',+,'BUY','KoronaPay', "H~",a12)
        insertvalue('DOGE',+,'BUY','KoronaPay', "H~",a12)
        insertvalue('TRX',+,'BUY','KoronaPay', "H~",a12)
        matrix.append(a12)
        insertvalue('USDT',+,'BUY','Revolut', "B~",a13)
        insertvalue('BTC',+,'BUY','Revolut', "C~",a13)
        insertvalue('BUSD',+,'BUY','Revolut', "D~",a13)
        insertvalue('BNB',+,'BUY','Revolut', "E~",a13)
        insertvalue('ETH',+,'BUY','Revolut', "F~",a13)
        insertvalue('DAI',+,'BUY','Revolut', "G~",a13)
        insertvalue('ADA',+,'BUY','Revolut', "H~",a13)
        insertvalue('SHIB',+,'BUY','Revolut', "H~",a13)
        insertvalue('DOGE',+,'BUY','Revolut', "H~",a13)
        insertvalue('TRX',+,'BUY','Revolut', "H~",a13)
        matrix.append(a13)
        insertvalue('USDT',+,'BUY','BAKAIBANK', "B~",a14)
        insertvalue('BTC',+,'BUY','BAKAIBANK', "C~",a14)
        insertvalue('BUSD',+,'BUY','BAKAIBANK', "D~",a14)
        insertvalue('BNB',+,'BUY','BAKAIBANK', "E~",a14)
        insertvalue('ETH',+,'BUY','BAKAIBANK', "F~",a14)
        insertvalue('DAI',+,'BUY','BAKAIBANK', "G~",a14)
        insertvalue('ADA',+,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('SHIB',+,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('DOGE',+,'BUY','BAKAIBANK', "H~",a14)
        insertvalue('TRX',+,'BUY','BAKAIBANK', "H~",a14)
        matrix.append(a14)
        insertvalue('USDT',+,'BUY','Fibabanka', "B~",a15)
        insertvalue('BTC',+,'BUY','Fibabanka', "C~",a15)
        insertvalue('BUSD',+,'BUY','Fibabanka', "D~",a15)
        insertvalue('BNB',+,'BUY','Fibabanka', "E~",a15)
        insertvalue('ETH',+,'BUY','Fibabanka', "F~",a15)
        insertvalue('DAI',+,'BUY','Fibabanka', "G~",a15)
        insertvalue('ADA',+,'BUY','Fibabanka', "H~",a15)
        insertvalue('SHIB',+,'BUY','Fibabanka', "H~",a15)
        insertvalue('DOGE',+,'BUY','Fibabanka', "H~",a15)
        insertvalue('TRX',+,'BUY','Fibabanka', "H~",a15)
        matrix.append(a15)
        insertvalue('USDT',+,'BUY','Paysend', "B~",a16)
        insertvalue('BTC',+,'BUY','Paysend', "C~",a16)
        insertvalue('BUSD',+,'BUY','Paysend', "D~",a16)
        insertvalue('BNB',+,'BUY','Paysend', "E~",a16)
        insertvalue('ETH',+,'BUY','Paysend', "F~",a16)
        insertvalue('DAI',+,'BUY','Paysend', "G~",a16)
        insertvalue('ADA',+,'BUY','Paysend', "H~",a16)
        insertvalue('SHIB',+,'BUY','Paysend', "H~",a16)
        insertvalue('DOGE',+,'BUY','Paysend', "H~",a16)
        insertvalue('TRX',+,'BUY','Paysend', "H~",a16)
        matrix.append(a16)
        insertvalue('USDT',+,'BUY','RUBfiatbalance', "B~",a17)
        insertvalue('BTC',+,'BUY','RUBfiatbalance', "C~",a17)
        insertvalue('BUSD',+,'BUY','RUBfiatbalance', "D~",a17)
        insertvalue('BNB',+,'BUY','RUBfiatbalance', "E~",a17)
        insertvalue('ETH',+,'BUY','RUBfiatbalance', "F~",a17)
        insertvalue('DAI',+,'BUY','RUBfiatbalance', "G~",a17)
        insertvalue('ADA',+,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('SHIB',+,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('DOGE',+,'BUY','RUBfiatbalance', "H~",a17)
        insertvalue('TRX',+,'BUY','RUBfiatbalance', "H~",a17)
        matrix.append(a17)
        insertvalue('USDT',+,'BUY','CashDeposit', "B~",a18)
        insertvalue('BTC',+,'BUY','CashDeposit', "C~",a18)
        insertvalue('BUSD',+,'BUY','CashDeposit', "D~",a18)
        insertvalue('BNB',+,'BUY','CashDeposit', "E~",a18)
        insertvalue('ETH',+,'BUY','CashDeposit', "F~",a18)
        insertvalue('DAI',+,'BUY','CashDeposit', "G~",a18)
        insertvalue('ADA',+,'BUY','CashDeposit', "H~",a18)
        insertvalue('SHIB',+,'BUY','CashDeposit', "H~",a18)
        insertvalue('DOGE',+,'BUY','CashDeposit', "H~",a18)
        insertvalue('TRX',+,'BUY','CashDeposit', "H~",a18)
        matrix.append(a18)
        insertvalue('USDT',+,'BUY','Wise', "B~",a19)
        insertvalue('BTC',+,'BUY','Wise', "C~",a19)
        insertvalue('BUSD',+,'BUY','Wise', "D~",a19)
        insertvalue('BNB',+,'BUY','Wise', "E~",a19)
        insertvalue('ETH',+,'BUY','Wise', "F~",a19)
        insertvalue('DAI',+,'BUY','Wise', "G~",a19)
        insertvalue('ADA',+,'BUY','Wise', "H~",a19)
        insertvalue('SHIB',+,'BUY','Wise', "H~",a19)
        insertvalue('DOGE',+,'BUY','Wise', "H~",a19)
        insertvalue('TRX',+,'BUY','Wise', "H~",a19)
        matrix.append(a19)
        insertvalue('USDT',+,'BUY','SEPA', "B~",a20)
        insertvalue('BTC',+,'BUY','SEPA', "C~",a20)
        insertvalue('BUSD',+,'BUY','SEPA', "D~",a20)
        insertvalue('BNB',+,'BUY','SEPA', "E~",a20)
        insertvalue('ETH',+,'BUY','SEPA', "F~",a20)
        insertvalue('DAI',+,'BUY','SEPA', "G~",a20)
        insertvalue('ADA',+,'BUY','SEPA', "H~",a20)
        insertvalue('SHIB',+,'BUY','SEPA', "H~",a20)
        insertvalue('DOGE',+,'BUY','SEPA', "H~",a20)
        insertvalue('TRX',+,'BUY','SEPA', "H~",a20)
        matrix.append(a20)
        insertvalue('USDT',+,'BUY','SEPAinstant', "B~",a21)
        insertvalue('BTC',+,'BUY','SEPAinstant', "C~",a21)
        insertvalue('BUSD',+,'BUY','SEPAinstant', "D~",a21)
        insertvalue('BNB',+,'BUY','SEPAinstant', "E~",a21)
        insertvalue('ETH',+,'BUY','SEPAinstant', "F~",a21)
        insertvalue('DAI',+,'BUY','SEPAinstant', "G~",a21)
        insertvalue('ADA',+,'BUY','SEPAinstant', "H~",a21)
        insertvalue('SHIB',+,'BUY','SEPAinstant', "H~",a21)
        insertvalue('DOGE',+,'BUY','SEPAinstant', "H~",a21)
        insertvalue('TRX',+,'BUY','SEPAinstant', "H~",a21)
        matrix.append(a21)
        insertvalue('USDT',+,'BUY','WesternUnion', "B~",a22)
        insertvalue('BTC',+,'BUY','WesternUnion', "C~",a22)
        insertvalue('BUSD',+,'BUY','WesternUnion', "D~",a22)
        insertvalue('BNB',+,'BUY','WesternUnion', "E~",a22)
        insertvalue('ETH',+,'BUY','WesternUnion', "F~",a22)
        insertvalue('DAI',+,'BUY','WesternUnion', "G~",a22)
        insertvalue('ADA',+,'BUY','WesternUnion', "H~",a22)
        insertvalue('SHIB',+,'BUY','WesternUnion', "H~",a22)
        insertvalue('DOGE',+,'BUY','WesternUnion', "H~",a22)
        insertvalue('TRX',+,'BUY','WesternUnion', "H~",a22)
        matrix.append(a22)
        insertvalue('USDT',+,'BUY','Bancamiga2', "B~",a23)
        insertvalue('BTC',+,'BUY','Bancamiga2', "C~",a23)
        insertvalue('BUSD',+,'BUY','Bancamiga2', "D~",a23)
        insertvalue('BNB',+,'BUY','Bancamiga2', "E~",a23)
        insertvalue('ETH',+,'BUY','Bancamiga2', "F~",a23)
        insertvalue('DAI',+,'BUY','Bancamiga2', "G~",a23)
        insertvalue('ADA',+,'BUY','Bancamiga2', "H~",a23)
        insertvalue('SHIB',+,'BUY','Bancamiga2', "H~",a23)
        insertvalue('DOGE',+,'BUY','Bancamiga2', "H~",a23)
        insertvalue('TRX',+,'BUY','Bancamiga2', "H~",a23)
        matrix.append(a23)
        insertvalue('USDT',+,'BUY','BurganBank', "B~",a24)
        insertvalue('BTC',+,'BUY','BurganBank', "C~",a24)
        insertvalue('BUSD',+,'BUY','BurganBank', "D~",a24)
        insertvalue('BNB',+,'BUY','BurganBank', "E~",a24)
        insertvalue('ETH',+,'BUY','BurganBank', "F~",a24)
        insertvalue('DAI',+,'BUY','BurganBank', "G~",a24)
        insertvalue('ADA',+,'BUY','BurganBank', "H~",a24)
        insertvalue('SHIB',+,'BUY','BurganBank', "H~",a24)
        insertvalue('DOGE',+,'BUY','BurganBank', "H~",a24)
        insertvalue('TRX',+,'BUY','BurganBank', "H~",a24)
        matrix.append(a24)
        insertvalue('USDT',+,'BUY','CashU', "B~",a25)
        insertvalue('BTC',+,'BUY','CashU', "C~",a25)
        insertvalue('BUSD',+,'BUY','CashU', "D~",a25)
        insertvalue('BNB',+,'BUY','CashU', "E~",a25)
        insertvalue('ETH',+,'BUY','CashU', "F~",a25)
        insertvalue('DAI',+,'BUY','CashU', "G~",a25)
        insertvalue('ADA',+,'BUY','CashU', "H~",a25)
        insertvalue('SHIB',+,'BUY','CashU', "H~",a25)
        insertvalue('DOGE',+,'BUY','CashU', "H~",a25)
        insertvalue('TRX',+,'BUY','CashU', "H~",a25)
        matrix.append(a25)
        insertvalue('USDT',+,'BUY','Cashapp', "B~",a26)
        insertvalue('BTC',+,'BUY','Cashapp', "C~",a26)
        insertvalue('BUSD',+,'BUY','Cashapp', "D~",a26)
        insertvalue('BNB',+,'BUY','Cashapp', "E~",a26)
        insertvalue('ETH',+,'BUY','Cashapp', "F~",a26)
        insertvalue('DAI',+,'BUY','Cashapp', "G~",a26)
        insertvalue('ADA',+,'BUY','Cashapp', "H~",a26)
        insertvalue('SHIB',+,'BUY','Cashapp', "H~",a26)
        insertvalue('DOGE',+,'BUY','Cashapp', "H~",a26)
        insertvalue('TRX',+,'BUY','Cashapp', "H~",a26)
        matrix.append(a26)
        insertvalue('USDT',+,'BUY','SkrillMoneybookers', "B~",a27)
        insertvalue('BTC',+,'BUY','SkrillMoneybookers', "C~",a27)
        insertvalue('BUSD',+,'BUY','SkrillMoneybookers', "D~",a27)
        insertvalue('BNB',+,'BUY','SkrillMoneybookers', "E~",a27)
        insertvalue('ETH',+,'BUY','SkrillMoneybookers', "F~",a27)
        insertvalue('DAI',+,'BUY','SkrillMoneybookers', "G~",a27)
        insertvalue('ADA',+,'BUY','SkrillMoneybookers', "H~",a27)
        insertvalue('SHIB',+,'BUY','SkrillMoneybookers', "H~",a27)
        insertvalue('DOGE',+,'BUY','SkrillMoneybookers', "H~",a27)
        insertvalue('TRX',+,'BUY','SkrillMoneybookers', "H~",a27)
        matrix.append(a27)
        
        
        
        
        
        wks1.update_values('B18:H29', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(10)
    pass