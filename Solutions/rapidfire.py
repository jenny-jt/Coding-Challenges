"abc" -> a
"cbac" -> b
"aaaaaaaaaaaaaaabbccbd" -> d

from collections import Counter

def first_repeating(s):
    counter = Counter(s)
    # use LL and loop through LL and check counter[char]
    
    for char, count in counter.items():
        if count == 1:
            return char
        
    for char in s_list:
        if counter[char] == 1:
            return char

# given BST, return second largest element
# in order
def second_largest(root):
    arr = []
    self.count = 0

    def rev_order(node):
        if not node:
            return
       
        rev_order(node.right)
        self.count += 1
        if count == 2:
            return
        rev_order(node.left)
        
    rev_order(root)
    return arr[-1]

    
    list items 
    items.map( x -> x + 1).collections(toList)
    
    for x in items:
        x + 1
        
 "(+ 1 2)" -> 1 + 2 -> 3


# Integer to Roman Numeral Conversion
convert = {0: ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix" ], 
            1: ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxx", "xc"],
            2: ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"],
            3: ["", "m", "mm", "mmm"]}

# 55 -> LV 

# LV -> 50 + 5 -> 55
# XCVI -> XC = 90 VI=6 -> 90 + 6 = 96

def to_string(num):
    """takes in int num and returns roman numeral string"""
    digits, result = [], []
    
    while num > 10:
        remainder = num % 10
        digits.append(remainder)
        num //= 10
    
    digits.append(num)
    # digits = [5,7]
    
    digits = digits[::-1]
    # print(digits) # [7,5]
    
    count = 0
    while digits:
        digit_to_convert = digits.pop()
        converted_digit = convert[count][digit_to_convert]
        result.append(converted_digit)
        count += 1
    
    return ''.join(result[::-1])

print(to_string(96))
print(to_string(55))
print(to_string(75))