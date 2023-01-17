#!/usr/bin/env python3

__author__ = "19BCY10145"

import PyInstaller.__main__ as pyinstaller


"""Set up the arguments required by PyInstaller to build the Network
Packet Sniffer binary."""
pyinstaller.run(("packet_sniffer/core.py", "--onefile"))
