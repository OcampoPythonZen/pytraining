def almostIncreasin(sequence):
    times = 0
    for vals in sequence:
        if vals < vals + 1:
            times += 1
            if times > 1:
                return False
        else:
            return True

if __name__ == "__main__":
    sequence = [1,3,2,1]
    print(almostIncreasin(sequence))