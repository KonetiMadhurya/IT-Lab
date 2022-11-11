import string
characters = string.ascii_letters

text = input("Enter original text : ")
key = int(input("Enter key : "))

list = {}
for i in range(len(characters)):
    list[characters[i]] = characters[(i+key)%len(characters)]
encrypt_text = []
for char in text:
    if char == " ":
        temp = "$"
        encrypt_text.append(temp)
    elif char in characters:
        temp = list[char]
        encrypt_text.append(temp)
    else:
        temp = char
        encrypt_text.append(temp)
encrypt = "".join(encrypt_text)
print(encrypt)

list1 = {}
for i in range(len(characters)):
    list1[characters[i]] = characters[(i-key)%len(characters)]
decrypt_text = []
for char in encrypt:
    if char == "$":
        temp = " "
        decrypt_text.append(temp)
    elif char in characters:
        temp = list1[char]
        decrypt_text.append(temp)
    else:
        temp = char
        decrypt_text.append(temp)
decrypt = "".join(decrypt_text)
print(decrypt)

def frequency(text):
    frequency=dict()
    length = len(text)
    offset = 100/length
    for i in text:
        if i == "":
            continue
        elif i in frequency:
            frequency[i]+=offset
        else:
            frequency[i]=offset
    return frequency
an_freq = frequency(text)
print(an_freq)
