

from subprocess import call
import os
import sys
import time
from threading import Thread
from multiprocessing import Process
#os.system('ls')

termFR = sys.argv[1]
termEN = sys.argv[2]

commandFR00 = 'python 00collocationWindFR.py corpus/vulcanoFR-POS.txt '+termFR+' stopWords/StopWordsFR.txt'
commandEN00 = 'python 00collocationWindEN.py corpus/vulcanoEN-POS.txt '+termEN+' stopWords/StopWordsEN.txt'

commandFR01 = 'python 01collocationsFR.py '+termFR
commandEN01 = 'python 01collocationsEN.py '+termEN

commandENFR02 = 'python 02alignement-coll.py '+termFR+' '+termEN
commandENFR03 = 'python 03sentences.py'

commandENFR04 = 'python	04evaluation-affine.py'
commandENFR05 = 'python 06-trans.py'

start_time = time.time()

os.system(commandFR00)
os.system(commandEN00)

os.system(commandFR01)
os.system(commandEN01)

os.system(commandENFR02)
os.system(commandENFR03)


os.system("ssconvert -O 'separator=|' finall.xls all.txt")


os.system(commandENFR04)
os.system(commandENFR05)


end_time = time.time()

print "Time = {:.2f} seconds.".format(end_time - start_time)
