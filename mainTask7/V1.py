def Fib(n):
    fib = [1, 1]

    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2]);

    return fib[:n];

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
    n = int(Inp("enter n - "))
    ans = Fib(n)

    Print("ansver:")
    Print(ans)

main()
