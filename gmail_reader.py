import imaplib
import email
import yaml
import re

def fetch_email_data():

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
                date = re.findall(r'\d{1,2} [A-Za-z]{3,4} \d{4}', my_msg.get('Date'))
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/html':
                        store_and_dollar_info = re.findall(r'<\s*span style=3D[^>]*>(.*?)<\s*/\s*span>', part.get_payload())
                        store_letters = re.findall(r'[A-Za-z]',store_and_dollar_info[2])
                        connected_store_letters = ''.join(store_letters)
                        date_store_amount_values = []
                        date_store_amount_values.append([date[0], connected_store_letters, store_and_dollar_info[1]])
                        return date_store_amount_values
                

                