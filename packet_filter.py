class PacketFilter:
    def __init__(self, filter_rule=None):
        self.filter_rule = filter_rule

    def filter_packet(self, packet):
        # Implement your filtering logic here
        # For now, just returning True to log all packets
        return True
