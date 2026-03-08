import numpy as np
hours=np.array([[1],[2],[3],[4]])
marks=np.array([50,60,70,80])
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(hours,marks)
studyhours=float(input("Enter the number hours you study    :  "))
prediction=model.predict([[studyhours]])[0]
print(f"The number hours {studyhours} and the expeted marks are {prediction}")