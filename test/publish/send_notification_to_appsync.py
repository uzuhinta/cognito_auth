import os
import json
from requests import request
from urllib.parse import urlparse

from boto3.session import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from config import Config

query = """
mutation SEND_MESSAGE($message: AWSJSON!) {
    sendMessage(message: $message) {
        id
        tenantCode
        action
        content
    }
}
"""


def sigv4_request(
    url,
    method="GET",
    body=None,
    params=None,
    headers=None,
    service="execute-api",
    region=os.environ["AWS_REGION"],
    credentials=Session().get_credentials().get_frozen_credentials(),
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
    req = AWSRequest(method=method, url=url, data=body, params=params, headers=headers)
    SigV4Auth(credentials, service, region).add_auth(req)
    req = req.prepare()

    # send request
    return request(method=req.method, url=req.url, headers=req.headers, data=req.body)


def sendMessage(msg):
    url = Config.APPSYNC_API_URL
    print(f'URL: {url}')
    api_key = Config.APPSYNC_API_KEY
    method = "POST"
    headers = {
        "Content-Type": "application/json",
        "host": urlparse(url).hostname,
    }
    body = json.dumps({"query": query, "variables": {"message": json.dumps(msg)}})
    print('api_key', api_key)

    try:
        if api_key is not None:
            print('key')
            headers["x-api-key"] = api_key
            request(url=url, method=method, headers=headers, data=body)
        else:
            print('sign')
            res = sigv4_request(
                url=url,
                method=method,
                headers=headers,
                body=body,
                service="appsync",
            )
            print(res.content)
    except:
        print('Wrong')
