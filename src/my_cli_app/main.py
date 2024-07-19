import sys


def main(argv):
    if len(argv) != 1:
        print("Usage: my_cli_app <name>")
        sys.exit(1)

    name = argv[0]
    print(f"Hello, {name}!")


if __name__ == '__main__':
    main(sys.argv[1:])
