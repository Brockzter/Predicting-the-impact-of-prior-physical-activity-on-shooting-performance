import pandas as pd
import matplotlib.pyplot as plt

SESSION = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']

def insert_comma():
    for i in range(0, 5):
        with open(SESSION[i], 'r') as data:
            txt = data.read()

        txt = txt.replace(' ', ',')

        with open(SESSION[i], 'w') as replace:
            replace.write(txt)

#Insert comma into text file
#insert_comma()

#Convert the new csv files to pd dataframes
session1 = pd.read_csv(SESSION[0])
session2 = pd.read_csv(SESSION[1])
session3 = pd.read_csv(SESSION[2])
session4 = pd.read_csv(SESSION[3])
session5 = pd.read_csv(SESSION[4])

#Plot movement
mov = session1.ix[:, 1]
mov.plot()

#Plot force
force = session1.ix[:, 10]
force.plot()
plt.show()
