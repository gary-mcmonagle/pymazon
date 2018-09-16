import re, base64, email
from cosmos.add_product import add_product
from cosmos.remove_product import remove_product

def analyse_inbox(service, db_client):
    messages = service.users().messages().list(userId='me').execute()
    if "messages" in messages:
        for idx, m in enumerate(messages["messages"]):
            try:
                analyse_message(db_client, service, m['id'])
            except:
                pass
            service.users().messages().trash(userId='me', id=m['id']).execute()

def analyse_message(db_client, service, message_id):
    message = service.users().messages().get(userId='me', id=message_id, format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII')).decode()
    mime_msg = email.message_from_string(msg_str)
    from_email = re.search(r'[\w\.-]+@[\w\.-]+', mime_msg["From"]).group(0)
    infer_subject(db_client, mime_msg["Subject"], from_email)

def infer_subject(db_client, subject, sender):
    split = subject.split(' ')
    if split[0].lower() == "add" and len(split) == 3:
        add_product(db_client, split[1], sender, float(split[2]))
    if split[0].lower() == "remove":
        remove_product(db_client, split[1], sender)




