def min_number_of_subsequences(source, target):
    # 检查target的字符是否都在source中存在
    source_set = set(source)
    for char in target:
        if char not in source_set:
            return -1

    # 指针i指向source的匹配字符，指针j指向target匹配字符
    i, j = 0, 0
    count = 0  # subsequence 计数    
    while j < len(target):
        # 寻找target中的最长匹配
        while i < len(source):
            if source[i] == target[j]:
                j += 1
                if j == len(target):
                    break
            i += 1
        i = 0  # source指针归零
        count += 1  # 计数器加一

    return count

print(min_number_of_subsequences("abc", "abcbc"))
# Output: 2
print(min_number_of_subsequences("abc", "acdbc"))
# Output: -1
print(min_number_of_subsequences("xyz", "xzyxz"))
# Output: 3