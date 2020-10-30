import argparse
import requests

# use arparse to  structure input and output file
#url = "https://verify-email.org/home/verify-as-guest/"


def ade():
    parser = argparse.ArgumentParser(description='validate list of emails  using a wordlist')
    parser.add_argument('-w', help='wordlist', required=True)
    parser.add_argument('-o', help='outfile')

    # usage file.py -w wordlist -o outfile or file.py --wordlist word --outfile outfile
    args = parser.parse_args()
    # print(args)
    # print(args.w)
    # print(args.o)
    opt1 = args.w
    opt2 = args.o
    #    return opt1, opt2
    infile = open(opt1, "r")
    files = infile.readlines()
    for file in files:
        # print(file.rstrip())
        email = file.rstrip()
        if email.__contains__("@"):
            url = "https://verify-email.org/home/verify-as-guest/"
            url_new = url + email
            r = requests.get(url_new)
            result = r.json()
            if result['response']['status'] == 'success':
                print(email + " =====>valid email")
            else:
                print(email + " not valid ")
        else:
            print(email + " ===>> not valid")


ade()
