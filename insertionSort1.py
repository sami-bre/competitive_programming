def insertionSort1(n, arr):
    # input an array with a last item unsorted and this
    # function puts that element where it belongs
    val = arr[-1]   # the unsorted element
    working_index = n-2     # the working index starts at one before the last item.
    while(working_index >= 0):
        # if val is less than the element at the working index, that element
        # needs to be moved one step to the end so assign it at the next index
        if(val < arr[working_index]):
            arr[working_index + 1] = arr[working_index]
            # then print the new array
            print(str(arr)[1:-1].replace(",", ""))
            if(working_index == 0):     # handling an exceptional case
                arr[0] = val
                print(str(arr)[1:-1].replace(",", ""))
        else:
            # if val is not less than the element at the working index, we know it 
            # is less than all the previous elements so put it just after the current
            # working index
            arr[working_index + 1] = val
            # then print the array
            print(str(arr)[1:-1].replace(",", ""))
            break       # val has got its place now. so we should break
        working_index -= 1      # decrement the working_index by 1 at each step


insertionSort1(5, [2,2,2,2,1])