import urllib
import threading
import os

os.system("clear")
print """
REVERSE IP SIMPLE CEkEER\n
QIUBY ZHUKHI
"""
target = "/storage/emulated/0/a/target.txt"
log= "/storage/emulated/0/a/log.txt"
def ip():
    buka = open(target).read()
    a = buka.split("\n")
    return a

def main(ip):
        link = urllib.urlopen("http://api.hackertarget.com/reverseiplookup/?q={}".format(i)).read()
        print link
        save = open(log, "a+")
        save.write(link)

threads = []
ip = ip()
if __name__ == "__main__":
    for  i in ip:
        print i
        t = threading.Thread(target=main(ip), args=(i,))
        threads.append(t)

for i in threads:
    i.start()
for i in threads:
    i.join()

print "SELSAI"