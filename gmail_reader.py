import imaplib
import email
import yaml

with open("email_credentials.yml") as f:
    content = f.read()
    
my_credentials = yaml.load(content, Loader=yaml.FullLoader)
user, password = my_credentials["user"], my_credentials["password"]

imap_url = 'imap.gmail.com'

my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(user, password)

my_mail.select('Inbox')
key = 'FROM'
value = 'bmoalerts@bmo.com'

typ, message_numbers_list = my_mail.search(None, key, value)
    
# mail_id_list = data[1]
# print(mail_id_list[0][0])
mail_ids = message_numbers_list[0].decode("utf-8").split()

alt_mail_ids = [mail_ids[-1]]
email_response = []

for mail_id in alt_mail_ids:
    message_content_id = '(RFC822)'

    t, data = my_mail.fetch(mail_id, message_content_id)
    email_response.append(data)

for msg in email_response:
    for body in msg: 
        if type(body) is tuple:
            my_msg = email.message_from_bytes((body[1]))
            for part in my_msg.walk():
                print(part.get_content_type())
                if part.get_content_type() == 'text/html':
                    print(part.get_payload())