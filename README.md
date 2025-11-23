Network Traffic Capture & LLM-Based Analysis (PBL Project)

This Project-Based Learning (PBL) project implements an automated system for capturing live network traffic, logging it in a structured format, and generating an AI-driven analytical report. It provides a practical understanding of packet-level monitoring and showcases how modern LLMs can enhance network forensics.

Project Overview

This system performs three main tasks:

1. Live Network Traffic Capture
Captures packets from a chosen network interface using PyShark, extracting:
1. Timestamp
2. Source IP
3. Destination IP
4. Protocol
Captured data is saved into traffic_log.csv, allowing further analysis.
(Implementation: network_detection.py)

2. Automated Traffic Summarization
1. Processes the packet log and generates:
2. Total traffic count
3. Unique source/destination IPs
4. Observed protocol diversity
5. Time range of capture
(Implementation: LLM_summary.py)

3. LLM-Based Traffic Interpretation
The summary is sent to an LLM (via Groq API) to provide:
1. Behavioral insights
2. Suspicious activity detection
3. Protocol usage patterns
4. Potential anomalies
This forms the core intelligence layer of the system.
(Implementation: LLM_summary.py)

4. Main Orchestration Script
main.py ties everything together:
1. Runs the capture
2. Generates summaries
3. Triggers the AI analysis
4. Displays all results cleanly

File Structure
├── main.py
├── network_detection.py
├── LLM_summary.py
├── traffic_log.csv (generated after capture)
├── requirements.txt

Requirements
Install dependencies:
pip install -r requirements.txt


The project uses:
pyshark — for packet capturing
groq — for LLM API access
python-dotenv — for environment variable management

How to Run
Ensure your system supports packet capture (Wireshark/Npcap may be required on Windows).
Set your Groq API key:
export GROQ_API_KEY="your_key_here"

Run the main script:
python main.py 

Purpose of This PBL Project
This project helps students understand:
Real-time network packet analysis
Logging & summarization of traffic
AI-augmented security analysis

Combining cybersecurity tools with modern LLM workflows

It demonstrates how automated monitoring and intelligent analysis can support network defense and incident response.
