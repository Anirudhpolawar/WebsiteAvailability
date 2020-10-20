import datetime as dt
import time
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
SQL = "select statuscode from allsafe where datetime = "

def getconnection(user=None,password=None,host=None,database=None):
    con = None
    try:
        con = psycopg2.connect(host=host,database=database,user = user,password = password)
    except (Exception, psycopg2.Error) as error :
        print ("Error Connecting : ", error)
    return con


try:
    con = getconnection(user="allsafe",database="AllSafeP1",password = "123456",host="localhost")
    if con:
        cursor = con.cursor()
        print (con.get_dsn_parameters())
        print("TimeStamp  \t\t Status Code")
        while True:
            timenow = (dt.datetime.now() - dt.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S") #getting one sec less than current
            cursor.execute(SQL+"\'"+timenow+"\'")
            record = cursor.fetchone()
            if record:
                print(timenow+" \t "+str(record[0]))
                y.append(record[0])
                x.append(timenow)
                plt.clf()           
                plt.plot(x,y,color='green', linestyle='dashed', marker='o',markerfacecolor='green', markersize=8)
                plt.pause(0.1)
                if len(x)>5:
                    x.pop(0)
                    y.pop(0)
            time.sleep(0.900)
except (Exception) as error :
    print ("Error : ", error)
finally:                            
        if(con):                            #closing connections, cursor and plt
            cursor.close()
            con.close()
            plt.close()
            print("Connection Closed")




