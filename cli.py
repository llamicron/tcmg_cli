"""CLI.py

Usage:
    cli.py add <x> <y>
    cli.py subtract <x> <y>
    cli.py walk [right | left] <distance>
"""

# import docopt (remember to install it)
from docopt import docopt

def run():
    # Make a dictionary from the arguments
    args = docopt(__doc__, version="0.1.0")
    # When debugging, it's very use to print the args dictionary to see what's in it,
    # uncomment this while developing
    # print(args)


    # If the command is "add"
    if args['add']:
        # Cast these to an int or a float, from a string.
        x = float(args['<x>'])
        y = float(args['<y>'])
        # Print the sum
        print(x + y)

    # This is the same as above...
    if args['subtract']:
        x = float(args['<x>'])
        y = float(args['<y>'])
        # ... but print the difference instead of the sum
        print(x - y)

    # If the command is walk
    if args['walk']:
        # If they provided 'right'
        if args['right']:
            # Print this message and also the distance variable
            print("you walked right " + args['<distance>'])
        # If they provided 'left
        if args['left']:
            # Print this message and also the distance variable
            print("you walked left " + args['<distance>'])

if __name__ == '__main__':
    # When they run the file, run this method
    run()

