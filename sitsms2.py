#!/usr/bin/python

import sitsms

def main():
    txt = 'hello main'
    sitsms.loginsite()
    sitsms.sendsms('8015376450',txt)

if __name__ == '__main__':
    main()

