aws cloudformation create-stack --stack-name transcribes3stack --template-body file://C:/path_to_yaml/proxy/template/bucket_config.yaml --parameters file://C:/path_to_json/proxy/template/s3_params.json
aws cloudformation create-stack --stack-name transcribeinputqueuestack --template-body file://C:/path_to_yaml/proxy/template/sqs.yaml --parameters file://C:/path_to_json/proxy/template/sqs_params.json
aws cloudformation create-stack --stack-name transcribeinputlambdastack --template-body file://C:/path_to_yaml/proxy/template/template.yaml --parameters file://C:/path_to_json/proxy/template/params.json
aws cloudformation update-stack --stack-name transcribes3stacknotifications --template-body file://C:/path_to_yaml/proxy/template/bucket_notifications.yaml --parameters file://C:/path_to_json/proxy/template/s3_params_lambda_notification.json