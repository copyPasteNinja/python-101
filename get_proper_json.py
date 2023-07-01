import json, boto3, uuid
client = boto3.client('dynamodb')


def write2dynamo(**kwargs): #batchID, email, firstname, lastname, homecity, occupation, phone, registered
    response = client.put_item(
        TableName='aKumoSolutions-registration',
        Item={
              "batchID": {
                "S": kwargs['batchID']
              },
              "phone": {
                "N": kwargs['phone']
              },
              "registered": {
                "BOOL": kwargs['registered']
              },
              "members": {
                "L": [
                  {
                    "M": {
                      "email": {
                        "S": kwargs['email']
                      },
                      "firstname": {
                        "S": kwargs['firstname']
                      },
                      "homecity": {
                        "S": kwargs['homecity']
                      },
                      "lastname": {
                        "S": kwargs['lastname']
                      },
                      "occupation": {
                        "S": kwargs['occupation']
                      }
                    }
                  }
                ]
              }
            }
    )
  
def list_pre_members(batchID):
  response = client.query(
      TableName="aKumoSolutions-registration",
      KeyConditionExpression='batchID = :batchID',
      ExpressionAttributeValues={
          ':batchID': {'S': batchID}
      }
  )
  return response['Items']

def lambda_handler(event, context):
    users = list_pre_members(batchID="january-2023")
    print(users)
    users_data = []
    for user in users:
        for member in user['members']['L']:
            users_data.append(
                {
                    # "batchID": batchID,
                    "phone": user['phone']['N'],
                    "firstname": member['M']['firstname']['S'], 
                    "lastname": member['M']['lastname']['S'], 
                    "email": member['M']['email']['S'],
                    "homecity": member['M']['homecity']['S'],
                    "occupation": member['M']['occupation']['S'],
                }
            )

    for member in users_data:
        if event['phone'] == member['phone']:
            result = "User with this email exists, contact aKumo Support for help"
            statusCode = 400
            
        else:
            write2dynamo(
                batchID="january-2023", 
                email=event["email"], 
                firstname=event["firstname"], 
                lastname=event["lastname"], 
                homecity=event["homecity"], 
                occupation=event["occupation"], 
                phone=event["phone"],
                registered=False
            )
            result = users_data
            statusCode = 200
    
    headers = {
        "Content-Type": "application/json", 
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*" 
    }
    responseObject = {"statusCode": statusCode, "headers": headers, "body": json.dumps({"Users": result})}
    
    return responseObject
    