import network
import time


WIFI_SSID = "VIVACOM_FiberNet_93D4"
WIFI_PASS = "zaniK2KMcs" # No this is not our regular password. :)

# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect(WIFI_SSID, auth=(network.WLAN.WPA2, WIFI_PASS))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
print("connceted")
# WIFI_SSID = "VIVACOM_FiberNet_93D4"
# WIFI_PASS = "zaniK2KMcs" # No this is not our regular password. :)
