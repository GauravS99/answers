# I will assume valid input, that is if matrix m_1 and matrix m_2 are next to each other in a, then
# m_1 x m_2 is a valid operation

# I understand that this solution will not compete with numpy's or some other major package's solution,
# and that there are optimizations if we know the matricies are sparse

# let n = the number of matricies
# let m = the largest dimension in any matrix
# Time Complexity: O(nm^3)
# Space Complexity: O(m^2)


def multiply_matrix(matrix_A, matrix_B):
    result = []

    for i in range(len(matrix_A)): # for clarity and to be explicit, initialize with Nones
        result.append([None] * len(matrix_B[0]))

    for row_A in range(len(matrix_A)):
        for col_B in range(len(matrix_B[0])):
            accumulator = 0
            for col_A in range(len(matrix_A[row_A])):
                accumulator += (matrix_A[row_A][col_A] * matrix_B[col_A][col_B])
            result[row_A][col_B] = accumulator
    
    return result

def multiply_matrices(a):
    """
    Given a list/vector of 2D matrices as arrays, multiply them together in the same order and return the resulting matrix as a new array.  You may not use any libraries to perform the multiplication for you.
    """
    num_matricies = len(a)
    if (num_matricies == 0):
        return [] 
    elif (num_matricies == 1):
        return a[0]

    temp = a[0]
    for i in range(1, num_matricies):
        temp = multiply_matrix(temp, a[i])
    
    return temp

if __name__ == "__main__":
    matrix_A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_B = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

    matrix_C = [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
    ]
    # print(multiply_matrix(matrix_A, matrix_B))
    print(multiply_matrices([matrix_A, matrix_B, matrix_C]))