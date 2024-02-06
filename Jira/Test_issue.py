# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mateenshaikh046.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0T2IbQMonFAWg5BKmf7dPcQL81sNGuvVmhNKHqJ21BedPyjpKEyHvWClyu_YFKey4_HbeTyF2nXRxf5nuTjQJq4KVAUAFQGD0wFH_sQPjLS10PfCHZfMVKBuFMfymmgr1M86TfG0lbIyP-ZyypIT5br3ySoF5NIS0RNmo2EDPW7w=C60D06CD"

auth = HTTPBasicAuth("mateenshaikh046@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


payload = json.dumps({
    "fields": {
        "project": {
            "key": "MP"
        },
        "summary": "Jira ticket using Python scripts",
        "description": "My first Jira Ticket",
        "issuetype": {
            "id": "10004"
        }
    }
})
