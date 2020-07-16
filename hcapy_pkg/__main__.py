#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import ctypes
from pprint import pprint
from hcapy_pkg import funcrawler

dllname="libhcapy.so"

_DIRNAME = os.path.dirname(os.path.abspath(__file__))
_PARENTPATH = os.path.abspath(_DIRNAME + os.path.sep + "..")
_DLLPATH = os.path.abspath(_PARENTPATH + os.path.sep + "lib" + os.path.sep + dllname)
_hcapi = ctypes.CDLL(_DLLPATH)


def main() -> None:
    print("Executing " + __name__);
    print("_DLLPATH: " + _DLLPATH);
    print("Found functions: ")
    pprint(funcrawler.funcrawl(_DLLPATH));

if __name__ == "__main__":
    main()

