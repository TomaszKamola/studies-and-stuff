import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


#
housing = fetch_california_housing()
X = housing.data
y = housing.target

# 
names = [
    'Mediana dochodów w grupie blokowej',
    'Wiek domu w grupie blokowej',
    'Średnia liczba pokoi',
    'Średnia liczba sypialni',
    'Średnia populacja grupy blokowej',
    'Średnia ilość mieszkańców domu',
    'Szerokość grupy blokowej',
    'Długość grupy blokowej'
]

for i in range(8):
    plt.figure(figsize=(19,10))
    plt.scatter(X[:, i], y, s=0.1, c='red')
    plt.title(f"Mediana wartości domu w 100000$ (y) w zależności od:\n{names[i]} (x)")
    plt.xlabel(names[i])
    plt.ylabel("Mediana wartości domu w 100000$ (y)")
    plt.show()

# 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    train_size=0.7
)

# 
model = LinearRegression().fit(X_train, y_train)

# 2 e)
y_pred_train = model.predict(X_train)
mae_train = mean_absolute_error(y_train, y_pred_train)
mse_train = mean_squared_error(y_train, y_pred_train)

y_pred_test = model.predict(X_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
mse_test = mean_squared_error(y_test, y_pred_test)

means = {
    'mae_train': mae_train,
    'mse_train': mse_train,
    'mae_test': mae_test,
    'mse_test': mse_test
}

for key, val in means.items():
    print(key, '=' ,val)

# 2 f)
for i in range(8):
    X_reshaped = X_train[:, i].reshape(-1, 1)
    model_train = LinearRegression().fit(X_reshaped, y_train)

    y_pred = model_train.predict(X_reshaped)

    plt.figure(figsize=(19,10))
    plt.scatter(X_reshaped, y_train, s=0.1, c='red')
    plt.plot(X_reshaped, y_pred, c="blue")
    plt.title(f"Mediana wartości domu w 100000$ (y) w zależności od:\n{names[i]} (x)")
    plt.xlabel(names[i])
    plt.ylabel("Mediana wartości domu w 100000$ (y)")
    plt.show()

    mae = mean_absolute_error(y_train, y_pred)
    mse = mean_squared_error(y_train, y_pred)

    print(
        f"{i+1}: MAE = {mae}\n{i+1}: MSE = {mse}"
    )