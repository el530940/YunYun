from collections import Counter

Value1= input("請輸入英文字母:")
result= ''
dictForSorting = dict(Counter(Value1))
print(dictForSorting)
sortedData =sorted(dictForSorting.items(),key=lambda  x:x[1],reverse=True)
print(sortedData)
for item in sortedData:
    print(item)
    result +=  item[0]*item[1]
print(result)
