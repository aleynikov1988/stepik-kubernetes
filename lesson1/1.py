import os


def main(secret):
    print("Hello %s" % secret)

main(os.environ.get("SECRET", "Python"))