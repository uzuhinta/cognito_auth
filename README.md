# command

```sh
pip install --target ./package requests
pip install --target ./package boto3

cd package/
zip -r ../my_deployment_package.zip . 

cd ..
zip my_deployment_package.zip lambda_function.py
```