import pyshark
import time
from collections import Counter
import csv

def capture_network(interface="Wi-Fi", run_time=30, csv_file_path="traffic_log.csv"):
    proto_counts = Counter()
    ip_counts = Counter()

    print(f"\n[+] Capturing on: {interface} for {run_time} seconds\n")
    print(f"{'Source IP':<15} {'Destination IP':<15} {'Protocol':<10}")

    # Set up CSV writer
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["timestamp", "src_ip", "dst_ip", "protocol"])

        # Live capture
        capture = pyshark.LiveCapture(interface=interface)
        end_time = time.time() + run_time

        for packet in capture.sniff_continuously():
            if time.time() > end_time:
                break
            if not hasattr(packet, 'ip'):
                continue

            try:
                proto = packet.highest_layer
                src = packet.ip.src
                dst = packet.ip.dst
                ts = packet.sniff_time
            except:
                continue

            proto_counts[proto] += 1
            ip_counts[src] += 1

            # Write to CSV
            csv_writer.writerow([ts, src, dst, proto])
            csv_file.flush()

            # Live output
            print(f"{src:<15} {dst:<15} {proto:<10}")

    print("\n[+] Capture complete.")

    return proto_counts, ip_counts
