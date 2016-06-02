import sys
import imaplib
import getpass
import email
import datetime

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    M.login('notatallawhistleblowerIswear@gmail.com',getpass.getpass())
except imaplib.IMAP4.error:
     print "LOGIN FAILED!!!"
     