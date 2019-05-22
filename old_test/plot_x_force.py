#import pandas as pd
import matplotlib.pyplot as plt

SESSION = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
COLUMNS = ["NaN", "NaN.1", "NaN.2", "NaN.3", "NaN.4", "NaN.5", "NaN.6",
           "NaN.7", "NaN.8", "NaN.9", "NaN.10", "NaN.11", "NaN.12"]
THRESHOLD_MOVEMENT = 10000
THRESHOLD_FORCE = 100
def insert_comma():
    for i in range(0, 5):
        with open(SESSION[i], 'r') as data:
            txt = data.read()
        txt = txt.replace(' ', ',')

        with open (SESSION[i], 'w') as add_col:
            add_col.write('time,acc,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,force,NaN,NaN,NaN,NaN,NaN\n')

        with open(SESSION[i], 'a') as replace:
            replace.write(txt)
                          
def plot(session):
    mov = session.ix[:, 1]
    force = session.ix[:, 2]
    mov.plot()
    force.plot()
    plt.show()
   
#Insert comma into text file
#insert_comma()

#Convert the new csv files to pd dataframes
session1 = pd.read_csv(SESSION[0])
session2 = pd.read_csv(SESSION[1])
session3 = pd.read_csv(SESSION[2])
session4 = pd.read_csv(SESSION[3])
session5 = pd.read_csv(SESSION[4])

#Remove excess columns
session1 = session1.drop(columns=COLUMNS)
session2 = session2.drop(columns=COLUMNS)
session3 = session3.drop(columns=COLUMNS)
session4 = session4.drop(columns=COLUMNS)
session5 = session5.drop(columns=COLUMNS)

#Plot session
plot(session1)
plt.show()

sess_list = session1.values.tolist()
#print(sess_list)

force_lst = session1['force'].tolist()
move_lst = session1['acc'].tolist()

indexCnt = 0
indexT1 = []
indexT2 = []
for i in range(0, len(move_lst)):
    if move_lst[i] > THRESHOLD_MOVEMENT:
        print("index COUNTER", indexCnt)
        indexT1.append(force_lst[indexCnt-300])
        indexT2.append(force_lst[indexCnt])
    indexCnt += 1

print("INDEX t1", indexT1)
print("INDEX t2", indexT2)

plt.plot(indexT1)
#plt.scatter(indexT1, indexT2)
plt.show()
#for x in range(indexCnt1, 0, -1):
#            if force_lst[x] < (force_lst[indexCnt1] - (force_lst[indexCnt1]*2)):
 #print(force_lst[x])
 #indexTime.append(force_lst[x])
#print(indexTime)
#moveShotReg = session1.ix[:, 1]
#forceShotReg = session1.ix[:, 10]

#indexCnt = []
#for i in range(0, session1.size):
#    if moveShotReg.ix[1, i] > 14000 and forceShotReg.ix[1, i] > 6000:
#        indexCnt.append(moveShotReg.ix[1, i])
#print(indexCnt)

