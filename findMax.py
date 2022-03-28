import numpy as np

## Generating a random matrix to work with
matrix = np.random.random_integers(0, 9, size = (5,5))  

rows, columns = matrix.shape
maxArray = ["max"]*columns

# Offsetting by 1 for indexing
row = rows-1
column = columns-1

# While loop to iterate through columns and populate maxArray
while(column >= 0):

    colMax = 0

    # While loop to iterate through rows and find max
    # This isn't the most efficient solution
    while(row >= 0):
        
        if(matrix[row][column] > colMax):
            colMax = matrix[row][column]
            maxRow = row
            print(colMax)
        row = row - 1
    
    
    maxArray[column] = colMax
    # This ensures that the next iteration will only search until last maxRow
    row = maxRow 

    column = column-1 


print(maxArray)

