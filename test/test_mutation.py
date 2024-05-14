import requests
import json

url = 'https://qyte2xsv3veorcshyitwogoyue.appsync-api.ap-northeast-1.amazonaws.com/graphql'
api_key = 'da2-wgzhlwbopfejlaxawed7iwohbu'

message = {"cciCode":"testCCI","companyCode":"testCode","content":{"a":1,"b":"he"},"id":"testID"}


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

variables = {
        "message": json.dumps(message),
    }

body = json.dumps({
    "query": query,
    "variables": variables,
})


headers = {
    'Content-Type': 'application/graphql',
    'x-api-key': api_key,
}

response = requests.post(url, data=body, headers=headers)
print(json.dumps(response.json(), indent=4))