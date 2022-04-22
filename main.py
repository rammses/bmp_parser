from influxdb import InfluxDBClient

def main():
    inf_server = '172.21.23.2'
    inf_port = 8086
    user = "bmp"
    database = "bmp"
    password = "12qwasZX"

    client = InfluxDBClient(host=inf_server,
                            port=inf_port,
                            username=user,
                            database=database,
                            password=password,
                            ssl=False)

    # print(client.get_list_database())
    #
    # json_body = [
    #     {
    #         "measurement": "brushEvents",
    #         "tags": {
    #             "user": "Carol",
    #             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
    #         },
    #         "time": "2018-03-28T8:01:00Z",
    #         "fields": {
    #             "duration": 127
    #         }
    #     },
    #     {
    #         "measurement": "brushEvents",
    #         "tags": {
    #             "user": "Carol",
    #             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
    #         },
    #         "time": "2018-03-29T8:04:00Z",
    #         "fields": {
    #             "duration": 132
    #         }
    #     },
    #     {
    #         "measurement": "brushEvents",
    #         "tags": {
    #             "user": "Carol",
    #             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
    #         },
    #         "time": "2018-03-30T8:02:00Z",
    #         "fields": {
    #             "duration": 129
    #         }
    #     }
    # ]
    #
    # print(client.write_points(json_body))

    with open('1649861284.6593025.msg','r') as file:
        lines = file.readlines()
        for line in lines:
            print(type(line),line)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


