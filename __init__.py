__title__ = 'upperhand'
__version__ = '0.1'
__author__ = 'Morteza Ansarinia'
__license__ = 'CC-NC-SA 4.0'
__copyright__ = 'Copyright 2014 Morteza Ansarinia'


from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from gmail import Gmail
import getpass

def process_sent_emails():
  email = raw_input("Your Email: ")
  my_password = getpass.getpass("Password: ")
  second_email = raw_input("Friend's Email: ")

  g = Gmail()
  g.login(email, my_password)

  emails = g.mailbox('[Gmail]/Sent Mail').mail(to=second_email)
  for email in emails:
    body = email.body
    tokens = word_tokenize(body)
    tags = pos_tag(tokens)

  g.logout()
  print("Logged out")

if __name__=='__main__':
  process_sent_emails()
