def find_uniq(lst):
    dic = {};
    
    for char in lst:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    
    for char in dic:
        if dic[char] == 1:
            return char
    
print(find_uniq([1, 1, 1, 2, 1, 1]))