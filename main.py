import argparse
from ast import parse

def main():
    print(parse_arguments())

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
