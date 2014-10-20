__title__ = 'upperhand'
__version__ = '0.1'
__author__ = 'Morteza Ansarinia'
__license__ = 'CC-NC-SA 4.0'
__copyright__ = 'Copyright 2014 Morteza Ansarinia'


from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from gmail import Gmail
import getpass

def process_emails(emails):

  score = 0
  index = 0

  for msg in emails:

    print "Fetching %d of %d..." % (index+1, len(emails))
    msg.fetch()
    index += 1

    if msg.body is not None:
      tokens = word_tokenize(msg.body)
      tags = pos_tag(tokens)

      for tag in tags:
        if tag[1]=='PRP' and (tag[0]=='I' or tag[0]=='i'):
          score += 1

  return score


if __name__=='__main__':


  email = raw_input("Your Email: ")
  password = getpass.getpass("Password: ")
  second_email = raw_input("Friend's Email: ")

  g = Gmail()
  g.login(email, password)

  print("Processing sent emails...")
  sent_emails = g.mailbox('[Gmail]/Sent Mail').mail(to=second_email)
  my_score = process_emails(sent_emails)

  print("Processing received emails...")
  received_emails = g.label('Archive').mail(sender=second_email)
  friend_score = process_emails(received_emails)

  if my_score > friend_score:
    print("Your friend has the upper hand!")
  elif my_score==friend_score:
    print("Nobody has the upper hand.")
  else:
    print("You have the upper hand!")

  g.logout()
