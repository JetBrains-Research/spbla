import random
import pyspbla
from tests import test_transitive_closure


def lists_to_pairs(rows, cols):
    pairs = set()
    for i in range(len(rows)):
        pairs.add((rows[i], cols[i]))

    return pairs


def gen_matrix_data(size, seed):
    m = size[0]
    n = size[1]

    values = set()
    rows = list()
    cols = list()

    for _ in range(seed):
        i = random.randrange(0, m)
        j = random.randrange(0, n)
        values.add((i, j))

    for (i, j) in values:
        rows.append(i)
        cols.append(j)

    return rows, cols, len(values)


def gen_matrix(size, seed):
    rows, cols, nvals = gen_matrix_data(size, seed)
    mat = pyspbla.Matrix.empty(size)
    mat.build(rows, cols, no_duplicates=True)
    return mat, lists_to_pairs(rows, cols)


dim = (10, 10)
to_gen = 50

# pyspbla.setup_logger(pyspbla.get_default_log_name())
a, a_set = gen_matrix(dim, to_gen)
b, b_set = gen_matrix(dim, to_gen)

print("Matrix a din:", a.shape, "values count:", a.nvals)
print("Matrix b dim:", b.shape, "values count:", b.nvals)

r = a.ewiseadd(b, time_check=True)
c = a.mxm(b, accumulate=True)
print(a, b, c, sep="\n")

print("Matrix r values count:", r.nvals)

rows, cols = r.to_lists()
res_set = lists_to_pairs(rows, cols)

print(b_set.union(a_set) == res_set)

t = test_transitive_closure.transitive_closure(a)

print(a.nvals, a.shape)
print(t.nvals, t.shape)

rows = [0, 1, 2, 3, 3, 3, 3]
cols = [0, 1, 2, 0, 1, 2, 3]

matrix = pyspbla.Matrix.from_lists((4, 4), rows, cols, is_sorted=True)
transposed = matrix.transpose()
submatrix = matrix[0:3, 1:]
rows, cols = transposed.to_lists()

print([(rows[i], cols[i]) for i in range(transposed.nvals)])

print(matrix)
print(transposed)
print(submatrix)

print(list(iter(matrix)))

matrix = pyspbla.Matrix.from_lists((4, 4), [0, 1, 2, 3], [0, 1, 2, 0], is_sorted=True)
print(matrix.extract_matrix(0, 1, shape=(3, 3)))

matrix = pyspbla.Matrix.empty(shape=(4, 4))
matrix[0, 0] = True
matrix[1, 1] = True
matrix[2, 3] = True
matrix[3, 1] = True
print(matrix)

matrix = pyspbla.Matrix.from_lists((4, 4), [0, 1, 2, 2], [0, 1, 0, 2])
print(matrix.reduce())

a = pyspbla.Matrix.empty(shape=(4, 4))
a[0, 0] = True
a[0, 3] = True
print(a)
a = a.ewiseadd(a.transpose())
print(a)
a[3, 3] = True
print(a)

a = pyspbla.Matrix.empty(shape=(4, 4))
a[0, 0] = True
a[1, 3] = True
a[1, 0] = True
a[2, 2] = True
vals = a.to_list()
print(vals)
print(a.equals(a))

matrix = pyspbla.Matrix.generate(shape=(4, 4), density=0.5)
print(matrix)
