from sklearn.tree import DecisionTreeClassifier
x=[
    [7,2],
    [8,3],
    [9,7],
    [10,8]
]
y=[0,0,1,1]
model=DecisionTreeClassifier()
model.fit(x,y)
shade=float(input("enter the weight in "))
size=float(input("enter the size in cm"))
prediction=model.predict([[size,shade]])[0]
if prediction==1:
    print(f"based on  it is  likely orange")
else:
    print(f"based onit is  likely apple")