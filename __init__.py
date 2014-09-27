__author__ = 'Morteza Ansarinia'

from gmail import Gmail
import getpass

email = raw_input("Your Email: ")
my_password = getpass.getpass("Password: ")
second_email = raw_input("Friend's Email: ")

g = Gmail()
g.login(email, my_password)

emails = g.mailbox('[Gmail]/Sent Mail').mail(to=second_email)

g.logout()
print("Logged out")
