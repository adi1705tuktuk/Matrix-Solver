def rref(matrix):
    row = len(matrix)
    col = len(matrix[0])
    r = 0
    c = 0
    pivot_positions = []
    while r < row and c < col:
        # find the pivot in the current column
        pivot = r
        for i in range(r+1, row):
            if abs(matrix[i][c]) > abs(matrix[pivot][c]):
                pivot = i
        if matrix[pivot][c] == 0:
            c += 1
            continue
        # swap the pivot row with the current row
        matrix[pivot], matrix[r] = matrix[r], matrix[pivot]
        pivot_positions.append((r, c))
        # divide the current row by the pivot element
        pivot_val = matrix[r][c]
        for j in range(c, col):
            matrix[r][j] /= pivot_val
        # subtract the current row from the other rows to make the pivot element 0
        for i in range(row):
            if i != r:
                factor = matrix[i][c]
                for j in range(c, col):
                    matrix[i][j] -= factor * matrix[r][j]
        r += 1
        c += 1
    return matrix, pivot_positions


# Input size of matrix
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

# Input matrix A
A = [[int(input("Enter entry for A["+str(i+1)+"]["+str(j+1)+"]: ")) for j in range(m)] for i in range(n)]

rref_matrix, pivot_positions = rref(A)
for i in range(n):
    for j in range(m):
        if rref_matrix[i][j]==-0:
            rref_matrix[i][j]=0
print()
print("PIVOT POSITIONS:")
print(pivot_positions)
print("RREF:")
for row in rref_matrix:
    print(row)
    

def main():
    M=rref_matrix
    #free variable
    free_vars=[]
    vars=[]
    for j in pivot_positions:
        vars.append(j[1])
    for i in range(m):
        if i not in vars:
            free_vars.append(i)

    trash=[0]*m
    sol={}
    pivot_positionsy=[y for x,y in pivot_positions]
    pivot_positionsx=[x for x,y in pivot_positions]
    for i in free_vars:
        sol [i]=trash.copy()
    for q,i in enumerate(free_vars):
        for j in range(m):
            if j in pivot_positionsy:
                k=pivot_positionsy.index(j)
                kx=pivot_positionsx[k]
                sol[i][j]=-rref_matrix[kx][i]
            elif j!=i :
                sol[i][j]=0
            else :
                sol[i][j]=1  

#Printing of parametric solution
    print("\n SOLUTION:")
    s=''
    for i in sol :
        s+='x_'+str(i+1)+'*'+str(sol[i])+'+'
    print(s.strip('+'))

main()

