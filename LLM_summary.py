from groq import Groq
import os
import csv

def summarize_traffic(csv_path):
    # Read the data
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No traffic detected.")
        return

    # Basic summary text to feed into LLM
    summary_text = f"""
Traffic Summary:

Total Records: {len(rows)}
Unique Source IPs: {len(set(r['src_ip'] for r in rows))}
Unique Destination IPs: {len(set(r['dst_ip'] for r in rows))}
Protocols Observed: {len(set(r['protocol'] for r in rows))}
First Packet Timestamp: {rows[0]['timestamp']}
Last Packet Timestamp: {rows[-1]['timestamp']}
"""

    print("\n=== RAW SUMMARY ===")
    print(summary_text)

    # Send to Groq for analysis
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are a network analysis assistant. Analyze the following traffic summary captured on a LAN. 
Explain what the stats imply about the activity. Focus on:
- Whether the traffic seems normal or suspicious.
- What kind of activity might be happening (e.g., browsing, scanning, IoT chatter, DNS floods)
- Whether the diversity or volume of traffic is noteworthy.
- Any red flags or patterns to watch out for.

Respond clearly and concisely in points.

Traffic Summary:
{summary_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful network traffic analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    explanation = response.choices[0].message.content

    print("\n=== LLM ANALYSIS ===")
    print(explanation)
    print("====================\n")
