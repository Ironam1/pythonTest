def reverse(s):
    str=""
    for i in s:
        str = i + str
    return str 

s = "helloworld"

print ("the original string is : ")
print (s)

print ("the reversed string(using loops) is : ")
print (reverse(s))