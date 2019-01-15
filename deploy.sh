pip install awscli --upgrade --user

echo "Zipping the Zipper!"
zip run.zip run.py


echo "DEPLOYING..."
aws lambda update-function-configuration --function-name MS-Cloudfront-Auto-Invalidate --handler run.invalidate
aws lambda update-function-code --function-name MS-Cloudfront-Auto-Invalidate --zip-file fileb://run.zip