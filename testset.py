from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size= .5)

from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, Y_train)

predictions = my_classifier.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print (accuracy_score(Y_test,predictions))
