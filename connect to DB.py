import requests
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import time

def getLastPrice(cryptocurrency):
    # зайти в БД id удалить и блабла id_cryptocurrency
    # """select name_string from cryptocurrency where id = %s"""
    url = f"https://data.messari.io/api/v1/assets/{cryptocurrency}/metrics"
    r = requests.get(url)
    info = r.json()
    return round(info['data']['market_data']['price_usd'], 2)

def connectToBD(dbname, user, password, host):
    try:
        conn = psycopg2.connect(dbname=dbname,
                                user=user,
                                password=password,
                                host=host)
        cursor = conn.cursor()
        print(cursor)
    except (Exception, Error) as error:
        print(f"Ошибка при работе с PostgreSQL\n{error}")

    finally:

        return conn

def updateLastPrice(conn, last_price):
    cursor = conn.cursor()
    last_price = str(last_price)
    sql_query = """UPDATE cryptocurrency SET last_price_string = %s WHERE id = 1;"""
    cursor.execute(sql_query, (last_price,))
    conn.commit()
    cursor.close()

def updateLastPrice2(conn2, last_price2):
    cursor2 = conn2.cursor()
    last_price2 = str(last_price2)
    sql_query = """UPDATE cryptocurrency SET last_price_string = %s WHERE id = 2;"""
    cursor2.execute(sql_query, (last_price2,))
    conn2.commit()
    cursor2.close()

def updateLastPrice3(conn3, last_price3):
    cursor3 = conn3.cursor()
    last_price3 = str(last_price3)
    sql_query = """UPDATE cryptocurrency SET last_price_string = %s WHERE id = 3;"""
    cursor3.execute(sql_query, (last_price3,))
    conn3.commit()
    cursor3.close()   

def updateLastPrice4(conn4, last_price4):
    cursor4 = conn4.cursor()
    last_price4 = str(last_price4)
    sql_query = """UPDATE cryptocurrency SET last_price_string = %s WHERE id = 4;"""
    cursor4.execute(sql_query, (last_price4,))
    conn4.commit()
    cursor4.close() 

def updateLastPrice5(conn5, last_price5):
    cursor5 = conn5.cursor()
    last_price5 = str(last_price5)
    sql_query = """UPDATE cryptocurrency SET last_price_string = %s WHERE id = 5;"""
    cursor5.execute(sql_query, (last_price5,))
    conn5.commit()
    cursor5.close() 

if __name__ == "__main__":

    dbname = 'tgbotinfo'
    user = 'postgres'
    password = '5972'
    host = 'localhost'
    conn = connectToBD(dbname, user, password, host)
    while True:
        cryptocurrency = 'Bitcoin'
        last_price = getLastPrice(cryptocurrency)
        cryptocurrency2 = 'Ethereum'
        last_price2 = getLastPrice(cryptocurrency2)
        cryptocurrency3 = 'Tether'
        last_price3 = getLastPrice(cryptocurrency3)
        cryptocurrency4 = 'USDC'
        last_price4 = getLastPrice(cryptocurrency4)
        cryptocurrency5 = 'BNB'
        last_price5 = getLastPrice(cryptocurrency5)
        updateLastPrice(conn, last_price)
        updateLastPrice2(conn, last_price2)
        updateLastPrice3(conn, last_price3)
        updateLastPrice4(conn, last_price4)
        updateLastPrice5(conn, last_price5)
        time.sleep(100)


