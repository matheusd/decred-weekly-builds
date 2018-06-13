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

    print("Checking out %s/dcrd/%s" % (versions["dcrdRepoOwner"], versions["shaDcrd"]))
    system("git clone https://github.com/%s/dcrd %%(GOPATH)s/src/github.com/decred/dcrd" % versions["dcrdRepoOwner"])
    system("cd %(GOPATH)s/src/github.com/decred/dcrd && git checkout " + versions["shaDcrd"])

    print("Checking out %s/dcrwallet/%s ", (versions["dcrwRepoOwner"], versions["shaDcrwallet"]))
    system("git clone https://github.com/%s/dcrwallet %%(GOPATH)s/src/github.com/decred/dcrd" % versions["dcrwRepoOwner"])
    system("cd %(GOPATH)s/src/github.com/decred/dcrwallet && git checkout " + versions["shaDcrwallet"])

    print("Checking out %s/decrediton/%s ", (versions["decreditonRepoOwner"], versions["shaDecrediton"]))
    system("git clone https://github.com/%s/decrediton %%(GOPATH)s/src/github.com/decred/decrediton" % versions["decreditonRepoOwner"])
    system("cd %(GOPATH)s/src/github.com/decred/decrediton && git checkout " + versions["shaDecrediton"])

    print("Fixing decrediton version")
    decreditonPath = "%(GOPATH)s/src/github.com/decred/decrediton" % os.environ

    for fname in ["/package.json", "/app/package.json"]:
        with open(decreditonPath + fname, "r") as f:
            packagejson = json.load(f)
            packagejson["version"] = packagejson["version"] + "-dev." + versions["version"]
        with open(decreditonPath + fname, "w") as f:
            json.dump(packagejson, f, indent=2)

if __name__ == "__main__":
    main()
