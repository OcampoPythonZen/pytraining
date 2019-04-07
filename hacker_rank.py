def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    for x,y in zip(a,b):
        if x < y:
            b_count +=1
        elif x > y:
            a_count += 1
    return a_count,b_count

def plusMinus(arr):
    n = 3
    zero_val = 0
    neg_val = 0
    posi_val = 0
    for val in arr:
        if val == 0:
            zero_val += 1
        elif val > 0:
            posi_val += 1
        elif val < 0:
            neg_val += 1

    print(format(float(posi_val/n), '.6f'))
    print(round((neg_val/n),6)) 
    print(round((zero_val/n),6))


a = [17,28,30]
b = [99,16,8]
print(compareTriplets(a,b))
