from app.service import get_message


def lambda_handler(event, context):
    return {"statusCode": 200, "body": get_message()}


#dfghnm