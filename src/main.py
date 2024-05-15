"""The entry point of the application."""

import sys

from src.example import greeting


def main():
    name: str
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        name = input("Enter your name: ")
    print(greeting(name))


if __name__ == "__main__":
    main()
