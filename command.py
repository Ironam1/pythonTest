import sys

s = sys.argv[1]
print("sys.argv is", sys.argv[1])


def reverseS(s):
    if sys.argv[2] == "-r":
        str = ""
        for i in s:
            str = i + str
        return str


print(reverseS(s))

str = sys.argv[2]
def reverseW(s):
    if sys.argv[2] == "-w":
        # str = ""
        str.reverse()
    return str


print(reverseW(s))

