"""
The below class is for easier configuration of the JSON messages sent to the MPU5 API server.
Once instantiated, the object with take the global argument of WMI_PASSWORD, and API_VARIABLE.
"""

class APIMessage:
    def __init__(self, wmi_password, api_variable):
        self.wmi_password = wmi_password
        self.api_variable = api_variable
        self.json_message = {
            "protocol_version": "1.5.0",      # API protocol version
            "username": "factory",    # "factory" required to be set for username
            "password": wmi_password, # WMI password
            "command": "get",        # "get", "set", "validate"
            "msgtype": "req",        # request-type message to be sent. Response is "rep" from server
            "token": "3x4y5z",     # token for tracking messaging
            "variables": {             # list of variables to get/set/validate
                api_variable: {}, # empty dictionary for get variables
            }
        }