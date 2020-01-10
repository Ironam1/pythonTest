import sys
f = open("prompt.txt", "r")
arg = f.read()
s = sys.argv[1]
print("sys.argv is", sys.argv[1])
# print(s.split())

def reverseS(arg):
    
    if sys.argv[1] == "-r":
        str = ""
        for i in arg:
            str = i + str

    elif sys.argv[1] == "-w":
        str = arg.split()
        str.reverse()
        # print(word)
    
    return str


print(reverseS(arg))


# def reverseW(s):
#     if sys.argv[2] == "-w":
#         s.split(" ")
#     return s


# print(reverseW(s))

