def main():

    plist = []

    begin = int(input('Enter a number that is greater than one:'))
    end = int(input('Enter a number that is greater than the first input: '))
    
    for num in range(begin, end+1):
        if num > 1:
            
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                plist.append(num)
                print (num)

    return plist


if __name__ == '__main__':
    main()
