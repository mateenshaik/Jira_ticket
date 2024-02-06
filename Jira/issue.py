# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mateenshaikh046.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0T2IbQMonFAWg5BKmf7dPcQL81sNGuvVmhNKHqJ21BedPyjpKEyHvWClyu_YFKey4_HbeTyF2nXRxf5nuTjQJq4KVAUAFQGD0wFH_sQPjLS10PfCHZfMVKBuFMfymmgr1M86TfG0lbIyP-ZyypIT5br3ySoF5NIS0RNmo2EDPW7w=C60D06CD"

auth = HTTPBasicAuth("mateenshaikh046@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jeera Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
                ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10004"
    },
    "project": {
      "key": "MP"
    },

    "summary": "Jira ticket using Python scripts",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))