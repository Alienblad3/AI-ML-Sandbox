from random import choice, randint
import psutil
import speedtest
from datetime import datetime
import os
user = os.getenv('USERNAME')
output = "test.txt"
if not os.path.exists(output):
    open(output, 'w').close()

def test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res['server']["lat"]

counters = psutil.net_io_counters(pernic=True)
    # Iterate over network interfaces
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'network data wireless' in lowered:
        counters = psutil.net_io_counters(pernic=True)
        # Create an empty dictionary to store network details
        network_details = {}
        # Iterate over network interfaces
        for nic, data in counters.items():
            if nic == "wlp3s0":
                network_details[nic] = {
                    "Bytes Sent": data.bytes_sent,
                    "Bytes Received": data.bytes_recv,
                    "Packets Sent": data.packets_sent,
                    "Packets Received": data.packets_recv,
                    "Error In": data.errin,
                    "Error Out": data.errout,
                    "Drop In": data.dropin,
                    "Drop Out": data.dropout
                }
        return network_details
    elif 'network data wired' in lowered:
        counters = psutil.net_io_counters(pernic=True)
        # Create an empty dictionary to store network details
        network_details = {}
        # Iterate over network interfaces
        for nic, data in counters.items():
            if nic == "enp4s0":
                network_details[nic] = {
                    "Bytes Sent": data.bytes_sent,
                    "Bytes Received": data.bytes_recv,
                    "Packets Sent": data.packets_sent,
                    "Packets Received": data.packets_recv,
                    "Error In": data.errin,
                    "Error Out": data.errout,
                    "Drop In": data.dropin,
                    "Drop Out": data.dropout
                }
        return network_details
    elif 'network data loopback' in lowered:
        counters = psutil.net_io_counters(pernic=True)
        # Create an empty dictionary to store network details
        network_details = {}
        # Iterate over network interfaces
        for nic, data in counters.items():
            if nic == "lo":
                network_details[nic] = {
                    "Bytes Sent": data.bytes_sent,
                    "Bytes Received": data.bytes_recv,
                    "Packets Sent": data.packets_sent,
                    "Packets Received": data.packets_recv,
                    "Error In": data.errin,
                    "Error Out": data.errout,
                    "Drop In": data.dropin,
                    "Drop Out": data.dropout
                }
        return network_details
    elif 'network speed' in lowered:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return {
            "Download": res["download"],
            "Upload": res["upload"],
            "Latency": res['server']["lat"]
        }
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])