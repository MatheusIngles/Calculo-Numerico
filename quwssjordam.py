

def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0])

    for i in range(n):

        if augMat[i][i]==0:
            for j in range(i + 1,n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                    break
                else:
                    raise ValueError("Matriz Singular!")

        if augMat[i][i]:
            divisor = augMat[i][i]
            for k in range(n):
                augMat[i][k] /= divisor
        else:
            pass

        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:
                pass
    
    print(augMat)

matriz = [[3, 2,-4,  3],
          [2, 3, 3, 15],
          [5,-3, 1, 14]]

if __name__ == "__main__": 
    GaussJordanMethod(matriz)