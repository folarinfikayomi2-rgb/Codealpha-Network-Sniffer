CodeAlpha Basic Network Sniffer

Project Overview

This project is a basic network sniffer developed in Python using the Scapy library as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and displays useful information about network traffic, including source and destination IP addresses, protocols, and port numbers.

It also supports protocol filtering and saves captured packet information to a text file.

*/ Features
* Packet Capture: Captures network packets using Scapy.
* IP Address Extraction: Identifies source and destination IP addresses.
* Protocol Identification: Detects TCP, UDP, and ICMP traffic.
* Port Extraction: Displays source and destination ports for TCP and UDP packets.
* Payload Inspection: Displays a preview of the first 100 bytes of available packet payloads.
* Protocol Filtering: Allows users to select TCP, UDP, or ICMP traffic.
* File Logging: Saves captured packet information into a text file


*Technologies Used
* Python 3
* Scapy
* Kali Linux / Parrot OS
* Linux terminal


* Project Structure
--codealpha-network-sniffer/
├── sniffer.py
├── captured_packets.txt
├── requirements.txt
├── README.md


Installation

1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd codealpha-network-sniffer

2. Create a virtual environment
python3 -m venv .venv

3. Activate the virtual environment
source .venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

Usage
Run the network sniffer with elevated privileges because packet capture requires access to network interfaces:
sudo .venv/bin/python sniffer.py

Select one of the available protocols:
* TCP
* UDP
* ICMP

* The program captures up to 20 matching packets and displays their available network information.
Captured packet metadata is also saved to:
Sniffer.txt

* Screenshots
Screenshots documenting the development and testing of this project are available in the screenshots files.


Security and Ethical Considerations

This tool is intended for educational purposes and authorised network monitoring.
Only capture traffic on networks and devices you own or have explicit permission to monitor.

Captured packet payloads may contain sensitive information. Handle them responsibly and do not share private data.
HTTPS traffic is generally encrypted, so capturing its payload does not automatically reveal the original application data.

* Learning Outcomes
Through this project, I gained practical experience with:
* Network packet analysis.
* TCP, UDP, and ICMP protocols.
* IP addresses and port numbers.
* Python functions and conditional statements.
* Lambda functions and dictionaries.
* Packet filtering using Scapy.
* Basic network monitoring and traffic inspection.
* Author
* Developed as part of the CodeAlpha Cyber Security Internship.
