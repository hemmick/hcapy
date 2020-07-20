#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
from pprint import pprint

def callback(gw_addr: bytearray, gw_addr_cnt: int, is_ipv4: bool, usr_param, rpt_num: int, total_rpt: int, gw_name_array) -> None:
    print("received CB")
    pprint(gw_addr)
    pprint(gw_addr_cnt)
    pprint(is_ipv4)
    pprint(usr_param)
    pprint(rpt_num)
    pprint(total_rpt)
    pprint(gw_name_array)
