# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) < 2:
        return (numbers[0], None) if numbers else (None, None)

    max_val = second_max = float('-inf')

    for num in numbers:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num != max_val:
            second_max = num

    return (max_val, second_max)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort() 
    return unique_numbers
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num 
        result.append(total) 
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_row = [row[i] for row in matrix] 
        transposed.append(new_row)
    return transposed

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(numbers, N):
    result = []
    for i in range(0, len(numbers), N):
        result.append(numbers[i])
    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0
    for i in range(len(list1)):
        total += list1[i] * list2[i]
    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
         return("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            row_result.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(row_result)
    
    return result