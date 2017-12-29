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

    print("Checking out dcrd " + versions["shaDcrd"])
    system("cd %(GOPATH)s/src/github.com/decred/dcrd && git checkout " + versions["shaDcrd"])

    print("Checking out dcrwallet " + versions["shaDcrwallet"])
    system("cd %(GOPATH)s/src/github.com/decred/dcrwallet && git checkout " + versions["shaDcrwallet"])

    print("Checking out decrediton " + versions["shaDecrediton"])
    system("cd %(GOPATH)s/src/github.com/decred/decrediton && git checkout " + versions["shaDecrediton"])

    print("Fixing decrediton version")
    decreditonPath = "%(GOPATH)s/src/github.com/decred/decrediton" % os.environ
    with open(decreditonPath + "/package.json") as f:
        packagejson = json.load(f)
        packagejson["version"] = packagejson["version"] + "-dev" + versions["version"]
        f.truncate()
        json.dump(packagejson, f, indent=2)

if __name__ == "__main__":
    main()
