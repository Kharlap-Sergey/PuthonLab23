def reverse(vector):
    if IsDataIncorrect(vector):
        return
    def reverse_algo(vector, n):
        if(n == 1):
            return [vector[0]]
        ans = []
        ans.append(vector[n-1])
        ans.extend(reverse_algo(vector, n-1))
        return ans

    return reverse_algo(vector, len(vector))

    

def Print(*obj, end = '\n', sep = ' '):
    for i in obj:
        print(i, end = sep)
    print(end = end)

def IsDataIncorrect(data):
    return False;

def ReadInArray(messeng):
    ans = 0;
    try:
        inp = input(messeng).split();
        ans = [int(i) for i in inp]

        if(IsDataIncorrect(ans)):
            raise Exception;
    except:
        Print("somthing is incorrect, try again")
        return ReadInArray(messeng)

    return ans

def main():
    array = ReadInArray("enter array")
    reverseArr = reverse(array)
    Print("reverse array - ", reverseArr)

main()

