import random
import string
from argparse import ArgumentParser
import secrets
parser = ArgumentParser(prog="Password generator",description="Simple and powerful tool for creating passwords.")
parser.add_argument("-n","--numbers",default=0,help="Number of digits in pass.",type=int)
parser.add_argument("-l","--lowercase",default=0,help="Number of lowercase letters in pass.",type=int)
parser.add_argument("-u","--uppercase",default=0,help="Number of uppercase letters in pass.",type=int)
parser.add_argument("-s","--special",default=0,help="Number of special chars in pass.",type=int)
parser.add_argument("-o","--output",default=0,help="Name of text file to output the pass. If no file, output will appear in command line. Be careful, it clean all data that was in file.")
parser.add_argument("-t","--total",default=0,help="Total length of pass. If it passed, we'll ignore -n,-l,-u and -s",type=int)
args = parser.parse_args()
password=""
if args.total:
    for i in range(args.total):
        password+=str(secrets.choice(string.digits+string.ascii_uppercase+string.ascii_lowercase+string.punctuation))
else:
    password=""
    for i in range(args.numbers):
        password+=str(secrets.choice(string.digits))
    for i in range(args.lowercase):
        password+=str(secrets.choice(string.ascii_lowercase))
    for i in range(args.uppercase):
        password+=str(secrets.choice(string.ascii_uppercase))
    for i in range(args.numbers):
        password+=str(secrets.choice(string.punctuation))
password=list(password)
random.shuffle(password)
password="".join(password)
if args.output:
    with open(args.output,'w') as file:
        file.write(password)
        file.close()
else:
    print(password)
