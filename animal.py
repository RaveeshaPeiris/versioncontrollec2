import sys

def dog():
    print("baw")

def cat():
    print("meow")

def default():
    print('hello')

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'dog':
        dog()
    elif len(sys.argv) > 1 and sys.argv[1] == 'cat':
        cat()
    else:
        default()
        
if __name__ == '__main__':
    main()
