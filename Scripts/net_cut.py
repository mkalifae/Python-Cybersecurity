#!/usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()
    # packet.accept() to forward and packet.drop() to forward to gateway
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
