def get_matrix():
    matrices = {
        "identity_matrix": [
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3]
        ],
        "column_of_zeros": [
            [1, 0, 3, 4],
            [4, 0, 6, 5],
            [4, 0, 5, 2]
        ],
        "multiple_row_swaps": [
            [0, 1, 2, 4],
            [0, 0, 3, 5],
            [4, 5, 6, 6]
        ],
        "singular_matrix": [
            [1, 2, 3, 4],
            [2, 4, 6, 6],
            [4, 5, 6, 6]
        ],
        "large_matrix": [
            [1, 2, 3, 4, 5, 6, 7, 8, 2, 36],
            [2, 4, 6, 8, 10, 12, 14, 16, 4, 76],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
            [0, 2, 0, 4, 0, 6, 0, 8, 0, 20],
            [3, 0, 3, 0, 3, 0, 3, 0, 1, 13],
            [0, 0, 2, 0, 4, 0, 6, 0, 0, 12],
            [0, 6, 0, 3, 0, 9, 0, 12, 0, 30],
            [2, 2, 2, 2, 2, 2, 2, 2, 0, 16],
            [1, 3, 5, 7, 9, 11, 13, 15, 3, 67]

        ],
        "identity_matrix_echelon": [
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3]
        ],
        "column_of_zeros_echelon": [
            [1, 0, 3, 4],
            [0, 0, 1, round(11/6, 2)],
            [0, 0, 0, 1]
        ],
        "multiple_row_swaps_echelon": [
            [1, 5/4, 6/4, 6/4],
            [0, 1, 2, 4],
            [0, 0, 1, round(5/3, 2)]
        ],
        "singular_matrix_echelon": [
            [1, 2, 3, 4],
            [0, 1, 2, round(10/3, 2)],
            [0, 0, 0, 1]
        ],

        "large_matrix_echelon": [
            [1, 2, 3, 4, 5, 6, 7, 8, 2, 36],
            [0, 1, 2, 3, 4, 5, 6, 7, 1, 27],
            [0, 0, 1, 0.5, 2, 1, 3, 6/4, 0.5, 34/4],
            [0, 0, 0, 1, 0, 2, 0, 3, round(-2/3, 2), round(16/3, 2)],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1, 0, round(15/9, 2), round(-6/9, 2), 2],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, -1/5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ],
        "identity_matrix_reduced_echelon": [
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3]
        ],
        "column_of_zeros_reduced_echelon": [
            [1, 0, 0, -1.49],
            [0, 0, 1, 1.83],
            [0, 0, 0, 1]
        ],
        "multiple_row_swaps_reduced_echelon": [
            [1, 0, 0, -1.83],
            [0, 1, 0, 0.66],
            [0, 0, 1, 1.67]
        ],
        "singular_matrix_reduced_echelon": [
            [1, 0, -1, -2.66],
            [0, 1, 2, 3.33],
            [0, 0, 0, 1]
        ],
        "large_matrix_reduced_echelon": [
            [1, 0, 0, 0, -1, 0, -2, 0, 0, -1.61],
            [0, 1, 0, 0, 0, 0, 0, -0.3, 0, 1.47],
            [0, 0, 1, 0, 2, 0, 3, 0, 0, 6],
            [0, 0, 0, 1, 0, 0, 0, -0.33, 0, 1.46],
            [0, 0, 0, 0, 0, 1, 0, 1.67, 0, 1.87],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, -0.2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "mat1":[
            [1, 2, 0, 0, 0, 0, 3],
            [2, 3, 1, 0, 0, 0, 6],
            [0, 3, 4, 1, 6, 6, 20],
            [0, 0, 0, 0, 2, 1, 3],
            [1, 0, 0, 0, 0, 6, 7],
            [0, 0, 0, 1, 0, 9, 10]
        ],
        "mat1_reducedechelon":[
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1]
        ]
    }
    return matrices
