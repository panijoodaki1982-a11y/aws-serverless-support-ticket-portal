
import json
import boto3
import uuid
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SupportTickets')

def lambda_handler(event, context):
    try:
        body = event.get('body', event)

        if isinstance(body, str):
            body = json.loads(body)

        if not isinstance(body, dict):
            raise ValueError("Invalid request body")

    except (ValueError, TypeError):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid JSON request'})
        }

    name = body.get('name')
    email = body.get('email')
    issue = body.get('issue')

    if not all(isinstance(v, str) and v.strip()
               for v in [name, email, issue]):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'All fields are required'})
        }

    ticket_id = str(uuid.uuid4())

    item = {
        'ticketId': ticket_id,
        'name': name.strip(),
        'email': email.strip(),
        'issue': issue.strip(),
        'status': 'OPEN',
        'createdAt': datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': 'Support ticket created successfully',
            'ticketId': ticket_id
        })
    }
