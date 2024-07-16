import csv

def main():
    """
    
    """
    list = []
    count = 0

    with open("provinces.txt", "rt") as csv_file:
        reader = csv.reader(csv_file)

        for row in list:
            list.append(row)
        
        print(list)
        print()

        remove_first_element = list.pop(0)
        remove_last_element = list.pop()

        for line in list:
            if line == "AB":
                line = "Alberta"

        for line in list:
            if line == "Alberta":
                count += 1
                print(f"Alberta occurs {count} times in the modified list")

if __name__ == "__main__":
    main()