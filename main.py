import influxdb_client
from influxdb_client.client.write_api import  SYNCHRONOUS
from random import randint

def main():

    bucket ="bmp"
    org ="test1"
    token ="i4QpZZdrLt7VoShlQggHg2Dn4vGwsNijgGC9hfeasfJfpYWmm0MuwwppX1toRWW6wF6wHtSmxwW5DjgQGxWqpw=="
    url ="http://172.21.24.2:8086"


    # client = influxdb_client.InfluxDBClient(url=url,
    #                                         token=token,
    #                                         org=org)
    # write_api = client.write_api(write_options=SYNCHRONOUS)
    #
    # p = influxdb_client.Point("MyMeasurement").tag("location","istanbul").field("temperature", float(randint(10,36)))
    # write_api.write(bucket=bucket,
    #                 org=org,
    #                 record=p)


    #
    with open('1649861284.6593025.msg','r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


