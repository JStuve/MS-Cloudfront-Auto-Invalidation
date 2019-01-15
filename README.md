# Cloudfront Auto Invalidate

### Deploy Lambda

1. Install/Upgrade awscli

2. Run deploy script

    `$ sh deploy.sh`

### Test Lambda Locally

1. Install *Python-Lambda-Local*

   `$ pip3 install python-lambda-local`

2. Run following command

    `python-lambda-local -f file_function_name file_name.py test_data.json`

