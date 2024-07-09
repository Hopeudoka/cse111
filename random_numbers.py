import random


def main():
    # numbers = [21, 22, 15.2, 37, 40.7, 121.3]
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    # append_random_numbers(12) 
    # print(numbers)
    # append_random_numbers(13) 
    # print(numbers)
    
def append_random_numbers(numbers_list, quantity=1):
    numbers_list = []
    random_number = random.uniform(1.0, 200.0)
    round_number = round(random_number, 1)
    numbers_list.append(round_number)
    
main()
    
    