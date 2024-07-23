"""

"""
import os
import time
from datetime import datetime
import pytest
import csv


host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
local_ip = "127.0.0.1"

start_time = 6
end_time = 18

def main():
    
    while True:
        if block_time():
            start_block()
        else:
            unblock_websites()
        time.sleep(5)

def blocked_websites(filename):
    """

    """
    #create an empty list.
    websites = []
    #open and read file into a list.
    with open(filename, "rt") as file:
        #use the reader module to read the csv file.
        reader = csv.reader(file)
        #skip the first title line.
        next(reader)
        #a for loop to go through each row in the file.
        for row_list in reader:
            if len(row_list) != 0:
                #append each row to the list.
                websites.extend(row_list)

    return websites


def block_time():
    time = datetime.now()
    schedule = start_time >= time.hour < end_time
    return schedule

def start_block():
    webistes = blocked_websites("blocked_sites.csv")
    with open(host_file_path, "r+") as path_file:
        reader = path_file.read()
        for website in webistes:
            if website in reader:
                pass
            else:
                path_file.write(f"{local_ip} {website}\n")


def unblock_websites():
    websites = blocked_websites("blocked_sites.csv")
    with open(host_file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in websites):
                file.write(line)
            file.truncate()

if __name__ == "__main__":
    main()