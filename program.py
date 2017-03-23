# coding: UTF-8


import requests
from bs4 import BeautifulSoup as BSoup
import sys


class HashIdentifier(object):

    def __init__(self, hashc):
        self.hashc = hashc


    def avaliate(self):
        if len(self.hashc) == 32:
            print("[*] Hash MD5 Identified!")

        else:
            print("[!] Invalid Hash MD5")
            sys.exit()


    def decrypt(self):

        # Using Gromweb
        self.content = requests.get(
            'https://md5.gromweb.com/?md5=' + self.hashc)

        self.soup = BSoup(self.content.text, "html.parser")

        self.hashresult = self.soup.find('em', attrs={'class': 'long-content string'})

        if self.hashresult:
            return self.hashresult.text


if __name__ == '__main__':
    hash1 = HashIdentifier(sys.argv[1])

    hash1.avaliate()

    if hash1.decrypt():
        print("[*] Gromweb\t\t[+] Found: {}" .format(hash1.decrypt()))

    else:
        print("[*] Gromweb\t\t[-] Not Found")