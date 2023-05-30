import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.colors import ListedColormap
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.3,
    train_size=0.7
)
for i in range(1, 100):
    # k - nearest neighbors model
    k_range = [i for i in range(1, 26, 2)]
    parameters = dict(n_neighbors=k_range)
    knn = KNeighborsClassifier()
        
    grid = GridSearchCV(estimator=knn, param_grid=parameters, scoring='accuracy')
    grid_search = grid.fit(X_train, y_train)
    best = grid_search.best_params_
    accuracy = grid_search.best_score_ * 100
    print("\nK-Nearest Neighbors:\n")
    print(f"Optymalna wartość parametru: {best}")
    print(f"Wartość dokładności optymalnych parametrów dla danego zbioru wynosi: {accuracy:.2f}%")

    knn = KNeighborsClassifier(n_neighbors=best['n_neighbors'])
    knn.fit(X, y)
    y_pred = knn.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"Wartość dokładności predykcji: {test_accuracy:.2f}%\n")

    # support vector machines
    kernels = ['linear', 'rbf']
    Cs = [float(i) for i in range(1,11)]
    parameters = dict(kernel=kernels, C=Cs)
    svc = SVC()

    grid = GridSearchCV(estimator=svc, param_grid=parameters, scoring='accuracy')
    grid_search = grid.fit(X_train, y_train)
    best = grid_search.best_params_
    accuracy = grid_search.best_score_ * 100
    print("\nSVC:\n")
    print(f"Optymalna wartość parametrów: {best}")
    print(f"Wartość dokładności optymalnych parametrów dla danego zbioru wynosi: {accuracy:.2f}%")

    svc = SVC(C=best['C'], kernel=best['kernel'])
    svc.fit(X, y)
    y_pred = svc.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"Wartość dokładności predykcji: {test_accuracy:.2f}%\n")

    # multi-layer perceptron