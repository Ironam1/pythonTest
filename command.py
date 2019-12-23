import sys

s = sys.argv[1]
print("sys.argv is", sys.argv[1])
# print(s.split())

def reverseS(s):
    
    if sys.argv[2] == "-r":
        str = ""
        for i in s:
            str = i + str

    elif sys.argv[2] == "-w":
        str = s.split()
        str.reverse()
        # print(word)
    
    return str


print(reverseS(s))


# def reverseW(s):
#     if sys.argv[2] == "-w":
#         s.split(" ")
#     return s


# print(reverseW(s))

