test_dic = {
    'codingal': 2,
    'is': 2,
    'best': 2,
    'for' : 2,
    'coding': 1
}

k = 2
result = 0

for keys in test_dic:
    if test_dic[keys] == k:
        result = result + 1

print("The frequency for k is:", result)