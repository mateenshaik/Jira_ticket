import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mateenshaikh046.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0T2IbQMonFAWg5BKmf7dPcQL81sNGuvVmhNKHqJ21BedPyjpKEyHvWClyu_YFKey4_HbeTyF2nXRxf5nuTjQJq4KVAUAFQGD0wFH_sQPjLS10PfCHZfMVKBuFMfymmgr1M86TfG0lbIyP-ZyypIT5br3ySoF5NIS0RNmo2EDPW7w=C60D06CD"

auth = HTTPBasicAuth("mateenshaikh046@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output = json.loads(response.text)
for i in output:
  name = i['name']
  print(name)
#  print["name"]
# name = output[0]["name"]
# print(name)
