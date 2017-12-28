#!/bin/python

import json
import os

def system(cmd):
    res = os.system(cmd.format(os.environ))
    if res != 0:
        raise Exception("Error on cmd %s" % cmd)

def main():
    with open("versions.json") as f:
        versions = json.load(f)

    os.makedirs("{GOPATH}/src/github.com/decred/dcrd".format(os.environ))
    system("git clone https://github.com/decred/dcrd {GOPATH}/src/github.com/decred/dcrd")
    system("git clone https://github.com/decred/dcrwallet {GOPATH}/src/github.com/decred/dcrwallet")
    system("cd {GOPATH}/src/github.com/decred/dcrd && dep ensure && go build")
    system("cd {GOPATH}/src/github.com/decred/dcrwallet && dep ensure && go build")


if __name__ == "__main__":
    main()
