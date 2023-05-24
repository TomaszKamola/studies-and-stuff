from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV


# 2 a)
housing = fetch_california_housing()
X = housing.data
y = housing.target

# 2 b)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    train_size=0.7
)

# 2 c)
model = MLPRegressor().fit(X_train, y_train)

# 2 d)
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

# 2 e)
"""
Linear regression:
mae_train = 0.5334486799159137
mse_train = 0.5266769104206058
mae_test = 0.5290637381489675
mse_test = 0.5193663391261905

Multi-layer Perceptron regressor:
mae_train = 0.6283053855430213
mse_train = 0.7251402729908053
mae_test = 0.6324187419041993
mse_test = 0.6583540388821141
"""

# 2 f)
parameters = {
    "alpha": [0.0001, 0.001, 0.01, 0.1, 1],
    "hidden_layer_sizes": [(100,), (10,), (10, 10)],
    "learning_rate": ['constant', 'adaptive']    
}

mlpr = MLPRegressor(max_iter=10000)
gridCV = GridSearchCV(estimator=mlpr, param_grid=parameters)
gridCV.fit(X_train, y_train)

y_pred_train = gridCV.predict(X_train)
mae_train = mean_absolute_error(y_train, y_pred_train)
mse_train = mean_squared_error(y_train, y_pred_train)

y_pred_test = gridCV.predict(X_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
mse_test = mean_squared_error(y_test, y_pred_test)

means = {
    'mae_train': mae_train,
    'mse_train': mse_train,
    'mae_test': mae_test,
    'mse_test': mse_test
}

print("\nGridSearchCV:")

for key, val in means.items():
    print(key, '=' ,val)
    
"""
GridSearchCV:
mae_train = 0.6031037727584997
mse_train = 0.7210848837948141
mae_test = 0.606949467500593
mse_test = 0.815927205575369
"""