# I will assume valid input, that is if matrix m_1 and matrix m_2 are next to each other in a, then
# m_1 x m_2 is a valid operation

# I understand that this solution will not compete with numpy's or some other major package's solution,
# and that there are optimizations if we know the matricies are sparse

# let n = the number of matricies
# let m = the largest dimension in any matrix
# Time Complexity: O(nm^3)
# Space Complexity: O(m^2)


#memo contains tuples of form (operations, first_multiplication_index)
def least_operations(matrix_arr, left, right, memo):
    if (left == right):
        return (0, left)

    if (memo[left][right - left - 1] is not None):
        return memo[left][right - left - 1]       

    min_op = None
    for i in range(left, right):
        if (memo[i][0] is not None):
            operations = memo[i][0][0]
        else:
            operations =  len(matrix_arr[i]) * len(matrix_arr[i][0]) * len(matrix_arr[i + 1][0])

        total_op = operations + least_operations(matrix_arr, left, i, memo)[0] + least_operations(matrix_arr, i + 1, right, memo)[0] 
        if (min_op is None or total_op < min_op[0]):
            min_op = (total_op, i)
    
    memo[left][right - left - 1] = min_op
    return min_op    



def multiply_matrix_recursive(matricies, left, right, memo):

    if(left == right):
        return matricies[left]

    index = memo[left][right - left - 1][1]
    matrix_A = multiply_matrix_recursive(matricies, left, index, memo)
    matrix_B = multiply_matrix_recursive(matricies, index + 1, right, memo)

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
    #setup this matrix for memoization
    memo = []
    for i in range (len(a) - 1):
        memo.append([None] * (len(a) - i - 1))

    num_matricies = len(a)
    if (num_matricies == 0):
        return [] 
    elif (num_matricies == 1):
        return a[0]

    least_operations(a,  0, len(a) - 1, memo)

    return multiply_matrix_recursive(a, 0, len(a) - 1, memo)

if __name__ == "__main__":
    matrix_A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_B = [
        [1,2,3,4, 3],
        [5,6,7,8, 3],
        [9,10,11,12, 3],
        [1,1,1,1,1]
    ]

    matrix_C = [
        [1],
        [3],
        [5],
        [7],
        [2]
    ]
    # print(multiply_matrix(matrix_A, matrix_B))
    print(multiply_matrices([matrix_A, matrix_B, matrix_C]))