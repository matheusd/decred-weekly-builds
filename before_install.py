#!/bin/python3

import json
import os

DST_ROOT = dstRoot = "%(ROOT_BUILD)s" % os.environ

def system(cmd):
    res = os.system(cmd)
    if res != 0:
        raise Exception("Error on cmd %s" % cmd)

def destinationPath(path):
    for k in os.environ:
        print("%s: %s", (k, os.environ[k]))
    return "%s/src/%s" % (DST_ROOT, path)

def cloneAndCheckout(repoOwner, repo, commit):
    print("Checking out %s/%s/%s" % (repoOwner, repo, commit))
    dst = destinationPath(repo)
    print(dst)
    repoURL = "https://github.com/%s/%s" % (repoOwner, repo)
    system("git clone %s %s" % (repoURL, dst))
    system("cd %s && git checkout %s" % (dst, commit))

def main():
    with open("versions.json") as f:
        versions = json.load(f)

    cloneAndCheckout(versions["dcrdRepoOwner"], "dcrd", versions["shaDcrd"])
    cloneAndCheckout(versions["dcrwRepoOwner"], "dcrwallet", versions["shaDcrwallet"])
    cloneAndCheckout(versions["decreditonRepoOwner"], "decrediton", versions["shaDecrediton"])

    print("Fixing decrediton version")
    decreditonPath = destinationPath("decrediton")

    for fname in ["/package.json", "/app/package.json"]:
        with open(decreditonPath + fname, "r") as f:
            packagejson = json.load(f)
            packagejson["version"] = packagejson["version"] + "-dev." + versions["version"]
        with open(decreditonPath + fname, "w") as f:
            json.dump(packagejson, f, indent=2)

if __name__ == "__main__":
    main()
