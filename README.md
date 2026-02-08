# **Network Traffic Capture & LLM-Based Analysis (PBL Project)**

This Project-Based Learning (PBL) project implements a system that captures live network traffic, logs it in a structured format, and generates an AI-driven analytical report. It provides hands-on exposure to packet-level monitoring and demonstrates how modern LLMs can support network forensics and anomaly detection.

## **📌 Project Overview**

### **1. Live Network Traffic Capture**
The system uses **PyShark** to monitor a selected network interface and extract:
- Timestamp  
- Source IP  
- Destination IP  
- Protocol  

All captured packets are written into `traffic_log.csv`.

### **2. Automated Traffic Summarization**
Once the capture completes, the system analyzes the CSV file and produces:
- Total number of records  
- Count of unique source & destination IPs  
- Number of distinct protocols  
- First and last packet timestamps  

### **3. LLM-Based Traffic Interpretation**
The generated summary is sent to an LLM (via the Groq API) to interpret:
- Whether the traffic looks normal or unusual  
- Possible behaviors occurring on the network  
- Any red flags or anomalies worth attention  

### **4. Core Execution Flow**
The `main.py` script orchestrates:
1. Live capture  
2. Summary generation  
3. AI analysis  
4. Displaying final insights  

## **📂 Project Structure**

```
├── main.py
├── network_detection.py
├── LLM_summary.py
├── traffic_log.csv   (auto-generated)
├── requirements.txt
```

## **⚙️ Installation & Requirements**

Install dependencies:

```
pip install -r requirements.txt
```

This project uses:
- **pyshark**  
- **groq**  
- **python-dotenv**

## **🚀 Running the Project**

1. Ensure your system supports packet capture  
   (Windows users may need Npcap installed).  
2. Set your Groq API key:  
   ```
   export GROQ_API_KEY="your_key_here"
   ```
3. Run the main script:  
   ```
   python main.py
   ```

## **🎯 Educational Purpose (PBL)**

This PBL project helped me understand:

- Real-time network packet capturing  
- Traffic logging and summarization  
- Integration of cybersecurity tools with LLMs  
- Automated anomaly detection workflows  

