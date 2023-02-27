import hashlib
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-c","--cypher",help="hash to crack")
parser.add_argument("-a","--algorithm",help="hash type(md5, sha1, sha256)")
parser.add_argument("-w","--wordlist",help="wordlist")
args = parser.parse_args()
wordlist = open(args.wordlist, "r").readlines()

for word in wordlist:
    word = word.strip() #kelimenin sağındaki ve solundaki boşlukları kaldırır
    if args.algorithm == "md5":
        crack = hashlib.md5(word.encode("utf-8")).hexdigest()
    elif args.algorithm == "sha1":
        crack = hashlib.sha1(word.encode("utf-8")).hexdigest()
    elif args.algorithm == "sha256":
        crack = hashlib.sha256(word.encode("utf-8")).hexdigest()
    else:
        print("Cracking failed!. '--help' for documentation")
    if crack == args.cypher:
        print("\tCracking Successful!: "+word)
        break

if crack != args.cypher:
    print("Cracking Failed!(wordlist is not enough)")
    