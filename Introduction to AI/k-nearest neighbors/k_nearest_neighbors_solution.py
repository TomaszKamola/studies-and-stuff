import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits.mplot3d
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.inspection import DecisionBoundaryDisplay


# Zadanie 4. a)
iris = load_iris()
X = iris.data
y = iris.target

# Zadanie 4. b)
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    stratify=y, 
    train_size=0.7, 
    test_size=0.3
)

# Zadanie 4. c)
model = KNeighborsClassifier(n_neighbors=3)

# Zadanie 4. d)                                             
model.fit(X_train, y_train)                                                             
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(acc)

# Zadanie 4. e)
neighbors = [i for i in range(1, 23, 2)]
accuracy = []

for n in neighbors:
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc)

fig, ax = plt.subplots()
ax.plot(neighbors, accuracy, linewidth=2.0)
plt.xticks(neighbors)
plt.yticks(accuracy)
plt.title("Zależność dokładności od liczby k-sąsiadów (n)")
plt.xlabel("Liczba k-sąsiadów (n)")
plt.ylabel("Dokładność")

plt.show()

# Zadanie 4. f)
# 1)
classifier = KNeighborsClassifier(n_neighbors=15)
classifier.fit(X_train, y_train)

# 2)
np.set_printoptions(precision=2)

titles_options = [
    ("Macierz konfuzji bez normalizacji", None),
    ("Znormalizowana macierz konfuzji", "true"),
]

for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=iris.target_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

# 3)
X = iris.data[:, :2]
y = iris.target

cmap_light = ListedColormap(["red", "green", "aquamarine"])
cmap_bold = ["darkred", "darkgreen", "c"]

classifier.fit(X, y)

_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    classifier,
    X,
    cmap=cmap_light,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
    shading="auto",
)

sns.scatterplot(
    x=X[:, 0],
    y=X[:, 1],
    hue=iris.target_names[y],
    palette=cmap_bold,
    alpha=1.0,
    edgecolor="black",
)

plt.title("Klasyfikacja trzech klas (k = 15)")

plt.show()


y = classifier.predict(X)
classifier.fit(X, y)

cmap_light = ListedColormap(["red", "aquamarine", "green"])

_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    classifier,
    X,
    cmap=cmap_light,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
    shading="auto",
)

sns.scatterplot(
    x=X[:, 0],
    y=X[:, 1],
    hue=iris.target_names[y],
    palette=cmap_bold,
    alpha=1.0,
    edgecolor="black",
)

plt.title("Klasyfikacja trzech klas po zmianie wektora na wynik predykcji (k = 15)")

plt.show()

# 4)
X = iris.data[:, :3]
y = iris.target

classifier.fit(X, y)

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

cmap = ListedColormap(["darkred", "darkgreen", "c"])

for label in iris.target_names:
    scatter = ax.scatter(
        X[:, 0],
        X[:, 1],
        X[:, 2],
        c=y,
        cmap=cmap,
        edgecolor="k",
        label=label,
        s=40,
    )

ax.set_title("Wizualizacja 3D na podstawie trzech zmiennych")
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
plt.show()