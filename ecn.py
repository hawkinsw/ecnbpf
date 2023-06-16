#!/usr/bin/env python

from bcc import BPF
import ctypes as ct

if __name__ == "__main__":
    # Build probe and open event buffer
    b = BPF(src_file='ecn.bcc')

    # Listen for event until the ping process has exited
    no_ecn_label = "No ECN"
    ecn_support_label = "ECN Support"
    congestion_label = "Congestion"
    print(f"{no_ecn_label.ljust(15)}|{ecn_support_label.ljust(15)}|{congestion_label.ljust(15)}")
    while True:
        try:
            b.perf_buffer_poll(1000)
            print(f"{repr(b['ecn_stats'][ct.c_int(0)].value).ljust(15)} {repr(b['ecn_stats'][ct.c_int(1)].value).ljust(15)} {repr(b['ecn_stats'][ct.c_int(2)].value).ljust(15)}")
        except KeyboardInterrupt:
            exit()
