# Project is to create solutions of N equations using echelon form
import sys


def main():
    print("------------------------------")
    variables = get_int("Enter the Number of Variables: ")  # 'variables' is the number of variables
    print("------------------------------")
    eq = variables + 1
    while (eq > variables):
        eq = get_int("Enter the Number of Equations.(less or equal to the no of Variables): ")  # 'eq' is the number of equations

    print("------------------------------")
    print("Equations must be of the form \"ax1 + bx2 + cx3 .... = B\" ")

    print("Your Matrix should look like this.")
    # Printing sample aug_mat for ease of users
    sample = get_sampleaugmat(variables, eq)
    [print(a) for a in sample]
    print("------------------------------")

    aug_mat = get_augmat(variables, eq)  # get augments matrix

    #Open this if you want to see Augmented Matrix
    '''print("Augmented Matrix")
    for i in aug_mat:
        print(i)
    print()'''

    # Converting the augmented matrix into upper triangular matrix (i.e echelon Form)
    echelon_mat = convert_echelonForm(aug_mat, eq)

    #Open this if You want to see echelon Form
    '''print("echelon Form")
    for i in echelon_mat:
        print(i)
    print()'''


    # Converting to reduced echelon Form
    ref_mat = convert_reducedechelon(echelon_mat)

    #Open this if You want to see reduced echelon Form
    '''print("reduced echelon Form")
    for i in ref_mat:
        print(i)
    print()'''

    # Converitng aug_mat to the form Ax + b
    mat_a, mat_b = [], []
    for a in ref_mat:
        mat_a.append(a[:-1])
        mat_b.append(a[-1])

    #Open this if You want to Observe Mat_A or mat_b of the form Ax = b
    '''print("mat_a")
    for i in mat_a:
        print(i)
    print()
    print("mat_b", mat_b)'''

    print("------------------------------")  # adding a line

    # Checking for NO solution and Infinite solution
    inf_soln = False
    for i in range(variables):
        is_empty = True
        for j in mat_a[i]:
            if j != 0:
                is_empty = False
        if is_empty:
            if mat_b[i] != 0:
                sys.exit("NO SOLUTION\n------------------------------")  # Checking for no-solution and printing it
            else:
                inf_soln = True

    # Printing Unique solution
    if not inf_soln:
        print("UNIQUE SOLUTION")
        solns = get_uniquesolutions(mat_b)

    # to find solutions if system has infinite solutions
    if inf_soln:
        print("INFINITE SOLUTIONS")
        solns = find_infsoln(mat_a, mat_b)

    #Printing Solutions
    for keys in sorted(solns):
        print(f"{keys} = {solns[keys]}")

    print("------------------------------")  # adding a line


def get_int(promt):  # function for gettting a integer input
    while True:
        try:
            n = int(input(promt))
            return n
        except ValueError:
            print("Enter a Numerical Value")
            pass


def get_float(promt):  # function for gettting a float input
    while True:
        try:
            f = float(input(promt))
            return f
        except ValueError:
            print("Enter a Numerical Value")
            pass


def get_sampleaugmat(variables, eq):
    mat = []
    for i in range(1, eq+1):
        eq = []
        for j in range(1, variables+1):
            eq.append(f"{chr(96+j)}{i}")
        eq.append(f"B{i}")
        mat.append(eq)
    return mat


def get_augmat(variables, eq):
    aug_mat = []
    for i in range(1, eq+1):
        equation = []
        is_allzeroinput = True

        while is_allzeroinput:
            for j in range(1, variables+1):
                cons = get_float(f"Enter {chr(96+j)}{i}: ")
                if cons != 0:
                    is_allzeroinput = False
                equation.append(cons)
            if is_allzeroinput:
                print("Equation Can't Be Blank")

        equation.append(get_float(f"Enter B{i}: "))
        aug_mat.append(equation)

    if eq < variables:
        n = variables - eq
        for i in range(n):
            T = []
            for j in range(variables + 1):
                T.append(0)
            aug_mat.append(T)

    return aug_mat


def convert_echelonForm(aug_mat, eq):
    c = 0
    for r in range(eq):

        while c < len(aug_mat[0]) - 1 and aug_mat[r][c] == 0:  # If there is 0 rather than a number
            for s in range(r + 1, eq):
                if aug_mat[s][c] != 0:
                    aug_mat[s], aug_mat[r] = aug_mat[r], aug_mat[s]
                    break
            else:
                c += 1

        if c < len(aug_mat[0]):
            if aug_mat[r][c] != 0:
                temp = []
                for j in aug_mat[r]:
                    temp.append(round(j/aug_mat[r][c], 2))
                aug_mat[r] = temp

                for i in range(r + 1, eq):
                    factor = aug_mat[i][c]
                    temp = [a - factor*b for a, b in zip(aug_mat[i], aug_mat[r])]
                    aug_mat[i] = temp

        c += 1

    for i in range(len(aug_mat)):
        for j in range(len(aug_mat[i])):
            aug_mat[i][j] = round(aug_mat[i][j], 2)

    return aug_mat


def convert_reducedechelon(echelon_mat):
    for row in range(len(echelon_mat)-1, -1, -1):
        for col in range(row, len(echelon_mat)):
            if echelon_mat[row][col] == 1:
                break
        else:
            continue

        for i in range(1, row+1):
            factor = echelon_mat[row - i][col]
            echelon_mat[row-i] = [a - factor*b for a, b in zip(echelon_mat[row-i], echelon_mat[row])]

    for i in range(len(echelon_mat)):
        for j in range(len(echelon_mat[i])):
            echelon_mat[i][j] = round(echelon_mat[i][j], 2)

    return echelon_mat


def get_uniquesolutions(mat_b):
    sol = {}
    v = len(mat_b)
    for r in range(v):
        sol[f"x{r+1}"] = f"{mat_b[r] :.02f}"
    return sol

def find_infsoln(mat_a, mat_b):
    solutions = {}
    v = len(mat_b) #finding the number of variables

    #To find Dependent Varibles
    dep_var = []
    for i in range(v-1, -1, -1):
        for j in range(v-1, -1, -1):
            if mat_a[i][j] == 1:
                dep_var.append(j)
                break

    #To find Independent Variables
    ind_var = []
    [ind_var.append(i) for i in range(v) if i not in dep_var]

    #To add Independent Variables to solns
    ind_x = []
    for r in ind_var:
        ind_x.append(f"x{r + 1}")
        solutions[f"x{r + 1}"] = f" x{r + 1}"
    print(f"Let the Independent Variables be {','.join(ind_x)} respectively.")

    #print(ind_var, "infinite solutions")

    #To add Dependent Variables to solns
    for i in sorted(dep_var):
        temp = f"{mat_b[i] : .02f}"

        for ind in range(len(ind_var)):
            if mat_a[i][ind_var[ind]] != 0:
                temp += f" {-1 * mat_a[i][ind_var[ind]] : .02f}{ind_x[ind]}"

        solutions[f"x{i+1}"] = temp

    return solutions


if __name__ == "__main__":
    main()
