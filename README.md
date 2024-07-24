[python] Sure! Here's a comprehensive document for the `tcpdump.py` utility.

---

# Python TCPDump Utility

## Overview

The Python TCPDump Utility is a command-line tool designed to capture and log network packets. This utility is implemented using Python and the `scapy` library, and it supports various features to filter and log packets effectively. It is compatible with both Linux and Windows environments.

## Features

- **Packet Capture**: Captures network packets on a specified interface.
- **Packet Filtering**: Filters captured packets based on user-defined rules.
- **Logging**: Logs captured packets to a specified file in either text or JSON format.
- **Interface Listing**: Lists available network interfaces on the system.
- **Packet Count Limit**: Stops capturing after a specified number of packets.
- **Duration Limit**: Stops capturing after a specified duration.

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Install Scapy**: Install the `scapy` library using pip:
   ```sh
   pip install scapy
   ```

## Usage

The utility is run from the command line. Below are the available options:

### Command Line Options

- `-i`, `--interface`: Network interface to capture packets on.
- `-f`, `--filter`: Filter rule for capturing packets (default: `tcp`).
- `-l`, `--log`: Log file to store captured packets (default: `packets.log`).
- `-c`, `--count`: Number of packets to capture.
- `-d`, `--duration`: Duration to capture packets in seconds.
- `--format`: Output format for logging packets (`text` or `json`, default: `text`).
- `--list-interfaces`: List available network interfaces.

### Examples

1. **List Available Interfaces**:
   ```sh
   python tcpdump.py --list-interfaces
   ```

2. **Capture Packets on a Specific Interface**:
   ```sh
   python tcpdump.py -i eth0 -f "tcp port 80" -l http_packets.log -c 100 -d 60 --format json
   ```
   This command captures packets on the `eth0` interface, filters for TCP packets on port 80, logs the packets to `http_packets.log`, and stops after capturing 100 packets or after 60 seconds, whichever comes first, in JSON format.

## Module Descriptions

### tcpdump.py

The main script that parses command line arguments and initiates packet capture.

### packet_capture.py

Handles packet capturing using the `scapy` library.

#### Methods

- `__init__(self, interface, filter_rule, log_file, count, duration)`: Initializes the packet capture settings.
- `start_capture(self)`: Starts the packet capture process.
- `process_packet(self, packet)`: Processes each captured packet.
- `list_interfaces()`: Static method to list available network interfaces.

### packet_filter.py

Provides filtering mechanisms for captured packets.

#### Methods

- `__init__(self, filter_rule)`: Initializes the filter rule.
- `filter_packet(self, packet)`: Filters packets based on the rule.

### packet_logger.py

Manages logging of packet information.

#### Methods

- `__init__(self, log_file, format)`: Initializes the logger.
- `log_packet(self, packet)`: Logs packet information.
- `log_error(self, message)`: Logs error messages.

### config.py

Contains configuration settings. (Currently, not used but can be extended for default values or additional settings.)

## Running the Utility on Windows

### Specifying an Interface

On Windows, network interfaces are specified using names like `\\Device\\NPF_{GUID}`. Use the `--list-interfaces` option to list available interfaces and find the appropriate GUID.

### Example

To capture packets on a specific interface by GUID:

```sh
python tcpdump.py -i \\Device\\NPF_{GUID} -f "tcp port 80" -l http_packets.log -c 100 -d 60 --format json
```

This command captures packets on the specified interface, filters for TCP packets on port 80, logs the packets to `http_packets.log`, and stops after capturing 100 packets or after 60 seconds, whichever comes first, in JSON format.

## Conclusion

The Python TCPDump Utility is a versatile tool for capturing and logging network packets. With its modular design and command-line interface, it provides a flexible and powerful solution for network analysis on both Linux and Windows platforms.

For any questions or contributions, feel free to open an issue or submit a pull request on the project's GitHub repository. Happy packet capturing!

---

Feel free to customize this document further based on specific needs or additional features you may want to highlight.
