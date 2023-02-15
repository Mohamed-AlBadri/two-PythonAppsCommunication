# Application A will monitor changes to the file
import json
import time

prev_aps = []

while True:
    # this fucn is responsible to read the data from a file with a json format whch going to be chaninge Read the file content
    with open("/Users/mohamed-elbadri/Desktop/Python/access_points.json", "r") as f:
        aps = json.load(f)["access_points"]

    # This is to keep track of changes in the access points
    added_aps = [ap for ap in aps if ap not in prev_aps]
    removed_aps = [ap for ap in prev_aps if ap not in aps]
    changed_aps = [(ap, prev_ap) for ap in aps for prev_ap in prev_aps if ap["ssid"] == prev_ap["ssid"] and (ap["snr"] != prev_ap["snr"] or ap["channel"] != prev_ap["channel"])]

    # these three for loop to inform Application B of the changes
    for ap in added_aps:
        print(f"{ap['ssid']} is added to the list with SNR {ap['snr']} and channel {ap['channel']}")
    for ap in removed_aps:
        print(f"{ap['ssid']} is removed from the list")
    for (ap, prev_ap) in changed_aps:
        changes = []
        if ap["snr"] != prev_ap["snr"]:
            changes.append(f"SNR from {prev_ap['snr']} to {ap['snr']}")
        if ap["channel"] != prev_ap["channel"]:
            changes.append(f"channel from {prev_ap['channel']} to {ap['channel']}")
        print(f"{ap['ssid']}'s {' and '.join(changes)}")

    # Update the previous access points
    prev_aps = aps

    # Wait for X seconds before reading the file again
    time.sleep(1)
