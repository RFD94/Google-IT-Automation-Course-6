#!/user/bin/env python3
import os
import requests

lists = []
filepath = '/data/feedback'
external_ip = "34.69.76.32"

for file in folder:
    with open(filepath + file, 'r') as f:
        lists.append({"title": f.readline().rstrip("\n"),"name": f.readline().rstrip("\n"),"date": f.readline().rstrip("\n"),"feedback": f.readline().rstrip("\n")})
        for item in lists:
            resp = requests.post("http://" + external_ip + "/feedback/", json=item)
            if resp.status_code != 201:
                raise Exception('POST error status={}'.format(resp.status_code))
            print('Created feedback ID {}'.format(resp.json()["id"]))