import numpy as np
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn import svm

diabetes = datasets.load_diabetes()

x = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

y_pred=clf.predict(x_test)

print("accuracy of linear kernel is:")
print(metrics.accuracy_score(y_test,y_pred))

newclf = svm.SVC(kernel='rbf')
newclf.fit(x_train, y_train)

y_pred_new=newclf.predict(x_test)

print("accuracy of RBF kernel is:")
print(metrics.accuracy_score(y_test,y_pred_new))