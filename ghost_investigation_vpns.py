#!/usr/bin/env python3
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢡⡀⢀⣠⣤⠤⠷⠤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⣀⡴⠟⠉⢠⡀⠠⢤⣄⣠⠀⠉⠻⢦⡀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠄⠀⠀⠈⢳⡞⠉⠀⠀⠀⣠⡇⢀⠄⠀⢷⡀⠀⠀⠀⠘⣶⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡟⠉⠒⠦⣄⣠⡏⠀⠀⠀⠀⢰⣿⢀⣴⣶⣦⡄⣻⠄⢀⢀⣠⣤⢧⣄⣠⠤⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣿⡋⠀⠀⠀⠀⠀⡟⠀⠀⢠⣠⠀⠀⠹⣿⣿⣿⣿⣿⠋⠀⠈⡍⠀⠀⠈⣿⠀⠀⠀⠀⠒⢦⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠀⠀⠀⣀⣀⣸⠁⠀⠀⣆⠙⣿⣆⢠⣿⣷⣿⣿⣷⠀⣠⣾⣷⡞⠀⠀⢹⣀⣀⣀⣀⠀⢸⣷⣧⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠸⡄⠀⢀⡘⢦⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣩⠇⡀⠀⢸⠀⠀⠀⠀⠉⢸⣿⣿⣿⣮⡁⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⢄⡀⠀⠀⠀⢀⣷⡸⣄⣙⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⡚⠁⢀⣞⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡴⣔⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠐⠺⡏⣍⣁⠀⣽⣿⣿⣿⣿⣿⣿⣽⣿⣯⣽⣿⣿⣿⣍⢁⡜⠉⠉⠓⢤⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠠⣷⣿⣗⡤⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠛⢤⡀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⣿⣿⣿⣿⣿⠿⢿⣿⣿⠿⢿⣿⣿⣿⣿⣷⡀⠈⣿⣿⣄⠀⣿⣿⣿⠁⠹⣿⣿⣿⣿⣿⢿⣿⣗⠀⠀⠀⠉⠂⣠⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢀⡿⡿⠉⣿⡟⠀⢸⣿⠏⠀⠀⢹⠿⠿⢿⣿⣷⣄⠚⢿⣿⣿⣿⡿⠃⢈⣹⣿⣿⣿⣿⣿⡎⢿⣿⣇⠀⠀⣶⣴⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣾⣿⡇⠀⢸⠋⠀⠀⠀⠸⠀⠀⠀⠉⠛⣿⣷⣟⣙⠿⣿⡁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⠟⢿⡏⠀⢸⠉⠁⠀⠈⢹⢿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⡇⠀⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠍⠛⢿⠷⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣆⠀⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀⠞⠀⠘⣿⣿⣟
⢸⣿⣿⣏⣿⡗⠀⠀⠀⠀⠀⠀⣠⠒⠊⠉⠉⠉⢉⣒⠦⣄⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣤⣿⣿⠿⠶⠶⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠘⣿⣷⣿⡝⠁⠀⠀⠀⠀⠀⠉⢁⠀⠀⠀⠀⠀⠀⠈⢹⣮⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⠀⠀⠀⠀⠀⠀⠈⠛⢆⠀⠀⠀⠀⠀⠀⠀⠋⢻⡇
⠀⠻⣿⣤⠁⠀⠀⠀⠀⠀⣤⠈⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⢠⡿⠁
⠀⠀⢻⣧⡀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⣼⠃⠀
⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⠀⠀⣀⡼⠁⠀⠀
⠀⠀⠀⠀⠙⢶⡀⠀⠀⠀⠀⢿⣷⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⠏⠉⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⡿⣾⢻⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⠙⠳⢤⣀⣀⣀⣠⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⠇⣿⣿⣿⣿⢳⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⠹⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣾⣿⣿⢸⣿⣿⣿⣿⡇⣿⣿⣿⢹⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣅⡿⣫⠟⣿⣿⡿⢹⡿⠿⣿⣿⣧⢸⣿⣿⣿⣿⠇⣿⣿⠇⡞⣿⡏⠉⢷⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⠟⠁⠀⡇⢸⡇⢀⣧⡤⢰⣿⡟⢸⡇⡏⢹⣿⠀⣿⡟⠀⢳⣿⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⡠⠀⠀⠁⣿⠃⢸⣿⠙⢺⣻⡗⠸⡇⠡⢸⣿⣰⠈⠀⠀⢘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⢸⠁⠀⠀⠀⣿⠀⠘⣿⡄⠀⠁⠁⠀⠃⠀⠈⣿⠿⠀⠀⠀⠘⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⢀⣏⣥⠀⠀⠀⢠⣤⠔⠀⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
VPN Investigation Tool - Sigma Cyber Ghost Edition
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import time
from urllib.parse import urlparse
import requests
import whois
from ipwhois import IPWhois
import dns.resolver
import socket
import random

try:
    from androguard.core.apk import APK
    from androguard.core.dex import DEX
    from androguard.core.analysis.analysis import Analysis
    ANDROGUARD_AVAILABLE = True
except ImportError:
    print("\033[91m[!] Androguard not found. Installing...\033[0m")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "androguard"])
    try:
        from androguard.core.apk import APK
        from androguard.core.dex import DEX
        from androguard.core.analysis.analysis import Analysis
        ANDROGUARD_AVAILABLE = True
    except ImportError:
        print("\033[91m[!] Failed to install androguard. APK analysis will be limited.\033[0m")
        ANDROGUARD_AVAILABLE = False

try:
    from virustotal_python import Virustotal
except ImportError:
    print("\033[91m[!] Virustotal-python not found. Installing...\033[0m")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "virustotal-python"])
    from virustotal_python import Virustotal

class VPNInvestigationTool:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.vt_api_key = "fb10bbc8b86b55705628b380e572209f840d1c6564b4a8ecee79258093fbdf31"
        self.abuseipdb_api_key = "9a86f9b0956ae1c50cbbfca359771f0d61cfe8b26951dfa3e6e5b842415fffa1b46d06da941da06a"
        self.social_media = {
            "Twitter": "https://twitter.com/safderkhan0800_",
            "YouTube": "https://www.youtube.com/@sigma_ghost_hacking",
            "Telegram": "https://t.me/Sigma_Cyber_Ghost",
            "GitHub": "https://github.com/sigma-cyber-ghost",
            "YouTube2": "https://www.youtube.com/@Sigma-Cyber-Ghost"
        }
        
        self.suspicious_domains = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.pw', '.cc']
        self.high_risk_countries = ['CN', 'RU', 'IR', 'KP', 'SY']  # High-risk country codes
        
    def __del__(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def print_banner(self):
        banner = """
\033[92m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢡⡀⢀⣠⣤⠤⠷⠤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⣀⡴⠟⠉⢠⡀⠠⢤⣄⣠⠀⠉⠻⢦⡀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠄⠀⠀⠈⢳⡞⠉⠀⠀⠀⣠⡇⢀⠄⠀⢷⡀⠀⠀⠀⠘⣶⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡟⠉⠒⠦⣄⣠⡏⠀⠀⠀⠀⢰⣿⢀⣴⣶⣦⡄⣻⠄⢀⢀⣠⣤⢧⣄⣠⠤⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣿⡋⠀⠀⠀⠀⠀⡟⠀⠀⢠⣠⠀⠀⠹⣿⣿⣿⣿⣿⠋⠀⠈⡍⠀⠀⠈⣿⠀⠀⠀⠀⠒⢦⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠀⠀⠀⣀⣀⣸⠁⠀⠀⣆⠙⣿⣆⢠⣿⣷⣿⣿⣷⠀⣠⣾⣷⡞⠀⠀⢹⣀⣀⣀⣀⠀⢸⣷⣧⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠸⡄⠀⢀⡘⢦⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣩⠇⡀⠀⢸⠀⠀⠀⠀⠉⢸⣿⣿⣿⣮⡁⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⢄⡀⠀⠀⠀⢀⣷⡸⣄⣙⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⡚⠁⢀⣞⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡴⣔⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠐⠺⡏⣍⣁⠀⣽⣿⣿⣿⣿⣿⣿⣽⣿⣯⣽⣿⣿⣿⣍⢁⡜⠉⠉⠓⢤⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠠⣷⣿⣗⡤⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠛⢤⡀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⣿⣿⣿⣿⣿⠿⢿⣿⣿⠿⢿⣿⣿⣿⣿⣷⡀⠈⣿⣿⣄⠀⣿⣿⣿⠁⠹⣿⣿⣿⣿⣿⢿⣿⣗⠀⠀⠀⠉⠂⣠⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢀⡿⡿⠉⣿⡟⠀⢸⣿⠏⠀⠀⢹⠿⠿⢿⣿⣷⣄⠚⢿⣿⣿⣿⡿⠃⢈⣹⣿⣿⣿⣿⣿⡎⢿⣿⣇⠀⠀⣶⣴⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣾⣿⡇⠀⢸⠋⠀⠀⠀⠸⠀⠀⠀⠉⠛⣿⣷⣟⣙⠿⣿⡁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⠟⢿⡏⠀⢸⠉⠁⠀⠈⢹⢿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⡇⠀⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠍⠛⢿⠷⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣆⠀⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀⠞⠀⠘⣿⣿⣟
⢸⣿⣿⣏⣿⡗⠀⠀⠀⠀⠀⠀⣠⠒⠊⠉⠉⠉⢉⣒⠦⣄⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣤⣿⣿⠿⠶⠶⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠘⣿⣷⣿⡝⠁⠀⠀⠀⠀⠀⠉⢁⠀⠀⠀⠀⠀⠀⠈⢹⣮⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⠀⠀⠀⠀⠀⠀⠈⠛⢆⠀⠀⠀⠀⠀⠀⠀⠋⢻⡇
⠀⠻⣿⣤⠁⠀⠀⠀⠀⠀⣤⠈⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⢠⡿⠁
⠀⠀⢻⣧⡀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⣼⠃⠀
⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⠀⠀⣀⡼⠁⠀⠀
⠀⠀⠀⠀⠙⢶⡀⠀⠀⠀⠀⢿⣷⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⠏⠉⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⡿⣾⢻⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⠙⠳⢤⣀⣀⣀⣠⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⠇⣿⣿⣿⣿⢳⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⠹⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣾⣿⣿⢸⣿⣿⣿⣿⡇⣿⣿⣿⢹⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣅⡿⣫⠟⣿⣿⡿⢹⡿⠿⣿⣿⣧⢸⣿⣿⣿⣿⠇⣿⣿⠇⡞⣿⡏⠉⢷⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⠟⠁⠀⡇⢸⡇⢀⣧⡤⢰⣿⡟⢸⡇⡏⢹⣿⠀⣿⡟⠀⢳⣿⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⡠⠀⠀⠁⣿⠃⢸⣿⠙⢺⣻⡗⠸⡇⠡⢸⣿⣰⠈⠀⠀⢘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⢸⠁⠀⠀⠀⣿⠀⠘⣿⡄⠀⠁⠁⠀⠃⠀⠈⣿⠿⠀⠀⠀⠘⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⢀⣏⣥⠀⠀⠀⢠⣤⠔⠀⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[0m
        """
        print(banner)
        print("\033[94m" + "="*80 + "\033[0m")
        print("\033[93m           VPN INVESTIGATION TOOL - SIGMA CYBER GHOST EDITION\033[0m")
        print("\033[94m" + "="*80 + "\033[0m")
        print("\033[92m[+] Author: Sigma Cyber Ghost\033[0m")
        print("\033[92m[+] Specialized in Security Research & Black Hat Hacking\033[0m")
        print("\033[94m" + "="*80 + "\033[0m")
        
    def print_social_media(self):
        print("\n\033[93m[+] Follow me on:\033[0m")
        for platform, url in self.social_media.items():
            print(f"\033[96m    {platform}: {url}\033[0m")
        print("\033[94m" + "="*80 + "\033[0m")
    
    def typing_effect(self, text, speed=0.005):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()
    
    def extract_apk(self, apk_path):
        """Extract APK file and analyze its contents"""
        if not ANDROGUARD_AVAILABLE:
            print("\033[91m[!] Androguard is not available. APK analysis is disabled.\033[0m")
            return [], []
            
        print(f"\033[92m[+] Analyzing APK: {apk_path}\033[0m")
        
        file_size = os.path.getsize(apk_path)
        with open(apk_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        print(f"\033[96m    File Size: {file_size} bytes\033[0m")
        print(f"\033[96m    SHA-256: {file_hash}\033[0m")
        
        try:
            apk = APK(apk_path)
            print(f"\033[96m    Package Name: {apk.get_package()}\033[0m")
            print(f"\033[96m    Version: {apk.get_androidversion_name()}\033[0m")
            
            permissions = apk.get_permissions()
            print(f"\n\033[92m[+] App Permissions ({len(permissions)}):\033[0m")
            for perm in permissions:
                print(f"\033[96m    {perm}\033[0m")
            
            endpoints = self.extract_endpoints_from_apk(apk_path)
            print(f"\n\033[92m[+] Found {len(endpoints)} potential endpoints:\033[0m")
            for endpoint in endpoints:
                print(f"\033[96m    {endpoint}\033[0m")
            
            suspicious_perms = self.analyze_permissions(permissions)
            if suspicious_perms:
                print(f"\n\033[91m[!] Suspicious permissions detected:\033[0m")
                for perm in suspicious_perms:
                    print(f"\033[91m    {perm}\033[0m")
            
            return endpoints, permissions
            
        except Exception as e:
            print(f"\033[91m[!] Error analyzing APK: {e}\033[0m")
            return [], []
    
    def extract_endpoints_from_apk(self, apk_path):
        """Extract endpoints from APK files"""
        endpoints = set()
        
        if ANDROGUARD_AVAILABLE:
            try:
                apk = APK(apk_path)
                dex_files = apk.get_all_dex()
                
                for dex in dex_files:

                    url_pattern = r'https?://[^\s<>"{}|\\^`[\]]+'
                    matches = re.findall(url_pattern, dex)
                    for match in matches:
                        endpoints.add(match)
            except Exception as e:
                print(f"\033[91m    Error analyzing APK with androguard: {e}\033[0m")
        

        try:
            with zipfile.ZipFile(apk_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
                
            for root, dirs, files in os.walk(self.temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if file.endswith(('.xml', '.json', '.txt', '.html', '.js')):
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                                url_pattern = r'https?://[^\s<>"{}|\\^`[\]]+'
                                matches = re.findall(url_pattern, content)
                                for match in matches:
                                    endpoints.add(match)
                                    
                                ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
                                domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
                                
                                ip_matches = re.findall(ip_pattern, content)
                                domain_matches = re.findall(domain_pattern, content)
                                
                                for ip in ip_matches:
                                    if not any(octet.startswith('0') and len(octet) > 1 for octet in ip.split('.')):
                                        endpoints.add(ip)
                                
                                for domain in domain_matches:
                                    if not domain.endswith(('.android', '.com.android', '.xml', '.so')) and len(domain) > 4:
                                        endpoints.add(domain)
                                        
                    except (UnicodeDecodeError, IsADirectoryError, PermissionError):

                        continue
        except Exception as e:
            print(f"\033[91m    Error extracting APK: {e}\033[0m")
        
        return list(endpoints)
    
    def analyze_permissions(self, permissions):
        """Identify suspicious permissions"""
        suspicious_perms = []
        risky_permissions = [
            'android.permission.ACCESS_NETWORK_STATE',
            'android.permission.INTERNET',
            'android.permission.READ_PHONE_STATE',
            'android.permission.ACCESS_WIFI_STATE',
            'android.permission.CHANGE_WIFI_STATE',
            'android.permission.RECEIVE_BOOT_COMPLETED',
            'android.permission.WAKE_LOCK',
            'android.permission.VIBRATE',
            'android.permission.FOREGROUND_SERVICE',
            'android.permission.REQUEST_INSTALL_PACKAGES',
            'android.permission.SYSTEM_ALERT_WINDOW',
            'android.permission.WRITE_SETTINGS'
        ]
        
        for perm in permissions:
            if perm in risky_permissions:
                suspicious_perms.append(perm)
                
        return suspicious_perms
    
    def investigate_server(self, server_address):
        """Investigate a VPN server"""
        print(f"\033[92m[+] Investigating server: {server_address}\033[0m")
        
        if self.is_ip_address(server_address):
            return self.investigate_ip(server_address)
        else:
            return self.investigate_domain(server_address)
    
    def is_ip_address(self, address):
        """Check if the address is an IP"""
        ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        return re.match(ip_pattern, address) is not None
    
    def investigate_ip(self, ip_address):
        """Investigate an IP address"""
        print(f"\033[96m    IP Address: {ip_address}\033[0m")
        
        try:
            ipwhois = IPWhois(ip_address)
            results = ipwhois.lookup_rdap()
            country = results.get('asn_country_code', 'Unknown')
            asn = results.get('asn', 'Unknown')
            description = results.get('asn_description', 'Unknown')
            
            print(f"\033[96m    Country: {country}\033[0m")
            print(f"\033[96m    ASN: {asn}\033[0m")
            print(f"\033[96m    Description: {description}\033[0m")
            
            if country in self.high_risk_countries:
                print(f"\033[91m    [!] HIGH RISK: Server is located in a high-risk country: {country}\033[0m")
                
        except Exception as e:
            print(f"\033[91m    Geolocation lookup failed: {e}\033[0m")
            country = 'Unknown'
        
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            print(f"\033[96m    Reverse DNS: {hostname}\033[0m")
            
            for suspicious_domain in self.suspicious_domains:
                if suspicious_domain in hostname:
                    print(f"\033[91m    [!] SUSPICIOUS: Reverse DNS contains suspicious domain: {suspicious_domain}\033[0m")
                    
        except socket.herror:
            print(f"\033[96m    Reverse DNS: No PTR record found\033[0m")
            hostname = None
        
        vpn_ports = [1194, 443, 992, 5555, 8080, 53]
        open_ports = []
        for port in vpn_ports:
            if self.check_port(ip_address, port):
                open_ports.append(port)
        
        if open_ports:
            print(f"\033[96m    Open VPN ports: {open_ports}\033[0m")
        else:
            print(f"\033[96m    No standard VPN ports open\033[0m")
        
        vt_malicious = 0
        if self.vt_api_key:
            vt_malicious = self.virustotal_check(ip_address, 'ip')
        else:
            print("\033[91m    VirusTotal check skipped (no API key)\033[0m")
        
        abuse_score = 0
        if self.abuseipdb_api_key:
            abuse_score = self.abuseipdb_check(ip_address)
        else:
            print("\033[91m    AbuseIPDB check skipped (no API key)\033[0m")
        
        self.assess_risk_level(ip_address, country, vt_malicious, abuse_score, hostname)
        
        return True
    
    def investigate_domain(self, domain):
        """Investigate a domain"""
        print(f"\033[96m    Domain: {domain}\033[0m")
        
        for suspicious_domain in self.suspicious_domains:
            if suspicious_domain in domain:
                print(f"\033[91m    [!] SUSPICIOUS: Domain contains suspicious TLD: {suspicious_domain}\033[0m")
        
        try:
            a_records = dns.resolver.resolve(domain, 'A')
            print(f"\033[96m    A Records:\033[0m")
            for rdata in a_records:
                print(f"\033[96m        {rdata.address}\033[0m")
                self.investigate_ip(rdata.address)
        except Exception as e:
            print(f"\033[91m    DNS A record lookup failed: {e}\033[0m")
        
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            print(f"\033[96m    MX Records:\033[0m")
            for rdata in mx_records:
                print(f"\033[96m        {rdata.exchange}\033[0m")
        except Exception as e:
            pass
        
        try:
            w = whois.whois(domain)
            print(f"\033[96m    Registrar: {w.registrar}\033[0m")
            print(f"\033[96m    Creation Date: {w.creation_date}\033[0m")
            print(f"\033[96m    Expiration Date: {w.expiration_date}\033[0m")
            if w.name_servers:
                print(f"\033[96m    Name Servers: {w.name_servers}\033[0m")
                
            if hasattr(w.creation_date, '__iter__'):
                creation_date = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
            else:
                creation_date = w.creation_date
                
            if creation_date:
                from datetime import datetime
                if isinstance(creation_date, str):
                    try:
                        creation_date = datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
                    except:
                        creation_date = None
                
                if creation_date and (datetime.now() - creation_date).days < 30:
                    print(f"\033[91m    [!] SUSPICIOUS: Domain was created recently: {creation_date}\033[0m")
                    
        except Exception as e:
            print(f"\033[91m    WHOIS lookup failed: {e}\033[0m")
        
        vt_malicious = 0
        if self.vt_api_key:
            vt_malicious = self.virustotal_check(domain, 'domain')
        else:
            print("\033[91m    VirusTotal check skipped (no API key)\033[0m")
        
        return True
    
    def check_port(self, ip, port):
        """Check if a port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except socket.error:
            return False
    
    def virustotal_check(self, resource, resource_type):
        """Check resource on VirusTotal"""
        try:
            vtotal = Virustotal(API_KEY=self.vt_api_key)
            
            if resource_type == 'ip':
                resp = vtotal.request(f"ip_addresses/{resource}")
            elif resource_type == 'domain':
                resp = vtotal.request(f"domains/{resource}")
            else:
                return 0
            
            stats = resp.data.get('attributes', {}).get('last_analysis_stats', {})
            malicious = stats.get('malicious', 0)
            harmless = stats.get('harmless', 0)
            suspicious = stats.get('suspicious', 0)
            
            print(f"\033[96m    VirusTotal Detection: {malicious} engines detected this as malicious\033[0m")
            print(f"\033[96m    VirusTotal Results: {harmless} harmless, {suspicious} suspicious\033[0m")
            
            return malicious
            
        except Exception as e:
            print(f"\033[91m    VirusTotal check failed: {e}\033[0m")
            return 0
    
    def abuseipdb_check(self, ip_address):
        """Check IP on AbuseIPDB"""
        try:
            url = 'https://api.abuseipdb.com/api/v2/check'
            headers = {
                'Key': self.abuseipdb_api_key,
                'Accept': 'application/json',
            }
            params = {
                'ipAddress': ip_address,
                'maxAgeInDays': 90
            }
            
            response = requests.get(url, headers=headers, params=params)
            data = response.json().get('data', {})
            
            abuse_confidence = data.get('abuseConfidenceScore', 0)
            total_reports = data.get('totalReports', 0)
            
            print(f"\033[96m    AbuseIPDB Score: {abuse_confidence}% (higher is more suspicious)\033[0m")
            print(f"\033[96m    AbuseIPDB Reports: {total_reports}\033[0m")
            
            return abuse_confidence
            
        except Exception as e:
            print(f"\033[91m    AbuseIPDB check failed: {e}\033[0m")
            return 0
    
    def assess_risk_level(self, ip, country, vt_malicious, abuse_score, hostname=None):
        """Assess the overall risk level of the server"""
        risk_factors = []
        
        if country in self.high_risk_countries:
            risk_factors.append(f"Located in high-risk country: {country}")
            
        if vt_malicious > 0:
            risk_factors.append(f"Detected as malicious by {vt_malicious} engines")
            
        if abuse_score > 25:
            risk_factors.append(f"High abuse score: {abuse_score}%")
            
        if hostname:
            for suspicious_domain in self.suspicious_domains:
                if suspicious_domain in hostname:
                    risk_factors.append(f"Suspicious domain in reverse DNS: {suspicious_domain}")
        
        if risk_factors:
            print(f"\033[91m[!] SECURITY ALERT: {len(risk_factors)} risk factors detected:\033[0m")
            for factor in risk_factors:
                print(f"\033[91m    - {factor}\033[0m")
                
            if len(risk_factors) >= 2:
                print(f"\033[91m[!] WARNING: This server appears to be HIGH RISK!\033[0m")
            else:
                print(f"\033[93m[!] CAUTION: This server has some risk factors\033[0m")
        else:
            print(f"\033[92m[+] No significant risk factors detected\033[0m")
    
    def analyze_network_traffic(self, endpoints):
        """Analyze network traffic patterns from endpoints"""
        print(f"\n\033[92m[+] Analyzing network traffic patterns\033[0m")
        
        suspicious_patterns = []
        for endpoint in endpoints:

            if endpoint.startswith('http://'):
                suspicious_patterns.append(f"Insecure HTTP endpoint: {endpoint}")
            

            for suspicious_domain in self.suspicious_domains:
                if suspicious_domain in endpoint:
                    suspicious_patterns.append(f"Suspicious domain in endpoint: {endpoint}")
        
        if suspicious_patterns:
            print(f"\033[91m[!] Found {len(suspicious_patterns)} suspicious patterns:\033[0m")
            for pattern in suspicious_patterns:
                print(f"\033[91m    {pattern}\033[0m")
        else:
            print(f"\033[92m    No obvious suspicious network patterns detected\033[0m")
        
        return suspicious_patterns

def main():
    tool = VPNInvestigationTool()
    tool.print_banner()
    
    parser = argparse.ArgumentParser(description='VPN Investigation Tool - Sigma Cyber Ghost Edition')
    parser.add_argument('--apk', help='Path to VPN APK file for analysis')
    parser.add_argument('--server', help='VPN server address (IP or domain) to investigate')
    
    args = parser.parse_args()
    
    if not args.apk and not args.server:
        tool.typing_effect("\033[91m[!] Error: You must specify either an APK file or a server address to investigate\033[0m")
        parser.print_help()
        tool.print_social_media()
        sys.exit(1)
    
    tool.typing_effect("\033[92m[+] Initializing Sigma Cyber Ghost VPN Investigation Tool...\033[0m")
    time.sleep(1)
    tool.typing_effect("\033[92m[+] Loading threat intelligence databases...\033[0m")
    time.sleep(1)
    tool.typing_effect("\033[92m[+] Activating security protocols...\033[0m")
    time.sleep(1)
    print("\033[94m" + "="*80 + "\033[0m")
    
    endpoints = []
    if args.apk:
        if not os.path.isfile(args.apk):
            tool.typing_effect(f"\033[91m[!] Error: APK file not found: {args.apk}\033[0m")
            sys.exit(1)
        
        endpoints, permissions = tool.extract_apk(args.apk)
        if endpoints:
            tool.analyze_network_traffic(endpoints)
    
    if args.server:
        tool.investigate_server(args.server)
    
    print("\033[94m" + "="*80 + "\033[0m")
    tool.typing_effect("\033[92m[+] Investigation completed successfully!\033[0m")
    tool.typing_effect("\033[92m[+] Stay secure with Sigma Cyber Ghost!\033[0m")
    tool.print_social_media()

if __name__ == "__main__":
    main()
