def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    user_input = []
    print("Enter 5 values:")
    for i in range(5):
        value = int(input(f"Value {i+1}: "))
        user_input.append(value)

    merge_sort(user_input)

    print("Sorted list:", user_input)

if __name__ == "__main__":
    main()
