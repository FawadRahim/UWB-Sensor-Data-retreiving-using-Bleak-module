import asyncio
from bleak import BleakClient
from functools import partial
import bitstruct
from bleak import BleakScanner, BleakError
from bleak import BleakClient
import datetime
from operator import itemgetter
import logging
import time
# Known Decawave services (from documentation)
NETWORK_NODE_SERVICE_UUID = '680c21d9-c946-4c1f-9c11-baa1c21329e7'  # The format here does not do anything
#UUID
OPERATION_MODE_CHARACTERISTIC_UUID = '3f0afd88-7770-46b0-b5e7-9fc099598964'
NETWORK_ID_CHARACTERISTIC_UUID = '80f9d8bc-3bff-45bb-a181-2d6a37991208'
LOCATION_DATA_MODE_CHARACTERISTIC_UUID = 'a02b947e-df97-4516-996a-1882521e0ead'
LOCATION_DATA_CHARACTERISTIC_UUID = '003bbdf2-c634-4b3d-ab56-7ec889b89a37'
PROXY_POSITIONS_CHARACTERISTIC_UUID = 'f4a67d7d-379d-4183-9c03-4b6ea5103291'
DEVICE_INFO_CHARACTERISTIC_UUID = '1e63b1eb-d4ed-444e-af54-c1e965192501'
STATISTICS_CHARACTERISTIC_UUID = '0eb2bc59-baf1-4c1c-8535-8a0204c69de5'
FW_UPDATE_PUSH_CHARACTERISTIC_UUID = '5955aa10-e085-4030-8aa6-bdfac89ac32b'
FW_UPDATE_POLL_CHARACTERISIC_UUID = '9eed0e27-09c0-4d1c-bd92-7c441daba850'
DISCONNECT_CHARACTERISTIC_UUID = 'ed83b848-da03-4a0a-a2dc-8b401080e473'
ANCHOR_PERSISTED_POSITION_CHARACTERISTIC_UUID = 'f0f26c9b-2c8c-49ac-ab60-fe03def1b40c'
ANCHOR_CLUSTER_INFO_CHARACTERISTIC_UUID = '17b1613e-98f2-4436-bcde-23af17a10c72'
ANCHOR_MAC_STATS_CHARACTERISTIC_UUID = '28d01d60-89de-4bfa-b6e9-651ba596232c'
ANCHOR_LIST_CHARACTERISTIC_UUID = '5b10c428-af2f-486f-aee1-9dbd79b6bccb'
TAG_UPDATE_RATE_CHARACTERISTIC_UUID = '7bd47f30-5602-4389-b069-8305731308b6'
Tag1User1 = "F9:4E:10:ED:A8:64"
Tag2User2 = "DA:B4:DA:45:2A:CE"
Tag3User3 = "FC:34:DA:5B:CA:0A"
Tag4User4 = "DD:56:98:33:60:57"
Tag5User5 = "C0:E9:BE:C4:08:52"
Tag6User6 = "E8:2B:41:14:CE:0F"
Tag7User7 = "C9:5E:40:62:EA:FC"
Tag8User8 = "DD:0B:1F:73:91:0D"
Tag9User9 = "DD:40:42:90:1B:C5"

returnedvalue = {}

ble_devices = []


# Names of location data mode data values
LOCATION_DATA_MODE_NAMES = [
    'Position only',
    'Distances only',
    'Position and distances']

# Names of location data content values
LOCATION_DATA_CONTENT_NAMES = [
    'Position only',
    'Distances only',
    'Position and distances']





def callback(client: BleakClient, sender: int, data: bytearray):
    global returnedvalue
    #hex_string = data.hex()
   # print(
   #     f"{client.address}",
   #     "".join([hex_string[x : x + 2] for x in range(0, len(hex_string), 2)]),
   #)

   #my modifications
    value = data
    returnedvalue = get_location_data_from_peripheral(value)

    print(f"{client.address}" + str(returnedvalue))

    if (client.address == Tag1User1):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0]['distance']
        anchor23977 = returnedvalue["distance_data"][1]['distance']
        anchor16545 = returnedvalue["distance_data"][2]['distance']
        anchor22067 = returnedvalue["distance_data"][3]['distance']

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):


            with open('C:/Users/fawad/Downloads/tag1/sensordata.txt', 'a') as datafile:
                datafile.write(str(posx) + str(",") + str(posy) + str(",") +timestamp +str(",") + str(qf)+ str(",")+ str(anchor3108) +  str(",") + str(anchor23977) + str(",") + str(anchor16545)+ str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")

    elif (client.address == Tag2User2):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']

        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag2/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",") + str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")


    elif (client.address == Tag3User3):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']

        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag3/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",") + str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")

    elif (client.address == Tag4User4):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']

        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag4/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")

    elif (client.address == Tag5User5):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']

        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag5/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")


    elif (client.address == Tag7User7):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']
        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag7/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")

    elif (client.address == Tag8User8):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']
        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag8/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")



    elif (client.address == Tag6User6):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']
        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag6/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")

    elif (client.address == Tag9User9):
        posx = returnedvalue['position_data']['x_position']
        posy = returnedvalue['position_data']['y_position']
        qf = returnedvalue['position_data']['quality']
        print(posx)
        print(posy)
        time = datetime.datetime.now()
        timestamp = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
        # get distances from target location to anchors
        anchor3108 = returnedvalue["distance_data"][0].get('distance')
        print(anchor3108)
        anchor23977 = returnedvalue["distance_data"][1].get('distance')
        anchor16545 = returnedvalue["distance_data"][2].get('distance')
        anchor22067 = returnedvalue["distance_data"][3].get('distance')

        if (posx and posy and timestamp and anchor3108 and anchor23977 and anchor16545 and anchor22067):

            with open('C:/Users/fawad/Downloads/tag9/sensordata.txt', 'a') as datafile:
                datafile.write(
                    str(posx) + str(",") + str(posy) + str(",") + timestamp + str(",") + str(qf)+ str(",")+ str(anchor3108) + str(
                        ",") + str(anchor23977) + str(",") + str(anchor16545) + str(",") + str(anchor22067) + "\n")

        else:
            print("missing data reported so data will not be recorded!")





    else:
        print("client not found!")


def get_location_data_from_peripheral(value):
    #print(value)
    bytes = value
    #print(bytes)
    data = parse_location_data_bytes(bytes)
    #print(data)
    return data


def parse_location_data_bytes(location_data_bytes):
    if len(location_data_bytes) > 0:
        location_data_content = location_data_bytes[0]
        location_data_bytes = location_data_bytes[1:]
        location_data_content_name = LOCATION_DATA_CONTENT_NAMES[location_data_content]
    else:
        location_data_content = None
        location_data_content_name = None
    if (location_data_content == 0 or location_data_content == 2):
        if len(location_data_bytes) < 13:
            raise ValueError('Location data content byte indicated position data was included but less than 13 bytes follow')
        position_bytes = location_data_bytes[:13]
        location_data_bytes = location_data_bytes[13:]
        position_data = bitstruct.unpack_dict(
            's32s32s32u8<',
            ['x_position', 'y_position', 'z_position', 'quality'],
            position_bytes)
    else:
        position_data = None
    if (location_data_content == 1 or location_data_content == 2):
        if len(location_data_bytes) < 1:
            raise ValueError('Location data content byte indicated distance data was included but no bytes follow')
        distance_count = location_data_bytes[0]
        #print(distance_count)
        location_data_bytes = location_data_bytes[1:]
        #print(location_data_bytes)
        #print(len(location_data_bytes))
        if len(location_data_bytes) < 7*distance_count:
            raise ValueError('Distance count byte indicated that {} distance values would follow so expected {} bytes but only {} bytes follow'.format(
                distance_count,
                7*distance_count,
                len(location_data_bytes)))
        distance_data=[]
        for distance_data_index in range(distance_count):
            distance_datum_bytes = location_data_bytes[:7]
            location_data_bytes = location_data_bytes[7:]
            distance_datum = bitstruct.unpack_dict(
                'u16u32u8<',
                ['node_id', 'distance', 'quality'],
                distance_datum_bytes)
            distance_data.append(distance_datum)
    else:
        distance_data = None
    return {
        'location_data_content': location_data_content,
        'location_data_content_name': location_data_content_name,
        'position_data': position_data,
        'distance_data': distance_data}

async def scannerforever():
    global ble_devices
    while True:
        async with BleakScanner() as scanner:
            await asyncio.sleep(5.0)
        for d in scanner.discovered_devices:
            print(d)
            ble_devices.append(d.address)
            print(ble_devices)



def run(addresses):
    # These loops will be the same loop. Use only one loop.
    # Ref: https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop
    loop = asyncio.get_event_loop()
    loop1 = asyncio.get_event_loop()
    address2 = "C0:E9:BE:C4:08:52"
    #mycode
    loop2 = asyncio.get_event_loop()

    for address in ble_devices:
        try:
            loop2.create_task(scannerforever())
            if address2 == address:
                ble_devices.clear()
                loop.create_task(connect_to_device(address2))
            else:
                ble_devices.clear()



        except Exception as e:
            # No. Do not stop a loop with potentially multiple long time running jobs on it because one job failed.
            loop.stop()
            address = address
            # This adds the new task to the same loop you just stopped.
            loop1.create_task(connect_to_device(address))

    loop.run_forever()
    loop1.run_forever()
    loop2.run_forever()

    # This method is problematic. My advice is to use the `asyncio.gather` and `loop.run_until_complete`
    # pattern in the two_devices.py example in the Bleak repo.


async def connect_to_device(address):
    async with BleakClient(address, timeout=20.0, use_cached=False) as client:
        print(f"Connected: {address} {client.is_connected}")


        await client.start_notify(LOCATION_DATA_CHARACTERISTIC_UUID, partial(callback, client))

        while True:
            await asyncio.sleep(1.0)


if __name__ == "__main__":



    run(
        [
            Tag1User1,
            Tag2User2,
            Tag3User3,
            Tag4User4,
            Tag5User5,
            Tag6User6,
            Tag7User7,
            Tag8User8,
            Tag9User9
        ]
    )