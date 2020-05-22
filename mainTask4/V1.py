
def Reverse(array):
    ans = [];
    for i in range(len(array)-1, -1, -1):
        ans.append(array[i])
    return ans

def Print(*obj, end = '\n', sep = ' '):
    for i in obj:
        print(i, end = sep)
    print(end = end)

def IsInDataCorrect(data):
    return False;

def ReadInArray(messeng):
    ans = 0;
    try:
        inp = input(messeng).split();
        ans = [int(i) for i in inp]

        if(IsInDataCorrect(ans)):
            raise Exception;
    except:
        Print("somthing is incorrect, try again")
        return ReadInArray(messeng)

    return ans

def main():
    array = ReadInArray("enter array")
    reverseArr = Reverse(array)
    Print("reverse array - ", reverseArr)

main()

