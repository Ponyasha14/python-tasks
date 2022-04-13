def lucky_ticket(n):
    s = [int(x) for x in str(n)]
    return sum(s[:int(len(s) / 2)]) == sum(s[int(len(s) / 2):])

lucky_ticket(6208789948)
#print(lucky_ticket(123321))
s = 'sdjbfj basj ksd bf'
print([x for x in s])
print(x for x in s)