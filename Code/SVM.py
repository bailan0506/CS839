
# coding: utf-8

# In[2]:


#cd E:\18Spring\CS839\Stage1\CS839_1\Code


# In[12]:


import os
import sys
#from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score

fid = './train.txt';
f = open(fid);
Xtr = []; Ytr = [];
while 1:
	x = f.readline();
	if not x:
		break;
	x = x.rstrip('\n');
	x = x.split(',');
	x = [float(x[i]) for i in range(len(x))];
	y = f.readline();
	y = y.rstrip('\n');
	y = float(y);
	Xtr.append(x);
	Ytr.append(y);
f.close();


fid = './test.txt';
f = open(fid);
Xte = []; Yte = [];
while 1:
	x = f.readline();
	if not x:
		break;
	x = x.rstrip('\n');
	x = x.split(',');
	x = [float(x[i]) for i in range(len(x))];
	y = f.readline();
	y = y.rstrip('\n');
	y = float(y);
	Xte.append(x);
	Yte.append(y);
f.close();

clf = svm.SVC()
scores = cross_val_score(clf, Xtr, Ytr, cv=5)
print scores, scores.mean();

clf.fit(Xtr, Ytr);
Yp = clf.predict(Xte);
Np = 0;
Nr = 0;
TotalPositive = 0;
for i in range(len(Yte)):
	if Yp[i]==Yte[i]:
		Np += 1;
	if Yte[i]==1:
		TotalPositive += 1;
		if Yp[i]==Yte[i]:
			Nr += 1;

print('Precision: %f' %(float(Np)/len(Yte)));
print('Recall: %f' %(float(Nr)/TotalPositive));