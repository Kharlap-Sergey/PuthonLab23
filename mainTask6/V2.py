def Fac(n):
    ans = 1;
    for i in range(1, n+1):
        ans += i
    return ans

def Pow(number, power):
    if power == 0:
        return 1;

    if(power%2 == 0):
        return Pow(number, power//2)**2
    else:
        return number*Pow(number, power-1);

def Func(x, n):
    ansver = Pow(x, n) / fac(n)
    return ansver

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
    x = int(Inp("enter n - "))
    n = int(Inp("enter x - "))
    ans = Fun(x, n)

    Print("ansver:")
    Print(ans)

main()
