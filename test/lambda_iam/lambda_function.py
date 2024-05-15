from boto3.session import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import json
import os
from requests import request

def sigv4_request(
  url,
  method='GET',
  body=None,
  params=None,
  headers=None,
  service='execute-api',
  region=os.environ['AWS_REGION'],
  credentials=Session().get_credentials().get_frozen_credentials()
):
  """Sends an HTTP request signed with SigV4

  Args:
    url: The request URL (e.g. 'https://www.example.com').
    method: The request method (e.g. 'GET', 'POST', 'PUT', 'DELETE'). Defaults to 'GET'.
    body: The request body (e.g. json.dumps({ 'foo': 'bar' })). Defaults to None.
    params: The request query params (e.g. { 'foo': 'bar' }). Defaults to None.
    headers: The request headers (e.g. { 'content-type': 'application/json' }). Defaults to None.
    service: The AWS service name. Defaults to 'execute-api'.
    region: The AWS region id. Defaults to the env var 'AWS_REGION'.
    credentials: The AWS credentials. Defaults to the current boto3 session's credentials.
  Returns:
     The HTTP response
  """

  # sign request
  req = AWSRequest(
    method=method,
    url=url,
    data=body,
    params=params,
    headers=headers
  )
  SigV4Auth(credentials, service, region).add_auth(req)
  req = req.prepare()

  # send request
  return request(
    method=req.method,
    url=req.url,
    headers=req.headers,
    data=req.body
  )


print("hello")
message = {"cciCode":"testCCI","companyCode":"Hello from local with IAM role","content":{"a":1,"b":"he"},"id":"testID"}
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
# send request
response = sigv4_request(
'https://qyte2xsv3veorcshyitwogoyue.appsync-api.ap-northeast-1.amazonaws.com/graphql',
method='POST',
headers={
    'Content-Type': 'application/graphql',
},
body=body,
# In Lambda functions, you can omit 'region' and 'credentials' to use the Lambda's region and credentials
service="appsync"
)

# do something with response
print(response.status_code)
print(response._content)