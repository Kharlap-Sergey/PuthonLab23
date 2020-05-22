def calculate_digits_sum(number):
    digitsSum = 0

    while(number != 0):
        digitsSum += number%10
        number //= 10

    return digitsSum

def Print(*obj, end = '\n', sep = ' '):
    for i in obj:
        print(i, end = sep)
    print(end = end)

def IsInDataCorrect(data):
    return False;

def Inp(messeng):
    ans = 0;
    try:
        ans = input(messeng)
        ans = int(ans)
        if(IsInDataCorrect(ans)):
            raise Exception;
    except:
        Print("somthing is incorrect, try again")
        return Inp(messeng)

    return ans

def main():
    number = int(Inp("-enter number for calculate sum digit"))
    digitsSum = calculate_digits_sum(number)
    Print(digitsSum)

main()

