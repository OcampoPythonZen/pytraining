def minExcludant(s,upper):
    found = -1
    for i in range(upper):
        if not i in s:
            found = i
            break
        else:
            found = upper
    return found

if __name__ == "__main__":
    s = [0, 4, 2, 3, 1, 7]
    upper = 10
    print(minExcludant(s,upper))