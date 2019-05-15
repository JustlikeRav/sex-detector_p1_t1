from sklearn import tree

# https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=1

x = [[181,70,21], [110,55,24], [160,62,25], [130,62,25], [120,63,26], [172,65,23],
     [140,64,24], [173,35,23], [120,62,22]]

y = ['female', 'male', 'female', 'male', 'male', 'female', 'female', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[190, 70, 43]])

print (prediction)
