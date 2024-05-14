import requests
import json

url = 'https://qyte2xsv3veorcshyitwogoyue.appsync-api.ap-northeast-1.amazonaws.com/graphql'
api_key = 'da2-wgzhlwbopfejlaxawed7iwohbu'

message = {"cciCode":"testCCI","companyCode":"test44123421Code","content":{"a":1,"b":"he"},"id":"testID"}


query = """
mutation SEND_MESSAGE($message: AWSJSON!) {
  sendMessage(message: $message) {
    cciCode
    companyCode
    content
    id
  }
}
"""


body = json.dumps({
    "query": query,
    "variables": {
        "message": json.dumps(message),
    },
})


headers = {
    'Content-Type': 'application/graphql',
    'x-api-key': api_key,
}

response = requests.post(url, data=body, headers=headers)
print(json.dumps(response.json(), indent=4))