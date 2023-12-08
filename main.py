import functions_framework

import twilio

from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'AC098...'  # update with Twilio account sid
TWILIO_AUTH_TOKEN = '6cafda...'  # update with Twilio auth token
TWILIO_NUMBER = '+15005550006'  # This is your test number which will not send SMS
TO_NUMBERS = ['+14123131272']  # any valid cell phone


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def send_sms(cloud_event):
    data = cloud_event.data
    bucket = data['bucket']
    name = data['name']

    event_id = cloud_event['id']
    event_type = cloud_event['type']

    the_body = "Item added to Cloud Storage bucket '" + bucket + "'.\n" + "Item added: " + name + "'.\n" + "Item event id: " + event_id + "Item event type: " + event_type

    client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print('Sending SMS to: ' + str(TO_NUMBERS))
    print('with body: ' + the_body)
    for TO_NUMBER in TO_NUMBERS:
        rv = client.messages.create(
            to= TO_NUMBER,
            from_= TWILIO_NUMBER,
            body= the_body
        )
