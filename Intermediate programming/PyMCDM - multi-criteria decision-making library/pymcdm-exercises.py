import numpy as np

from pymcdm.methods import TOPSIS, COPRAS
from pymcdm.helpers import rankdata
from pymcdm.weights import entropy_weights
from pymcdm.correlations import weighted_spearman, rank_similarity_coef
from pymcdm.normalizations import minmax_normalization


# Function returns the best result from matrix
def print_best(matrix, prefs):
    return list(matrix[list(prefs).index(prefs.max())])


## 1
print('\n1)')
# Problem: 
# Selection of a used car from 5 alternatives based on 5 criteria
#   - price
#   - engine capacity (cm3)
#   - power (KM)
#   - year of production
#   - mileage

# Matrix (5 preferences, 5 alternatives)
matrix = np.array([
    [75000, 1998, 180, 2019, 153000],
    [26000, 1599, 105, 2013, 268000],
    [125000, 1800, 175, 2021, 33000],
    [13500, 1899, 125, 2008, 225000],
    [250000, 3199, 250, 2021, 145000]
], dtype='int')

# Subjective weights vector and type of criteria
weights = np.array([0.3, 0.1, 0.2, 0.1, 0.3])
types = np.array([-1, 1, 1, 1, -1])

# Calculation of preference values and positional ranking
topsis = TOPSIS()

prefs = topsis(matrix, weights, types)
ranks = rankdata(prefs, reverse=True)

print('\nWartości preferencji:', prefs)
print('Ranking pozycyjny:', ranks)
print('Najlepszy wybór:', print_best(matrix, prefs))

## 2
print('\n2)')
# Problem:
# Selection of yogurt based on the content of protein, fat and carbohydrates per 100g of product in order:
#   - price
#   - product weght
#   - protein content/100g
#   - fat content/100g
#   - carbohydrates content/100g

# Matrix (5 preferences, 6 alternatives)
matrix = np.array([
    [3.99, 300, 9, 6, 11],
    [4.50, 400, 11, 5, 7],
    [4.99, 333, 10, 7, 9],
    [3.19, 300, 6, 9, 12],
    [5.29, 350, 12, 6, 9],
    [5.99, 330, 10, 2, 5]
], dtype='float')

# Weight vectors and criteria types:
weights_obj = entropy_weights(matrix)
weights_sub = np.array([0.3, 0.2, 0.3, 0.1, 0.1])
types = np.array([-1, 1, 1, -1, -1])

# Calculation of preferences and positional rankings (TOPSIS)
prefs_obj = topsis(matrix, weights_obj, types)
prefs_sub = topsis(matrix, weights_sub, types)

ranks_obj = rankdata(prefs_obj, reverse=True)
ranks_sub = rankdata(prefs_sub, reverse=True)

# Calculating Correlations for Preferences and Position Rankings (TOPSIS)
pref_similarity = weighted_spearman(prefs_obj, prefs_sub)
rank_similarity = rank_similarity_coef(ranks_obj, ranks_sub)

print('\nObiektywne wartości preferencji (TOPSIS):', prefs_obj)
print('Obiektywny ranking pozycyjny (TOPSIS):', ranks_obj)
print('Najlepszy wybór (obiektywne wagi):', print_best(matrix, prefs_obj))

print('\nSubiektywne wartości preferencji (TOPSIS):', prefs_sub)
print('Subiektywny ranking pozycyjny (TOPSIS):', ranks_sub)
print('Najlepszy wybór (subiektywne wagi):', print_best(matrix, prefs_sub))

print('\nKorelacja między wartościami preferencji (TOPSIS):', pref_similarity)
print('Korelacja między pozycjami w rankingu (TOPSIS):', rank_similarity)

## 3
print('\n3)')
# Problem:
# Selection of the printer based on the parameters in the following order:
#   - price
#   - printing quantity/min.
#   - cartridge capacity (ml)
#   - cartridge price

# Matrix (4 preferences, 6 alternatives)
matrix_non = np.array([
    [999, 150, 200, 130],
    [1099, 130, 230, 150],
    [789, 100, 200, 109],
    [2998, 250, 300, 200],
    [1199, 185, 185, 185],
    [679, 90, 150, 90]
], dtype='float')

# Data normalization:
matrix = minmax_normalization(matrix_non)
print('\nZnormalizowane dane:\n', matrix)

# Weight vectors and criteria types:
weights_obj = entropy_weights(matrix)
weights_sub = np.array([0.3, 0.2, 0.2, 0.3])
types = np.array([-1, 1, 1, -1])

# Calculation of preferences and positional rankings (TOPSIS)
prefs_obj = topsis(matrix, weights_obj, types)
prefs_sub = topsis(matrix, weights_sub, types)

ranks_obj = rankdata(prefs_obj, reverse=True)
ranks_sub = rankdata(prefs_sub, reverse=True)

# Calculating Correlations for Preferences and Position Rankings (TOPSIS)
pref_similarity = weighted_spearman(prefs_obj, prefs_sub)
rank_similarity = rank_similarity_coef(ranks_obj, ranks_sub)

print('\nObiektywne wartości preferencji (TOPSIS):', prefs_obj)
print('Obiektywny ranking pozycyjny (TOPSIS):', ranks_obj)
print('Najlepszy wybór (obiektywne wagi):', print_best(matrix_non, prefs_obj))

print('\nSubiektywne wartości preferencji (TOPSIS):', prefs_sub)
print('Subiektywny ranking pozycyjny (TOPSIS):', ranks_sub)
print('Najlepszy wybór (subiektywne wagi):', print_best(matrix_non, prefs_sub))

print('\nKorelacja między wartościami preferencji (TOPSIS):', pref_similarity)
print('Korelacja między pozycjami w rankingu (TOPSIS):', rank_similarity)

copras = COPRAS()

# Calculation of Preferences (COPRAS)
prefs_top_obj, prefs_top_sub = prefs_obj, prefs_sub
prefs_cop_obj = copras(matrix, weights_obj, types)
prefs_cop_sub = copras(matrix, weights_sub, types)

# Correlation Calculation for Preferences (COPRAS)
pref_similarity = weighted_spearman(prefs_cop_obj, prefs_cop_sub)

# Calculation of correlations for TOPSIS and COPRAS preferences
pref_obj_similarity = weighted_spearman(prefs_top_obj, prefs_cop_obj)
pref_sub_similarity = weighted_spearman(prefs_top_sub, prefs_cop_sub)

# Calculating Position Rankings (COPRAS)
ranks_top_obj, ranks_top_sub = ranks_obj, ranks_sub
ranks_cop_obj = rankdata(prefs_cop_obj, reverse=True)
ranks_cop_sub = rankdata(prefs_cop_sub, reverse=True)

# Correlation Calculation for Position Rankings (COPRAS)
rank_similarity = rank_similarity_coef(ranks_cop_obj, ranks_cop_sub)

# Calculation of correlations for TOPSIS and COPRAS position rankings
rank_obj_similarity = rank_similarity_coef(ranks_top_obj, ranks_cop_obj)
rank_sub_similarity = rank_similarity_coef(ranks_top_sub, ranks_cop_sub)

print('\nObiektywne wartości preferencji (COPRAS):', prefs_cop_obj)
print('Obiektywny ranking pozycyjny (COPRAS):', ranks_cop_obj)
print('Najlepszy wybór (obiektywne wagi):', print_best(matrix_non, prefs_cop_obj))

print('\nSubiektywne wartości preferencji (COPRAS):', prefs_cop_sub)
print('Subiektywny ranking pozycyjny (COPRAS):', ranks_cop_sub)
print('Najlepszy wybór (subiektywne wagi):', print_best(matrix_non, prefs_cop_sub))

print('\nKorelacja między wartościami preferencji (COPRAS):', pref_similarity)
print('Korelacja między pozycjami w rankingu (COPRAS):', rank_similarity)

print('\nKorelacja między wartościami preferencji '
      'dla metod TOPSIS i COPRAS (obiektywne wagi):', pref_obj_similarity)
print('Korelacja między wartościami preferencji '
      'dla metod TOPSIS i COPRAS (subiektywne wagi):', pref_sub_similarity)

print('\nKorelacja między pozycjami w rankingu '
      'dla metod TOPSIS i COPRAS (obiektywne wagi):', rank_obj_similarity)
print('Korelacja między pozycjami w rankingu '
      'dla metod TOPSIS i COPRAS (subiektywne wagi):', rank_sub_similarity)


# After analyzing activities with and without data normalization
# the best choices remained the same.