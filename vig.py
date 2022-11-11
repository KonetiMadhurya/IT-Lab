string = str(input("Enter plain text : "))
string = string.upper()
keyword = str(input("Enter key : "))
keyword = keyword.upper()

list1 = []
for ia in string:
    if ia == " ":
        temp = ""
        list1.append(temp)
    else:
        temp = ia
        list1.append(temp)
text = "".join(list1)

def generatekey(string,key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return("".join(key))

def encryption(string,key):
    text = []
    for i in range(len(string)):
        x = (ord(string[i])+ord(key[i])) % 26
        x+=ord('A')
        text.append(chr(x))
    return ("".join(text))

key = generatekey(text, keyword)
encrypt = encryption(text, key)
print(encrypt)
