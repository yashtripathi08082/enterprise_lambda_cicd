from app.service import get_message
from app.utils import format_response

# hgdjhavdjhavdgdgdhghg
def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": get_message()
    }








# def lambda_handler(event, context):

#     return {
#         "statusCode": 200,
#         "body": "Hello Enterprise CI/CD"
#     }