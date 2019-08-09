import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


y_test = [3.88,  2.843, 3.748, 2.672, 4.991, 2.94, 6.804, 7.093, 3.977, 8.477]
pred = [6.53393622, 4.71255622, 4.19959882, 9.10539468, 9.32036666, 8.3569362,5.66960553, 5.50192872, 4.1230772, 8.8089035]

plt.scatter(y_test, pred)
plt.plot([0, 15], [0, 15], 'k--')
plt.xlabel('Actual DCM')
plt.ylabel('Predicted DCM')
plt.show()


dcm_unbiased = [2.21271845, 0.87047952, 1.25993671, 0.46390884, 0.43943193, 2.22930551,
 1.07920551, 1.1773969,  0.80923975, 1.74742685]

yerr = [1.38505855, 0.92173275, 1.10243827, 0.76079157, 0.67521834, 1.39961693,
 1.1074282,  1.01316234, 0.80503663, 1.20935715]


plt.errorbar(y_test, pred, yerr=np.sqrt(dcm_unbiased), fmt='o')
plt.plot([0, 15], [0, 15])#, 'k--')
plt.xlabel('Actual DCM')
plt.ylabel('Predicted DCM')
plt.show()
