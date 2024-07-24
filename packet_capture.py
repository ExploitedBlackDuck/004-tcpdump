import scapy.all as scapy
from packet_filter import PacketFilter
from packet_logger import PacketLogger
import time

class PacketCapture:
    def __init__(self, interface='eth0', filter_rule=None, log_file='packets.log', count=None, duration=None):
        self.interface = interface
        self.filter_rule = filter_rule
        self.logger = PacketLogger(log_file)
        self.packet_filter = PacketFilter(filter_rule)
        self.count = count
        self.duration = duration
    
    def start_capture(self):
        try:
            print(f"Starting packet capture on interface {self.interface} with filter {self.filter_rule}")
            start_time = time.time()
            packets = scapy.sniff(iface=self.interface, prn=self.process_packet, filter=self.filter_rule, count=self.count, timeout=self.duration)
            print(f"Captured {len(packets)} packets")
        except Exception as e:
            self.logger.log_error(f"Error starting packet capture: {str(e)}")
    
    def process_packet(self, packet):
        if self.packet_filter.filter_packet(packet):
            self.logger.log_packet(packet)

    @staticmethod
    def list_interfaces():
        return scapy.get_if_list()
