from sklearn import tree
features = [[140,1],[130,1],[150,0],[140,1]]
labels =[0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print("Enter weight and 0 or 1 for wrinkled or not")
wt,w = int(input()),int(input())
if clf.predict([[100, 0]]):
    print("Orange")
else:
    print("Not Orange")
