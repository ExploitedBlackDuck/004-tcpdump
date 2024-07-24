import logging
import json

class PacketLogger:
    def __init__(self, log_file, format='text'):
        self.logger = logging.getLogger('PacketLogger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.format = format

    def log_packet(self, packet):
        if self.format == 'json':
            packet_info = {
                'timestamp': str(packet.time),
                'src': packet[0][1].src,
                'dst': packet[0][1].dst,
                'summary': packet.summary()
            }
            self.logger.info(json.dumps(packet_info))
        else:
            self.logger.info(packet.summary())

    def log_error(self, message):
        self.logger.error(message)
