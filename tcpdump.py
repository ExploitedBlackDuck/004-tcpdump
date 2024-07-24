import argparse
from packet_capture import PacketCapture

def main():
    parser = argparse.ArgumentParser(description="Python TCPDump Utility")
    parser.add_argument('-i', '--interface', type=str, help='Network interface to capture packets on')
    parser.add_argument('-f', '--filter', type=str, default='tcp', help='Filter rule for capturing packets')
    parser.add_argument('-l', '--log', type=str, default='packets.log', help='Log file to store captured packets')
    parser.add_argument('-c', '--count', type=int, help='Number of packets to capture')
    parser.add_argument('-d', '--duration', type=int, help='Duration to capture packets in seconds')
    parser.add_argument('--format', type=str, choices=['text', 'json'], default='text', help='Output format for logging packets')
    parser.add_argument('--list-interfaces', action='store_true', help='List available network interfaces')

    args = parser.parse_args()

    if args.list_interfaces:
        interfaces = PacketCapture.list_interfaces()
        for index, iface in enumerate(interfaces):
            print(f"{index}: {iface}")
        return

    capturer = PacketCapture(interface=args.interface, filter_rule=args.filter, log_file=args.log, count=args.count, duration=args.duration)
    capturer.start_capture()

if __name__ == "__main__":
    main()
