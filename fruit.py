def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    #Reverse and print the fruit list.
    fruit_list.reverse()
    print(f"Reversed list: {fruit_list}")
    #Append orange to the end of the fruit list and print the list.
    fruit_list.append("orange")
    print(f"Append orange: {fruit_list}")
    #find where apple is in list and insert cherry before apple in the list
    #and print the list.
    position = fruit_list.index("apple")
    fruit_list.insert(position, "cherry")
    print(f"Insert cherry before apple: {fruit_list}")
    #remove banana from the fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    #pop the last item from the list, print the item and the list.
    item = fruit_list.pop()
    print(f"pop item: {item}")
    print(f"poped list: {fruit_list}")
    #sort and print the list.
    fruit_list.sort()
    print(f"sorted list: {fruit_list}")
    #clear and print list.
    fruit_list.clear()
    print(f"cleared list: {fruit_list}")

if __name__ == "__main__":
    main()