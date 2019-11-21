import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

y = np.array([49,45,44,39,38,37,34,33,30,29])
# model = LinearRegression()
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
