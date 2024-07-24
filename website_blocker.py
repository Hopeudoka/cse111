"""
A website blocker that gets a list of websites to block from a csv file and adds those websites to the systems's host file.
This website blocker is scheduled from 6:00am to 20:00pm.
"""
import time
from datetime import datetime
import csv


host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
local_ip = "127.0.0.1"

start_time = 6
end_time = 20

def main():
    
    while True:
        if block_time():
            start_block()
        else:
            unblock_websites()
        time.sleep(5)

def blocked_websites(filename):
    """
    This function takes a csv file, reads it and returns a list.
    parameters: filename
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
    """
    This functions gets the current time and compares it to the start and end time. This schedules the time for the blocker.
    It returns the schedule.
    parameters: None
    """
    #get current time
    time = datetime.now()
    #compare current time to start and end time.
    schedule = start_time <= time.hour < end_time
    #return schedule
    return schedule

def start_block():
    """
    This function gets the lists of websites and blocks them.
    parameters: None
    """
    #call the blocked_websites function to get the list.
    webistes = blocked_websites("blocked_sites.csv")
    #open host file to read and write.
    with open(host_file_path, "r+") as path_file:
        reader = path_file.read()
        #iterate through the list.
        for website in webistes:
            #pass website if in the host file
            if website in reader:
                pass
            else:
                #add website if not in the host file with ip to block.
                path_file.write(f"{local_ip} {website}\n")


def unblock_websites():
    """
    This function gets a lists of websites and unblocks them.
    parameters: None
    """
    #call the blocked_websites function to get the list.
    websites = blocked_websites("blocked_sites.csv")
    #open host file to read and write.
    with open(host_file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        #iterate through the file line by line.
        for line in lines:
            #write lines that do not contain websites in list.
            if not any(website in line for website in websites):
                file.write(line)
            #cut out the rest of the lines.
            file.truncate()

if __name__ == "__main__":
    main()