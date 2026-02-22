# Import libraries
from sklearn.linear_model import LogisticRegression
import numpy as np


x = np.array([[1], [2], [3], [4], [5]])  
y=np.array([0,0,0,1,1])
model=LogisticRegression()
model.fit(x,y)
hours=float(input("Enter number of hours"))
result = model.predict([[hours]])[0] # input must be 2D
print("result is",result)
if result==1:
    print(f"based on  {hours} hours you are likely pass")
else:
    print(f"based on  {hours} hours you are likely failed")
