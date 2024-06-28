def main():
    
    begin = int(input('Enter a number that a greater than one: '))
    end = int(input('Enter a value that is greater than the first input: '))
    plist = []
    num = range(begin, end)
    if num in range:
        for i in range(2, (num/2)+ 1):
            if (num % i) == 0:
                break
        else:
            print (f'{num} is a prime number')
            plist.append(num)
            
    return plist


if __name__ == '__main__':
    main()
