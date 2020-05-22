def CalculateElementSum(array):
    elementSum = 0

    for i in array:
        elementSum += i

    return elementSum

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

    sum = CalculateElementSum(array)
    Print("sum of elements is - ", sum)

main()
