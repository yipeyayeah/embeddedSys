# for logging of time
import time
import datetime

# csv to be able to open file
import csv
def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return today

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return now


def write_to_csv():
    while True:
        with open("dataset.csv", mode="a") as sensor_readings:
            sensor_write = csv.writer(
                sensor_readings, delimiter=", ", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            write_to_log = sensor_write.writerow(
                [date_now(), time_now(), i, t]
            )
        time.sleep(1)


write_to_csv()