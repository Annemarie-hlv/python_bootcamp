from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Create some very simple data
# X = Hours studied, y = Exam Score
X = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([10, 20, 30, 40, 50])

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[6]])

print(f'Predicted score if I study for 6 hours: {prediction[0]}')