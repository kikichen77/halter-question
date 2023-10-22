import pandas as pd

##can not download the there two CSV files
##https://comms-tech-test.s3.ap-southeast-2.amazonaws.com/tower_stream/tower-stream-2023-10-19T06%3A58%3A24.657Z.csv
##https://comms-tech-test.s3.ap-southeast-2.amazonaws.com/tower_stream/tower-stream-2023-10-19T06%3A58%3A24.746Z.csv
def main():
    import_data()


def import_data():
    df1 = pd.read_csv("./file/tower-stream-2023-10-19T06_58_24.613Z.csv")
    df2 = pd.read_csv("./file/tower-stream-2023-10-19T06_58_24.695Z.csv")
    df3 = pd.read_csv("./file/tower-stream-2023-10-19T06_58_24.773Z.csv")
    df4 = pd.read_csv("./file/tower-stream-2023-10-19T06_58_24.860Z.csv")
    data_frame = [df1, df2, df3, df4]
    df = pd.concat(data_frame, ignore_index=True)
    data_list = df.to_dict(orient='records')
    farmID_query = get_farmID_input()
    get_tower_id_from_farmId(data_list, farmID_query)


def get_farmID_input():
    user_input = input("Provide the farmID: ")
    return user_input


def get_tower_id_from_farmId(data, farmId_query):
    records_for_given_farm = []
    for record in data:
        if record['farmId'] == farmId_query:
            records_for_given_farm.append(record)
    if not records_for_given_farm:
        print("No records found for the provided farmID.")
        return
    get_tower_id_with_high_rssi(records_for_given_farm)


def get_tower_id_with_high_rssi(same_farmerId_list):
    highest_rssi_value = same_farmerId_list[0]['rssi']
    highest_rssi_towerId = same_farmerId_list[0]['towerId']
    for highest_rssi_towerId_list in same_farmerId_list:
        if highest_rssi_towerId_list['rssi'] > highest_rssi_value:
            highest_rssi_value = highest_rssi_towerId_list['rssi']
            highest_rssi_towerId = highest_rssi_towerId_list['towerId']
    print(f"{highest_rssi_towerId} is the highest amongst the towers for the given farm id")


main()
