from twilio.rest import Client


class NotificationManager:
    def __init__(self, acc_sid, auth_token):
        self.account_sid = acc_sid
        self.auth_token = auth_token

    def sendNotification(self, body, sender, receiver):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_=sender,
            body=body,
            to=receiver
        )

        print(message.sid)
