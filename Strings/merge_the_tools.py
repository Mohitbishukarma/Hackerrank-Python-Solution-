def merge_the_tools(string, k):
    count = 0
    item = ''
    for i in string:
        if i not in item:
            item +=i
        count += 1
        if count==k:
            count = 0
            print(item)
            item = ''