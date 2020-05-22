def Fib(f, s, curr, n):
    if(curr == n):
        return []
    fib = [f, s]
    fib.extend(Fib(s, f+s, curr+1, n)[1:])
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
        return Inp(mes3seng)

    return ans

def main():
    n = int(Inp("enter n - "))
    ans = Fib(1, 1, 1, n)

    Print("ansver:")
    Print(ans)

main()

