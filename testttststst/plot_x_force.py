import pandas as pd
import matplotlib.pyplot as plt

SESSION = ['23.txt', '2.txt', '3.txt', '4.txt', '5.txt']

def insert_comma():
    for i in range(0, 5):
        with open(SESSION[i], 'r') as data:
            txt = data.read()

        txt = txt.replace(' ', ',')

        with open(SESSION[i], 'w') as replace:
            replace.write(txt)

def plot(session):
    mov = session.ix[:, 1]
    force = session.ix[:, 10]
    mov.plot()
    force.plot()
    plt.show()

    
#Insert comma into text file
insert_comma()

#Convert the new csv files to pd dataframes
session1 = pd.read_csv(SESSION[0])
session2 = pd.read_csv(SESSION[1])
session3 = pd.read_csv(SESSION[2])
session4 = pd.read_csv(SESSION[3])
session5 = pd.read_csv(SESSION[4])

#Plot session 
plot(session1)


moveShotReg = session1.ix[:, 1]
forceShotReg = session1.ix[:, 10]

indexCnt = []
for i in range(0, session1.size):
    if forceShotReg.iloc[i] > 5500:
        print(forceShotReg.iloc[i])
        #indexCnt.append(forceShotReg.iloc[i])
#print(indexCnt)

#indexCnt = []
#for i in range(0, session1.size):
    #if moveShotReg[i] > 10000 and forceShotReg[i] > 6000:
        #indexCnt.append(moveShotReg[i])

#print("INDEX COUNT\n\n\n\n", indexCnt[0])
#print(forceShotReg)


