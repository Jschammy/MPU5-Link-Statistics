import csv
import os
from datetime import datetime, date, time

class FileLogger:
    def __init__(self):
        self.link_statistics_csv = str(f"{date.today()}-MPU5-Link-Statistics.csv")
        self.csv_headers = ["Date", "Time", "Local Radio", "Remote Node", "Remote Node IP Address", "Remote Radio", "Aggregate SNR", "Chain 1 SNR", "Chain 2 SNR", "Chain 3 SNR"]
        self.check_file()

    def check_file(self):
        file_exists = os.path.isfile(self.link_statistics_csv) and os.path.getsize(self.link_statistics_csv) > 0
        if not file_exists:
            with open(self.link_statistics_csv, "w", newline = "") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.csv_headers)

    def write_csv(self, statistics):
        with open(self.link_statistics_csv, "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(statistics)
