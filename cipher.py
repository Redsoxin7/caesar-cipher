# add your code here

sentence = input("Input a sentence to be encrypted:")
print("Original Sentence: " + sentence)
print("Encrypted Sentence: ", end="")
for char in sentence:
    if ord(char) >= 97 and ord(char) <= 117:
        print(chr(ord(char) + 5), end="")
        # print(ord(char))
    elif ord(char) >= 118 and ord(char) <= 122:
        print(chr(ord(char) - 21), end="")
    elif ord(char) >= 65 and ord(char) <= 85:
        print(chr(ord(char) + 5), end="")
    elif ord(char) >= 86 and ord(char) <= 90:
        print(chr(ord(char) - 21), end="")
    elif ord(char) >= 32 and ord(char) <= 64:
        print(chr(ord(char)), end="")
