import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('house_data.csv')

# Handle categorical features (convert 'Garage' and 'Pool' to numerical values)
label_encoder = LabelEncoder()
data['Garage'] = label_encoder.fit_transform(data['Garage'])
data['Garden'] = label_encoder.fit_transform(data['Garden'])

# Define the independent variables (features) and the dependent variable (target)
X = data[['Area', 'Bedrooms', 'Bathrooms', 'Floors', 'Age', 'Garage', 'Lot Size', 'Garden']]  # Features
y = data['Price']  # Target (Price)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate and print the Mean Squared Error (MSE) and R-squared Score (R²)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Optional: Save the trained model using pickle
with open('house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Plotting predicted vs actual prices (optional)
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.show()