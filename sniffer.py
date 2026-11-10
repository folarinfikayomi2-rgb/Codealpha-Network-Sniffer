from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

print("Codealpha Network sniffer")
print("Starting Packet Capture.............")

def process_packet(packet):
 if IP in packet:
   source_ip = packet[IP].src
   destination_ip = packet [IP].dst

   source_port = "N/A"
   destination_port = "N/A"

   if TCP in packet:   
     protocol = "TCP"
     source_port = packet [TCP].sport
     destination_port = packet [TCP].dport

   elif UDP in packet:
     protocol = "UDP"
     source_port = packet [UDP].sport
     destination_port = packet [UDP].dport

   elif ICMP in packet:
     protocol = "ICMP"

   else:
    protocol = "OTHER"

   print("Source Ip:", source_ip)
   print("Destination Ip:", destination_ip)
   print("Protocol:", protocol)
   print("Source_Port:", source_port)
   print("Destination_Port:", destination_port)

   with open("sniffer.txt", "a") as log_file:
    log_file.write(f"Source_Ip: {source_ip}\n")
    log_file.write(f"destination_ip: {destination_ip}\n")
    log_file.write(f"Protocol: {protocol}\n")
    log_file.write(f"Source_port: {source_port}\n")
    log_file.write(f"Destination_Port: {destination_port}\n")
    log_file.write("-" * 40 + "\n")

   if Raw in packet:
     payload = packet[Raw].load
     print("Payload Preview:", repr(payload[:100]))
  
   else:
     print("No Raw payload found")


     print("-" * 40)
 

print("Choose a protocol to capture:")
print("1. TCP")
print("2. UDP")
print("3. ICMP")

choice = input("Enter Your Chouce (1-3):")

protocol_filters = {
  "1": lambda packet: TCP in packet,

  "2": lambda packet: UDP in packet,

  "3": lambda packet: ICMP in packet

}

if choice in protocol_filters:
  print("\n Starting Seleted Protocol Capture...\n")

  sniff(prn=process_packet,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    lfilter=protocol_filters[choice],
    count=20
  )
else:
    print("Invalid Choice. Please 1, 2, or 3.")
