# -*- coding: utf-8 -*-
"""tugas3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13RkrV8HDOOwGB49Nep4Mn1x-oOK0vx9z
"""

import numpy as np
import matplotlib.pyplot as plt
index = np.arange(5)
values = [5,7,3,4,6]
plt.bar(index,values)
plt.xticks(index+0.4,['A','B','C','D','E'])
plt.show()