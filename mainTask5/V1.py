
def Pow(number, power):
    if power == 0:
        return 1;

    if(power%2 == 0):
        return Pow(number, power//2)**2
    else:
        return number*Pow(number, power-1);

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
    number = int(Inp("enter number"))
    power = int(Inp("enter power"))
    ans = Pow(number, power)

    Print("ansver:")
    Print(ans)

main()
