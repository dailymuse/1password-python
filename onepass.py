# onepass.py
# Author: Diljot Garcha
# Date: April 3, 2019

# Import statements
import json

from subprocess import run
from getpass import getpass

# Constants
OP_CLI = "op"
USERNAME = 0
PASSWORD = 1


class OnePass:

    def __init__(self, session_token=None):
        # Set the session token
        if session_token is None:
            session_token = getpass("Enter your 1Password CLI Session Token: ")
        self.__session_token = session_token

    @staticmethod
    def __run_command(command, text=True, json_output=True):
        # Run the command
        result = run(
            command,
            text=text,
            capture_output=True
        )

        # Return the output
        if json_output:
            return json.loads(result.stdout)
        else:
            return result.stdout

    def __create_basic_command(self, details):
        # Create a basic op command to run
        result = [OP_CLI]
        result.extend(details.split(" "))
        result.append("--session=" + self.__session_token)
        return result

    def __run_op_command(self, command_as_str, text=True, json_output=True):
        # Given a string, simply run a op command
        return self.__run_command(
                self.__create_basic_command(
                    command_as_str
                ),
                text=text,
                json_output=json_output
            )

    def get_credentials(self, item_name):
        # Get credentials for a specific item
        result = {}
        output = self.__run_op_command("get item {}".format(item_name))

        result["username"] = str(
            output["details"]["fields"][USERNAME]["value"]
        )

        result["password"] = str(
            output["details"]["fields"][PASSWORD]["value"]
        )
        return result

    def get_totp(self, item_name):
        # Get the One-Time-Password for a specifc item
        return self.__run_op_command("get totp {}".format(item_name))

    def get_uuid(self, file_name):
        # Get the UUID of a specific item
        output = self.__run_op_command("get item {}".format(file_name))
        return output["uuid"]

    def save_file(self, file_name, save_location):
        # Save the file to a location
        output = self.__run_op_command(
            "get document {}".format(
                self.get_uuid(file_name)
            ),
            text=False,
            json_output=False
        )

        with open(save_location, "wb") as file:
            file.write(output)

        print("File saved to: " + str(save_location))
