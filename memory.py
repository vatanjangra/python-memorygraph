import psutil
import time
import datetime
#run indefinite loop to continuosly return memory
while True:
    #current local time
    y=time.strftime("%H:%M:%S",time.localtime())
    #current used memory in gb
    x= psutil.phymem_usage().used/float(1073741824)
    #open test2.csv for writing
    text_file = open('test2.csv', 'w')
    #write time in csv format
    text_file.write('"' + y + '"'+',')
    #write memory in csv format
    text_file.write( '"%f"'%x)
    print "Time=%s Memory=%f"%(y,x)
    #close test2.csv to avoid file management conflict
    text_file.close()
    #sleep for 1 sec
    time.sleep(1)
