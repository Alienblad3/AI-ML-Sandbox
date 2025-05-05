import speedtest
from datetime import datetime

def test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res['server']["lat"]

d, u, p = test()
now = datetime.now()
datestr = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"[{datestr}] Download: {round(d / 1048576, 1)}MB Upload: {round(u / 1048576, 1)}MB Latency: {p}")
