
def IsNumberInPower(number, numberInPower):
    ans = False
    current = 1
    while current < numberInPower:
        current *= number
    return numberInPower == current

def FindWichPowerCons(number, numberInPower):

    sqrByNum = int(number**0.5 + 1)
    if(number == sqrByNum): 
        return[]
    
    ans = FindWichPowerCons(number+1, numberInPower)
    if(IsNumberInPower(number, numberInPower)):
       ans.append(number)

    return ans

def Print(*obj, end = '\n', sep = ' '):
    for i in obj:
        print(i, end = sep)
    print(end = end)

def IsDataIncorrect(data):
    return False;

def Inp(messeng):
    ans = 0;
    try:
        ans = input(messeng)
        ans = int(ans)
        if(IsDataIncorrect(ans)):
            raise Exception;
    except:
        Print("somthing is incorrect, try again")
        return Inp(messeng)

    return ans

def main():
    number = int(Inp("enter number for finde power"))
   
    ans = FindWichPowerCons(2, sqrByNum,numberInPower=number)
    Print("ansver:")
    Print(*ans)

main()