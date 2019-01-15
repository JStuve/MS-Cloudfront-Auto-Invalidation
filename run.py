import json
import boto3
import datetime
import os

def invalidate(event, context):

    currentTime = str(datetime.datetime.now())
    distId = os.environ['DIST_KEY_CLOUDFRONT']
    client = boto3.client('cloudfront')


    try:
        filePath = '/' + event["Records"][0]["s3"]["object"]["key"]

        resp = client.create_invalidation(
            DistributionId = distId,
            InvalidationBatch = {
                'Paths': {
                'Quantity': 1,
                'Items': [
                    filePath
                ]
                },
                'CallerReference': currentTime
            }
        )
        return {
            "statusCode" : 200,
            "body" : str(resp)
        }
    except Exception as e:
        print("Failed: " + str(e))
        return {
            "statusCode" : 420,
            "body" : "Invalidation Failed!"
        }


if __name__ == "__main__":
    data = json_data=open("test_event.json").read()
    event = json.loads(data)
    context = []
    invalidate(event, context)