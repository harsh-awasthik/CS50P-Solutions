import project as p
from matrices import get_matrix
import numpy as np

mat = get_matrix()

def test_get_sampleaugmat():
    assert p.get_sampleaugmat(3,1) == [["a1", "b1", "c1", "B1"]]
    assert p.get_sampleaugmat(3,3) == [["a1", "b1", "c1", "B1"],
                                             ["a2", "b2", "c2", "B2"],
                                             ["a3", "b3", "c3", "B3"]]


def test_convert_echelonform():
    assert np.allclose(p.convert_echelonForm(mat["identity_matrix"], 3), mat["identity_matrix_echelon"])
    assert np.allclose(p.convert_echelonForm(mat["column_of_zeros"], 3), mat["column_of_zeros_echelon"])
    assert np.allclose(p.convert_echelonForm(mat["multiple_row_swaps"], 3), mat["multiple_row_swaps_echelon"])
    assert np.allclose(p.convert_echelonForm(mat["singular_matrix"], 3), mat["singular_matrix_echelon"])
    assert np.allclose(p.convert_echelonForm(mat["large_matrix"], 9), mat["large_matrix_echelon"], atol = 1e-1)


def test_convert_reducedechelon():
    assert np.allclose(p.convert_reducedechelon(mat["identity_matrix_echelon"]), mat["identity_matrix_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat["column_of_zeros_echelon"]), mat["column_of_zeros_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat["multiple_row_swaps_echelon"]), mat["multiple_row_swaps_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat["singular_matrix_echelon"]), mat["singular_matrix_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat["large_matrix_echelon"]), mat["large_matrix_reduced_echelon"], atol = 1e-1)
    assert np.allclose(p.convert_reducedechelon(p.convert_echelonForm(mat['mat1'], 6)), mat['mat1_reducedechelon'], atol = 1e-1)


print(...)

def test_get_uniquesolutions():
    ...
