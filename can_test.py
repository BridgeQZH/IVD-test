import can
import logging


def _get_message(msg):

    return msg


class PCANBus(object):

    RX_SDO = 0x600
    TX_SDO = 0x580
    RX_PDO = 0x200
    TX_PDO = 0x180

    id_unit_a = [120, 121, 122, 123]
    id_unit_b = [124, 125, 126, 127]

    def __init__(self):

        logging.info("Initializing CANbus")

        self.bus = can.Bus(channel="PCAN_USBBUS1", bustype="pcan")
        self.buffer = can.BufferedReader()
        self.notifier = can.Notifier(self.bus, [_get_message, self.buffer])

    def send_message(self, message):

        try:
            self.bus.send(message)
            return True
        except can.CanError:
            logging.error("message not sent!")
            return False

    def read_input(self, id):

        msg = can.Message(arbitration_id=self.RX_PDO + id,
                          data=[0x00],
                          is_extended_id=False)

        self.send_message(msg)
        return self.buffer.get_message()

    def flush_buffer(self):

        msg = self.buffer.get_message()
        while (msg is not None):
            msg = self.buffer.get_message()

    def cleanup(self):

        self.notifier.stop()
        self.bus.shutdown()

    def disable_update(self):

        for i in [50, 51, 52, 53]:

            msg = can.Message(arbitration_id=0x600 + i,
                              data=[0x23, 0xEA, 0x5F, 0x00, 0x00, 0x00, 0x00, 0x00],
                              is_extended_id=False)

            self.send_message(msg)

pcan = PCANBus()
msg = Message(arbitration_id=pcan.RX_PDO + 50, is_extended_id=False, data=[0x4F, 0x00])
pcan.send_message(msg)
ret = pcan.read_input(0x78)
pcan.cleanup()

# import time, can
# bustype = 'socketcan'
# channel = 'vcan0'
# def producer(id):
#     # :param id: Spam the bus with messages including the data id.
#     bus = can.interface.Bus(channel=channel, bustype=bustype)
#     for i in range(10):
#         msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1], extended_id=False)
#         bus.send(msg)
#         print("hello")
#     # Issue #3: Need to keep running to ensure the writing threads stay alive. 
#     time.sleep(1)
# producer(10)


#  #!/usr/bin/env python
 
# """
#  This example shows how sending a single message works.
# """
 
# import can
 

# def send_one():
#     """Sends a single message."""

#     # this uses the default configuration (for example from the config file)
#     # see https://python-can.readthedocs.io/en/stable/configuration.html
#     # with can.interface.Bus() as bus:

#         # Using specific buses works similar:
#         # bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
#     bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
#     # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
#     # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
#     # ...

#     msg = can.Message(
#         arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True
#     )

#     try:
#         bus.send(msg)
#         print("Message sent on {bus.channel_info}")
#     except can.CanError:
#         print("Message NOT sent")


# if __name__ == "__main__":
#     send_one()

# # May have mature solutions on MATLAB