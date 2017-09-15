from datetime import datetime
import os
import time
from multiprocessing import Process
import thread
import  threading
import way2sms
import sys
data=list()







def fun1():


    #while True:
        #sem.acquire()
    req=raw_input("Do u want to set reminder y/n? :")
    if req == 'y':
        var1 = raw_input("ENTER Date And Time To Remind In Format MM/DD/YY HH:MM:SS  :")
        var2 = raw_input("Enter the event/to do  :")
        var3 = raw_input("Enter Mobile no :")
        tuple = (var1, var2, var3)
        data.append(tuple)
        #sem.release()
        #time.sleep(1)


def fun3():

    #print 'hhhh'
    while True:
        #sem.acquire()
        if len(data) != 0:
            #print "i m here "
            #print (datetime.strftime(datetime.now(),'%D %T'))
            if data[0][0] <= datetime.strftime(datetime.now(),'%D %T'):
                way2sms_message = str(data[0][1])
                way2sms_number = str(data[0][2])

                way2sms.function(way2sms_message,way2sms_number)
                data.remove(data[0])

        #sem.release()
        #time.sleep(1)







if __name__ == '__main__':
    p1=Process(target=fun1())
    p1.start()
    p1.join()
    p2=Process(target=fun3())
    p2.start()
    p1.join()





#date_entry=datetime.strptime(var1,"%Y-%m-%d %H:%M:%S")
