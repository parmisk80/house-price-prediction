# 🏠 House Price Prediction using Linear Regression  

This project demonstrates a simple machine learning model for predicting house prices based on their area (square meters).  

We use Linear Regression from scikit-learn to train a model using a small dataset that includes the number of rooms, area, price, and bathrooms.  

---

## 📂 Dataset  

The dataset is defined directly in the code as a dictionary and then converted into a Pandas DataFrame:  

| room | area   | price   | bathroom |
|------|--------|---------|----------|
| 11   | 45000  | 800000  | 1        |
| 12   | 65000  | 120000  | 2        |
| 13   | 85000  | 180000  | 3        |
| 14   | 120000 | 250000  | 4        |
| 15   | 150000 | 380000  | 8        |

---

## ⚙️ How it works  

1. The model is trained with `area` as the feature (X) and `price` as the target (Y).  
2. Data is reshaped into NumPy arrays for training.  
3. A Linear Regression model is created and fitted with the dataset.  
4. After training, the model can predict the price of a house based on its area.  

---

## 🚀 Example  

```python
house_size = 1800
predicted_price = model.predict(np.array([[house_size]]))
