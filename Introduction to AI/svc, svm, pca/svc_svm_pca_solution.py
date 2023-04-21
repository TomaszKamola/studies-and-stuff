import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.decomposition import PCA
from sklearn.inspection import DecisionBoundaryDisplay


# 4 a)
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 4 b)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.3,
    train_size=0.7
)

# 4 c)
model = SVC().fit(X_train, y_train)
y_pred = model.predict(X_test)

# 4 d)
acc = accuracy_score(y_test, y_pred)
print(acc)

# 4 e)
kernels = ['linear', 'rbf']
Cs = [float(i) for i in range(1,11)]

for kernel in kernels:
    accuracy = []

    for C in Cs:
        clf = SVC(C=C, kernel=kernel)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracy.append(acc)

    fig, ax = plt.subplots()
    plt.plot(Cs, accuracy)
    plt.xticks(Cs)
    plt.yticks(accuracy)
    plt.title(f"Zależność dokładności od liczby C dla kernela '{kernel}'")
    plt.xlabel("Liczba C")
    plt.ylabel("Dokładność")

    plt.show()

# 4 f)
clf_lin = SVC(C=8.0, kernel='linear').fit(X, y)
clf_rbf = SVC(C=2.0, kernel='rbf').fit(X, y)

# 1)
np.set_printoptions(precision=2)
models = [clf_lin, clf_rbf]
Cs = [8.0, 2.0]

for clf, kernel, C in zip(models, kernels, Cs):
    titles_options = [
        (f"Macierz konfuzji bez normalizacji dla kernela {kernel} i C={C}", None),
        (f"Znormalizowana macierz konfuzji dla kernela {kernel} i C={C}", "true"),
    ]

    for title, normalize in titles_options:
        disp = ConfusionMatrixDisplay.from_estimator(
            clf,
            X_test,
            y_test,
            display_labels=cancer.target_names,
            cmap=plt.cm.Blues,
            normalize=normalize,
        )

        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

        plt.show()

# 2)
L = PCA(n_components=3).fit_transform(X)

colors = ['blue', 'orange']

for clf, kernel, C in zip(models, kernels, Cs):

    for label, i, color in zip(cancer.target_names, [0, 1], colors):

        plt.scatter(
            L[y == i, 0], 
            L[y == i, 2], 
            c=color, 
            alpha=0.5,
            label=label
        )

    plt.xlabel(cancer.feature_names[0])
    plt.ylabel(cancer.feature_names[2])
    plt.legend()

    plt.title(f"Podział klas dla kernela '{kernel}' i C={C}")

    plt.show()

    y = clf.predict(X)
    clf.fit(X, y)

    for label, i, color in zip(cancer.target_names, [0, 1], colors):

        plt.scatter(
            L[y == i, 0], 
            L[y == i, 2], 
            c=color, 
            alpha=0.5,
            label=label
        )

    plt.xlabel(cancer.feature_names[0])
    plt.ylabel(cancer.feature_names[2])
    plt.legend()

    plt.title(f"Podział klas dla kernela '{kernel}' i C={C} po zmianie wektora klas na wynik predykcji")

    plt.show()

