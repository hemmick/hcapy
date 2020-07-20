#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
from ctypes import c_char,c_char_p,c_int,c_int8,c_uint8,c_void_p,POINTER,c_buffer,c_bool,c_byte,CDLL,CFUNCTYPE,Structure,sizeof
from pprint import pprint
from hcapy_pkg import funcrawler
from hcapy_pkg import discover_gw

dllname="libhcapy.so"

_DIRNAME = os.path.dirname(os.path.abspath(__file__))
_PARENTPATH = os.path.abspath(_DIRNAME + os.path.sep + "..")
_DLLPATH = os.path.abspath(_PARENTPATH + os.path.sep + "lib" + os.path.sep + dllname)
_hcapi = CDLL(_DLLPATH)

py_gw_disco_t = CFUNCTYPE(None, POINTER(c_char), c_char, c_int, c_void_p, c_int, c_int, POINTER(c_char))
py_gw_disco_cb = py_gw_disco_t(discover_gw.callback)

def main() -> None:
    print("Executing " + __name__);
    print("_DLLPATH: " + _DLLPATH);
    print("Found functions: ")
    pprint(funcrawler.funcrawl(_DLLPATH));
    print("attempting to call zwnet_gw_discvr_start in DLL...")
    
    _hcapi.zwnet_gw_discvr_start.argtypes = [py_gw_disco_t, c_void_p, c_int, c_int]
    _hcapi.zwnet_gw_discvr_start.restype = c_void_p

    bytebuf = c_void_p()

    result = _hcapi.zwnet_gw_discvr_start(py_gw_disco_cb,  bytebuf, True, 1)

    print("context returned: " + str(result))
    
    foo = input("press any key to quit: ")

    if result != 0:
        print("stoping discovery for context:" + str(result) + "...")
        _hcapi.zwnet_gw_discvr_stop.argtypes = [c_void_p]
        _hcapi.zwnet_gw_discvr_stop.restype = c_int

        result = _hcapi.zwnet_gw_discvr_stop(result)
        if result != 0:
            print("successful...")
        else:
            print("zwnet_gw_disvr_stop returned:" + str(result))

if __name__ == "__main__":
    main()

