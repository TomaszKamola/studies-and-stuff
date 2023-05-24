import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.colors import ListedColormap
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    train_size=0.7
)

# k - nearest neighbors model
knn = KNeighborsClassifier()

n_neighbors = [i for i in range(1, 26, 4)]

parameters = {
    "n_neighbors": n_neighbors
}
    
gscv = GridSearchCV(estimator=knn, param_grid=parameters)
gscv.fit(X_train, y_train)

fig, ax = plt.subplots()
ax.errorbar(
    x=n_neighbors,
    y=gscv.cv_results_["mean_test_score"],
    yerr=gscv.cv_results_["std_test_score"],
)
plt.title("Zależność dokładności od liczby k-sąsiadów (n)")
plt.xlabel("Liczba k-sąsiadów (n)")
plt.ylabel("Dokładność")
plt.xticks(n_neighbors)

plt.show()

y_pred = gscv.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(acc)

# support vector machines

# multi-layer perceptron