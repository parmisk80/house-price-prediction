import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression







data = {
    "room" : [11 , 12 , 13 , 14 , 15],
    "area" : [45000 , 65000 , 85000 , 120000 , 150000],
    "price" : [800000 , 120000 , 180000 , 250000 , 380000],
    "bathroom" : [1 , 2 , 3 , 4 , 8]
}


df = pd.DataFrame(data)

print("sample of dataset")
print(df)


X = df["area"].to_numpy().reshape(-1,1)

Y = df["price"].to_numpy()


print("X :")
print(X)

print("Y :")
print(Y)



model = LinearRegression()
model.fit(X , Y)


house_size = 1800
predicted_price = model.predict(np.array([[house_size]]))



print(f"house area : {house_size} square meter")

print(f"predicted price : {predicted_price[0]} dollar")
