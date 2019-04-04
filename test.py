# test.py
# Author: Diljot Garcha
# Date: April 3, 2019

# Import statements
import os

from onepass import OnePass

if __name__ == "__main__":
    # Get 1Password CLI Session Token
    # Saved to an environment variable
    onepass = OnePass(session_token=os.environ['OP_TOKEN'])

    # Print the username and password for the GitHub login
    print(onepass.get_credentials("GitHub"))

    # Get the OTP for the GitHub login
    print(onepass.get_totp("GitHub"))

    # Save a file from 1PW to the hard drive
    onepass.save_file("codes.txt", "C:\\file.txt")
