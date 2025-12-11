#Program 01

def count_even (numbers):
    for i in numbers:
        if i % 2 == 0:
            count += 1

    return count

num_list = list(input("Enter Numbers : "))
final_count = count_even(num_list)
print(final_count)
