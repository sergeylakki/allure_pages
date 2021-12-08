import os

import requests

d = 'report/'

print(requests.post('http://localhost:8000/generate', files={f: open(os.path.join(d, f), 'rb').read() for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))}).json()['url'])