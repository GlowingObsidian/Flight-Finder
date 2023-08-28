from twilio.rest import Client


class NotificationManager:
    def __init__(self, acc_sid, auth_token):
        self.account_sid = acc_sid
        self.auth_token = auth_token

    def sendNotification(self, body):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_='+12514184845',
            body=body,
            to='+918697445294'
        )

        print(message.sid)
