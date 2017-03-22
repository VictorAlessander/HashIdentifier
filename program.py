# coding: UTF-8


import requests
from bs4 import BeautifulSoup as BSoup
import sys


class HashIdentifier(object):

    def __init__(self, hashc):
        self.hashc = hashc


    def decrypter(self):

        # Using Gromweb
        self.content = requests.get(
            'https://md5.gromweb.com/?md5=' + self.hashc)

        self.soup = BSoup(self.content.text, "html.parser")

        self.hashresult = self.soup.find('em', attrs={'class': 'long-content string'})

        if self.hashresult is not None:
            return self.hashresult.text


if __name__ == '__main__':
    hash1 = HashIdentifier(sys.argv[1])
    
    if hash1 is not True:
        print("[*] Gromweb\t\t[-] Not Found")

    else:
        print("[*] Gromweb\t\t[+] Found: {}" .format(hash1.decrypter()))