import project as p
from matrices import get_mat_ef_ref, get_infsolmat
import numpy as np

mat1 = get_mat_ef_ref()
mat2 = get_infsolmat()

def test_get_sampleaugmat():
    assert p.get_sampleaugmat(3,1) == [["a1", "b1", "c1", "B1"]]
    assert p.get_sampleaugmat(3,3) == [["a1", "b1", "c1", "B1"],
                                             ["a2", "b2", "c2", "B2"],
                                             ["a3", "b3", "c3", "B3"]]


def test_convert_echelonform():
    assert np.allclose(p.convert_echelonForm(mat1["identity_matrix"], 3), mat1["identity_matrix_echelon"])
    assert np.allclose(p.convert_echelonForm(mat1["column_of_zeros"], 3), mat1["column_of_zeros_echelon"])
    assert np.allclose(p.convert_echelonForm(mat1["multiple_row_swaps"], 3), mat1["multiple_row_swaps_echelon"])
    assert np.allclose(p.convert_echelonForm(mat1["singular_matrix"], 3), mat1["singular_matrix_echelon"])
    assert np.allclose(p.convert_echelonForm(mat1["large_matrix"], 9), mat1["large_matrix_echelon"], atol = 1e-1)


def test_convert_reducedechelon():
    assert np.allclose(p.convert_reducedechelon(mat1["identity_matrix_echelon"]), mat1["identity_matrix_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat1["column_of_zeros_echelon"]), mat1["column_of_zeros_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat1["multiple_row_swaps_echelon"]), mat1["multiple_row_swaps_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat1["singular_matrix_echelon"]), mat1["singular_matrix_reduced_echelon"])
    assert np.allclose(p.convert_reducedechelon(mat1["large_matrix_echelon"]), mat1["large_matrix_reduced_echelon"], atol = 1e-1)
    assert np.allclose(p.convert_reducedechelon(p.convert_echelonForm(mat1['mat1'], 6)), mat1['mat1_reducedechelon'], atol = 1e-1)


def test_unique_solution():
    assert p.get_uniquesolutions([1, 0, 3]) == {
                                                "x1": "1.00",
                                                "x2": "0.00",
                                                "x3": "3.00"
                                                }
    assert p.get_uniquesolutions([1.4564, 0.65, -3.9999]) == {
                                                "x1": "1.46",
                                                "x2": "0.65",
                                                "x3": "-4.00"
                                                }

def test_find_infsoln():
    assert p.find_infsoln(mat2["mat11"], mat2["mat12"]) == mat2["mat13"]
    assert p.find_infsoln(mat2["mat21"], mat2["mat22"]) == mat2["mat23"]
    assert p.find_infsoln(mat2["mat31"], mat2["mat32"]) == mat2["mat33"]


def test_get_uniquesolutions():
    ...
