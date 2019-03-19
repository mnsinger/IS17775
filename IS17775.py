import base64
import datetime
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from exchangelib import ServiceAccount, Configuration, Account, DELEGATE
from exchangelib import Message, Mailbox, FileAttachment, HTMLBody
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate
import mskcc

input_file_1 = '../properties.txt'
f_in = open(input_file_1, 'r')
properties_dict = {}
for line in f_in:
    properties_dict[line.partition('=')[0]] = line.partition('=')[2].strip()
f_in.close()

now = EWSTimeZone.localzone().localize(EWSDateTime.now())
two_days_ago = now - datetime.timedelta(days=2)
three_days_ago = now - datetime.timedelta(days=3)
bunch_of_days_ago = now - datetime.timedelta(days=54)

#print(bunch_of_days_ago)

credentials = ServiceAccount(username=properties_dict["email_data_uid"], password=mskcc.decrypt(properties_dict["email_data_pwd"]).decode("latin-1"))
config = Configuration(server='mail.mskcc.org', credentials=credentials)
account = Account(primary_smtp_address='{}@mskcc.org'.format(properties_dict["email_data_uid"]), config=config, autodiscover=False, access_type=DELEGATE)

#account.inbox.filter(datetime_received__lte=three_days_ago).delete()
account.inbox.all().delete()
account.sent.filter(datetime_sent__lte=three_days_ago).delete()

print("deleted")

#c=0
# my_account.inbox.filter(datetime_received__gt=EWSDateTime(2016, 1, 1))
#for m in account.inbox.filter(datetime_received__lte=bunch_of_days_ago).iterator():
#for m in account.inbox.filter(datetime_received__lte=bunch_of_days_ago):
#for m in account.sent.filter(datetime_sent__lte=bunch_of_days_ago):
#for m in account.inbox.filter(subject__contains='OR_SCHED_T2'):
#    if c < 10:
#        print(m)
#        #m.delete()
#        c+=1
#    else:
#        exit
