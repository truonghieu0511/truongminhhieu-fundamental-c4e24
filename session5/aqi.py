from urllib.request import urlopen
import json
url = "https://wind.waqi.info/nsearch/full/hanoi?n=4"

# 1 Open connection
conn = urlopen(url)
# 2 Read Data
raw_data = conn.read()

# 3 Decode data
text=raw_data.decode("utf-8")
#4 convert data from str to dict
data = json.loads(text)
# print(data)
# print(data["dt"])
results = data["results"]
results = results[0]
print(results)


