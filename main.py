# Import required modules
from logger import FileLogger
from datetime import datetime, date, time
from time import sleep
from wr_api_client import WRApiClient
from api_message import APIMessage

# Establish global variables
WMI_PASSWORD = "password"
QUERY_IP = "10.3.1.254"
API_VARIABLE = "waverelay_neighbors"

# Instantiate objects and pass arguments
wr_api = WRApiClient(query_ip=QUERY_IP)
wr_message = APIMessage(WMI_PASSWORD, API_VARIABLE)
logger = FileLogger()

def collect_statistics():

    while True:
        wr_api.send(wr_message.json_message)
        resp = wr_api.receive()
        neighbors = resp["variables"][API_VARIABLE]["value"]
        neighbors_by_line = neighbors.splitlines()

        for line in neighbors_by_line:
            neighbor_link = str(f"{date.today()},{datetime.now().time()},{line}")
            link_statistics = neighbor_link.split(",")
            logger.write_csv(link_statistics)
            print(link_statistics)

        sleep(0.1)

if __name__ == "__main__":
    collect_statistics()


