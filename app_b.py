import sys
import json

# stay continuously read from the standard input
while True:
    line = sys.stdin.readline()
    
    # Check if the line is not empty
    if line:
        # Load the access points from the line
        aps = json.loads(line)["access_points"]
        
        # Print the changes to the access points
        for ap in aps:
            ssid = ap["ssid"]
            snr = ap["snr"]
            channel = ap["channel"]
            print(f"{ssid} has SNR {snr} and channel {channel}")
