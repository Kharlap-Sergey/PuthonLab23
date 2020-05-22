def calculate_element_sum(vector):
    def calculate_element_sum_algo(vector, n):
       if(n == 1):
           return vector[0]

       return vector[n-1] + calculate_element_sum_algo(vector, n-1)

    if IsInDataCorrect(vector):
        return

    return calculate_element_sum_algo(vector, len(vector))

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
    array = ReadInArray("-enter array")
    sum = calculate_element_sum(array)
    Print("sum of elements is - ", sum)

main()

