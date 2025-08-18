class APIMessage:
    """Constructs the JSON payload used to query the WaveRelay API."""
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