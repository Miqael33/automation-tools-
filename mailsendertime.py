import time
import smtplib
from email.mime.text import MIMEText
from scapy.all import *

def scan_ip_traffic(duration=60):
    start_time = time.time()  # Remember the start time of scanning
    packets = []  # Create an empty list for packets
    while time.time() - start_time < duration:  # Check how much time has passed since the start of scanning
        # Scan IP traffic using Scapy and add packets to the list
        packets.extend(sniff(filter="ip or icmp or (tcp port 22)", count=10))
        time.sleep(5)  # Wait for 5 seconds before the next scanning

    # Create an email message with information about all packets
    message = "Results of IP traffic scanning:\n\n"
    for packet in packets:
        message += str(packet) + "\n\n"

    # Send an email with the results
    send_email(message)

def send_email(message):
    # Email settings
    sender_email = ""
    receiver_email = ""
    password = ""

    # Create an email message
    msg = MIMEText(message)
    msg['Subject'] = 'Results of IP traffic scanning'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    scan_ip_traffic(duration=60)  # Scan traffic for 60 seconds and send one email
