import string
alphabets = string.ascii_letters
def seperate_list(list1, n):
    for i in range(0, len(list1), n):
        each_character = list1[i: n+i]

        if len(each_character) < n:
            each_character = each_character + \
                [None for y in range(n-len(each_character))]
        yield each_character
def transposition(text, key):
    c = key
    A = []
    B = []
    for char in text:
        A.append(char)
    matrix = list(seperate_list(A, key))
    matrix1 = matrix
    r = len(matrix)
    # print(r)
    print(matrix)
    print("------------------------------------------------")
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()
    print("-------------------------------------------------")
    for j in range(c):
        for i in range(r):
            if matrix[i][j] is not None:
                B.append(matrix[i][j])
    encrypt = "".join(B)
    return encrypt, matrix

plain_text = input("Enter the Text to encode : ")
transpose_key = int(input("Enter the tranpose key: "))
encrypt, matrix = transposition(plain_text, transpose_key)
print("Product Cipher : ", encrypt)
