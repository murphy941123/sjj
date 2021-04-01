import  subprocess
from time import ctime
def appium_start(host,port):

    bootstrap_port=str(port+1)
    cmd='start/b appium -a'+host+' -p '+str(port)+' -bp '+str(bootstrap_port)

    print('%s at %s' %(cmd,ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./log'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

