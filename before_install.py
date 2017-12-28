#!/bin/python3

import json
import os

def system(cmd):
    res = os.system(cmd % os.environ)
    if res != 0:
        raise Exception("Error on cmd %s" % cmd)

def main():
    with open("versions.json") as f:
        versions = json.load(f)

    system("cd %(GOPATH)s/src/github.com/decred/dcrd && dep ensure && go build")
    system("cd %(GOPATH)s/src/github.com/decred/dcrwallet && dep ensure && go build")


if __name__ == "__main__":
    main()
