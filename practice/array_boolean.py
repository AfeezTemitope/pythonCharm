class ArrayBool:

    # @staticmethod
    # def booli(arr):
    #     for numbers in arr:
    #         if arr[numbers] % 2 == 0:
    #             return False
    #         else:
    #             return True

    @staticmethod
    def badBoy(arr):
        return [num % 2 != 0 for num in arr]


    arr = [4, 5, 8, 8, 8, 2, 9]





    print(badBoy(arr))

# def new(arr):
#     return [arr[i] > arr[i-1] for i in range(1, len(arr))]
