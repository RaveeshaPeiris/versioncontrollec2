import sys

def cat():
    print("meow")

def default():
    print('hello')

def main () :
    default()

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__' :
    main()
