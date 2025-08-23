def fizzBuzz(n):
    both_3_and_5 = "FizzBuzz"
    only_3 = "Fizz"
    only_5 = "Buzz"
    n += 1
    for cont in range(1,n):
        
        if cont % 3 == 0 and cont % 5 == 0:
            print(both_3_and_5)
            continue
        if cont % 3 == 0:
            print(only_3)
            continue
        if cont % 5 == 0:
            print(only_5)
            continue
        if cont % 3 != 0 and cont % 5 != 0:
            print(cont)
            continue
        

if __name__ == '__main__':
    try:
        n = int(input().strip())
        if n < 1 or n > 200000:
            print('Invalid value, please enter a new value')
        else:
            fizzBuzz(n)
    except ValueError:
        print('Enter a valid value')