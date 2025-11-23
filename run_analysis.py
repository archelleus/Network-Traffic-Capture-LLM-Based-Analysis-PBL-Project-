# main.py
from network_detection import capture_network
from LLM_summary import summarize_traffic

def main():
    interface = "Wi-Fi"  # change if needed
    csv_path = "traffic_log.csv"
    run_time = 10

    # Step 1: Run capture for 30 seconds (printing live)
    print("[*] Starting capture...")
    proto_counts, ip_counts = capture_network(interface=interface, run_time=run_time, csv_file_path=csv_path)

    # Step 2: Generate summary and LLM analysis
    print("\n[*] Generating summary...\n")
    summarize_traffic(csv_path)

if __name__ == "__main__":
    main()
