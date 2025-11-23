from network_detection import capture_network
from LLM_summary import summarize_traffic

def main():
    interface = "Wi-Fi"  
    csv_path = "traffic_log.csv"
    run_time = 10

    
    print("[*] Starting capture...")
    proto_counts, ip_counts = capture_network(interface=interface, run_time=run_time, csv_file_path=csv_path)


    print("\n[*] Generating summary...\n")
    summarize_traffic(csv_path)

if __name__ == "__main__":
    main()

