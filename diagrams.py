import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('type', help="circle or radial diagram", choices=['radial', 'circle'])
args = arg_parser.parse_args()


def type1():
    print("1st type")

def type2():
    print("2nd type")

types = {
    'circle':type1,
    'radial':type2
}

if __name__ == "__main__":
    types[args.type]()