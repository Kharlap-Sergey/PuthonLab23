
def IsNumberInPower(number, numberInPower):
    ans = False
    current = 1
    while current < numberInPower:
        current *= number
    return numberInPower == current

def FindWichPowerCons(numberInPower):
    ansver = list();
    sqrByNum = int(numberInPower**0.5+2)
    
    for number in range(2, sqrByNum):
        if(IsNumberInPower(number, numberInPower)):
            ansver.append(number)
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
    number = int(Inp("enter number for finde power"))
    ans = FindWichPowerCons(number)
    Print("ansver:")
    Print(*ans)

main()