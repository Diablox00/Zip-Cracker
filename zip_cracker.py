import zipfile
import optparse
import threading
from termcolor import colored

def crack(zfile, password):
    try:
        hacked = zfile.extractall(pwd=password.encode())
        print(colored(f"[+] Password Found: {hacked}", "green"))

    except Exception as e:
        pass


def main():
    parsed = optparse.OptionParser(colored("[+] Usage: \n -f : <zipfile> \n -d : <Dictionary file>", "red"))
    parsed.add_option("-f", dest="fname", type="string", help="Path to zipfile")
    parsed.add_option("-d", dest="dname", type="string", help="Path to dictionary")
    (options, args) = parsed.parse_args()

    if options.fname is None or options.dname is None:
        print(parsed.usage)
        exit(0)
    else:
        fname = options.fname
        dname = options.dname
        zfile = zipfile.ZipFile(fname)
        dfile = open(dname)

        for line in dfile:
            word = line.strip("\n")
            t = threading.Thread(target=crack, args=(zfile, word))
            t.start()


if __name__ == "__main__":
    main()
