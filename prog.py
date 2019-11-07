import sys


def main():
    print('Command Line Arguments')
    print('Total Arguments : ' + str(len(sys.argv)))
    for arg in sys.argv:
        print(arg)


main()
