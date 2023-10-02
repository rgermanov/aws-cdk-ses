import boto3
from botocore.exceptions import ClientError

def send_email(subject, body_text, body_html, to_addresses, from_address):
    client = boto3.client('ses')

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': to_addresses,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=from_address,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return e.response['Error']['Message']
    else:
        print(f"Email sent! Message ID: {response['MessageId']}")
        return f"Email sent! Message ID: {response['MessageId']}"

def handler(event, context):
    subject = "Hello from Lambda SES!"
    body_text = "Hello, this is a test email sent from AWS Lambda using Amazon SES."
    body_html = "<html><head></head><body><h1>Hello!</h1><p>This is a test email sent from AWS Lambda using Amazon SES.</p></body></html>"
    to_addresses = ['receiver_email']  # Replace with your recipient email address
    from_address = 'sender_email'  # Replace with your verified SES email address

    response = send_email(subject, body_text, body_html, to_addresses, from_address)
    
    return {
        'statusCode': 200,
        'body': response
    }
