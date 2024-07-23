import sys
from shiv_cli.now import currentdate


def main(argv):
    if len(argv) != 1:
        print("Usage: shiv_cli <name>")
        sys.exit(1)

    name = argv[0]
    print(f"Hello, {name}!")
    print(f"Today's date is {currentdate()}.")


if __name__ == '__main__':
    main(sys.argv[1:])
