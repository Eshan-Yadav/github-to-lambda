import datetime
def lambda_handler(event, context):
    print(datetime.datetime.now())
    print("Sucessfully executed")