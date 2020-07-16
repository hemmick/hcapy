#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import CDLL
from subprocess import Popen, PIPE
import os

def funcrawl(pth: str) -> list:
    out = Popen (
            args="nm" + " " + os.path.abspath(pth),
            shell=True,
            stdout=PIPE
            ).communicate()[0].decode("utf-8")
    attrs = [
            i.split(" ")[-1].replace("\r","")
            for i in out.split("\n") if " T zw" in i
            ]

    return [i for i in attrs if hasattr(CDLL(pth), i)]
