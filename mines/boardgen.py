# boardgen.py
# generates n * m minesweeper boards
# Cole Frauzel
# 2022-09-24 last updated 2022-09-24

import numpy as np

# Starting parameters ---------------------------------------------------------
rs = 20     # row count
cs = 20     # column count
ms = 39     # mine count

# Generate the mine matrix ----------------------------------------------------
mine_mat = np.zeros(rs*cs, dtype=np.uint8)
    # Begin with an array of rs*cs zeros

mine_mat[np.random.choice(np.arange(rs*cs), ms, replace=False)] = 1
    # Randomly select ms numbers from 0 to (rs*cs)-1, without duplicates
    # Each selected number corresponds to an element in the boards array
    # Set the selected elements to 1; these are the mine locations 

mine_mat = np.reshape(mine_mat, (rs,cs))
    # Reshape the 1D array into a matrix of rs rows and cs columns

print(mine_mat)

# Generate a map of neighbouring mines ----------------------------------------
mcount_mat = np.zeros(np.shape(mine_mat), dtype=np.uint8)

mine_iter = np.nditer(mine_mat, flags=['multi_index']) # matrix made iterable

for i in mine_iter:
    rx, cx = ix = mine_iter.multi_index # extract the 2D index of this element

    # Get the corners of the area to slice around this element
    r1, r2 = max(0, rx-1), min(rs-1, rx+1) + 1
        # max/min functions are for checking at the edges of the matrix
        # r1 = rx-1 if rx-1 is positive, zero otherwise
        # r2 = rx+1 if rx-1 is less than rs-1, rs-1 otherwise
    c1, c2 = max(0, cx-1), min(cs-1, cx+1) + 1
        # same method is used for the columns
        # r2 and c2 are +1 because upper bounds of slices have exclusive
        # indexing, so we'll need to add 1 in any case.

    slice_sum = mine_mat[r1:r2, c1:c2].sum() - mine_mat[ix]
        # Sum all the 1's in the selected slice of the mine matrix
        # Subtract the element itself so that it's not included in the sum
    
    mcount_mat[ix] = slice_sum

print(mcount_mat)


# Preview the board -----------------------------------------------------------
print("\n\n\n")
print('+','- '*(rs-1),'+')
for i in range(rs):
    print('|',end='')
    for j in range(cs):        
        if mine_mat[i,j]==1:
            print("X",end=' ')
        else:
            if mcount_mat[i,j]==0:
                print(" ",end=' ')
            else:
                print(mcount_mat[i,j],end=' ')
    print('|')  
print('+','- '*(rs-1),'+')
print("\nrows:",rs,"| cols:",cs,"| mines:",ms)