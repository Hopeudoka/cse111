import pytest
import tempfile
import os
from website_blocker import blocked_websites, start_block, unblock_websites

local_ip = "127.0.0.1"

def test_blocked_websites():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        # Write sample data to the temporary CSV file
        temp_csv.write("Title\n")
        temp_csv.write("example.com\n")
        temp_csv.write("anotherexample.com\n")
        temp_csv.write("\n")  # Empty row to test that it is ignored
        temp_csv.write("yetanotherexample.com\n")
        temp_csv_filename = temp_csv.name
    
    # Expected output
    expected_websites = ["example.com", "anotherexample.com", "yetanotherexample.com"]

    # Call the function with the temporary CSV file
    actual_websites = blocked_websites(temp_csv_filename)
    
    # Assert the output is as expected
    assert actual_websites == expected_websites


def test_start_block():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        temp_csv.write("Title\n")
        temp_csv.write("example.com\n")
        temp_csv.write("anotherexample.com\n")
        temp_csv_filename = temp_csv.name
    
    # Create a temporary host file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_host:
        temp_host.write("127.0.0.1 alreadyblocked.com\n")
        temp_host.write(f"{local_ip} example.com\n")
        temp_host.write(f"{local_ip} anotherexample.com\n")
        temp_host_filename = temp_host.name
    
    global host_file_path
    host_file_path = temp_host_filename

    # Call the start_block function
    start_block()

    # Expected output in the host file
    expected_lines = [
        "127.0.0.1 alreadyblocked.com\n",
        f"{local_ip} example.com\n",
        f"{local_ip} anotherexample.com\n"
    ]

    # Read the actual content of the host file
    with open(temp_host_filename, "r") as f:
        actual_lines = f.readlines()

    # Assert the content of the host file is as expected
    assert actual_lines == expected_lines

    # Clean up temporary files
    os.remove(temp_csv_filename)
    os.remove(temp_host_filename)


def test_unblock_websites():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        temp_csv.write("Title\n")
        temp_csv.write("example.com\n")
        temp_csv.write("anotherexample.com\n")
        temp_csv_filename = temp_csv.name
    
    # Create a temporary host file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_host:
        temp_host.write(f"{local_ip} example.com\n")
        temp_host.write(f"{local_ip} anotherexample.com\n")
        temp_host.write(f"{local_ip} alreadyblocked.com\n")
        temp_host_filename = temp_host.name
    
    global host_file_path
    host_file_path = temp_host_filename

    # Call the unblock_websites function
    unblock_websites()

    # Expected output in the host file
    expected_lines = [
        f"{local_ip} example.com\n",
        f"{local_ip} anotherexample.com\n",
        f"{local_ip} alreadyblocked.com\n"
    ]

    # Read the actual content of the host file
    with open(temp_host_filename, "r") as f:
        actual_lines = f.readlines()

    # Assert the content of the host file is as expected
    assert actual_lines == expected_lines

    # Clean up temporary files
    os.remove(temp_csv_filename)
    os.remove(temp_host_filename)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])