def main():
    
    plist = []

    begin = int(input('Enter a number that is greater than one:'))
    end = int(input('Enter a number that is greater than the first input: '))
    
    for num in range(begin, end):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
                else:
                    print (num)
    
    return plist


if __name__ == '__main__':
    main()
