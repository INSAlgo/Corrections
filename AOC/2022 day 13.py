from reader import read

lines = read("day13.txt")


# Part 1 :

n = (len(lines) + 1) //3
pairs = [(eval(lines[i*3]), eval(lines[i*3+1])) for i in range(n)]

def compare(left: int | list, right: int | list) -> int :
    if type(left) is int and type(right) is int :
        if left < right :
            return 1
        if left > right :
            return -1
        return 0
    
    if type(left) is int :
        left = [left]
    if type(right) is int :
        right = [right]

    l, r = len(left), len(right)
    i = 0
    while i < l and i < r :
        res = compare(left[i], right[i])
        if res != 0 :
            return res
        i += 1

    if i < r :
        return 1
    if i < l :
        return -1
    return 0

s = 0
k = 1
for left, right in pairs :
    if compare(left, right) == 1 :
        s += k
    k += 1

print(s)

# Part 2 :

class Packet :
    def __init__(self, txt) :
        self.val = eval(txt)
    
    def __lt__(self, other) :
        return compare(self.val, other.val) == 1
    
    # For test
    def __str__(self) :
        return str(self.val)

packets = [Packet(line) for line in lines if line != ""] + [Packet("[[2]]"), Packet("[[6]]")]

packets.sort()

lists = [packet.val for packet in packets]

print((lists.index([[2]]) + 1) * (lists.index([[6]]) + 1))