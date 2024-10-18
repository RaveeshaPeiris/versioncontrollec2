import sys

def dog():
    print("baw")

def default():
    print('hello')

def main () :
    default()

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__' :
    main()
