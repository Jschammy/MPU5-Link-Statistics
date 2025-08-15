# Import required modules
import csv
from datetime import datetime, date, time
from time import sleep
from wr_api_client import WRApiClient
from api_message import APIMessage

# Establish global variables
WMI_PASSWORD = "password"
QUERY_IP = "10.3.1.254"
API_VARIABLE = "waverelay_neighbors"
csv_headers = ["Date/Time", "Local Radio", "Remote Node", "Remote Node IP Address", "Remote Radio", "Aggregate SNR", "Chain 1 SNR", "Chain 2 SNR", "Chain 3 SNR"]
link_statistics_csv = str(f"{date.today()}_MPU5_Link_Statistics.csv")

# Instantiate objects and pass arguments
wr_api = WRApiClient(query_ip=QUERY_IP)
wr_message = APIMessage(WMI_PASSWORD, API_VARIABLE)

# Main loop to start link statistic collection
while True:
    wr_api.send(wr_message.json_message)
    resp = wr_api.receive()
    neighbors = resp["variables"][API_VARIABLE]["value"]
    neighbors_by_line = neighbors.splitlines()
    for line in neighbors_by_line:
        neighbor_link = str(f"{datetime.today()},{line}")
        link_statistics = neighbor_link.split(",")
        print(link_statistics)
    sleep(0.5)



