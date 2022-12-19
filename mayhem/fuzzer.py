#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from ping3 import ping, verbose_ping


@atheris.instrument_func
def test_input(data):
    ping(data)
    verbose_ping(data)
    return

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
