# Ghost-Investigation-VPNs 🔍

**A powerful Black Hat Edition tool for analyzing VPN applications and servers to detect potential security risks, data collection practices, and malicious activities.**

## 🌟 Features

- **APK Analysis**: Extract and examine VPN Android applications
- **Server Investigation**: Analyze VPN server infrastructure and geolocation
- **Threat Intelligence**: Integration with VirusTotal and AbuseIPDB
- **Network Traffic Analysis**: Identify suspicious patterns
- **Security Risk Assessment**: Comprehensive risk scoring system
- **Black Hat Style Interface**: Professional hacker-themed UI

## 📦 Installation
```
git clone https://github.com/sigma-cyber-ghost/Ghost-Investigation-VPNs
pip3 install androguard virustotal-python python-whois ipwhois dnspython requests
cd Ghost-Investigation-VPNs
```
## 🚀 📖 Usage Examples
Analyzing a VPN APK
```
python3 ghost_investigation_vpns.py --apk /path/to/vpn-app.apk
```

**Investigating a VPN Server**
```
python3 ghost_investigation_vpns.py --server vpn.example.com
```

**Combined Analysis**
```
python3 ghost_investigation_vpns.py --apk /path/to/vpn-app.apk --server vpn.example.com
```

## 🔧 Command Line Arguments
Argument	Description	Required
--apk	Path to VPN APK file for analysis	Optional
--server	VPN server address (IP or domain) to investigate	Optional

## 📊 Output Interpretation

**Risk Levels**
🟢 Low Risk: No significant risk factors detected

🟡 Medium Risk: 1-2 risk factors present

🔴 High Risk: 3+ risk factors or critical issues

Common Risk Factors
Server located in high-risk country (CN, RU, IR, KP, SY)

Suspicious domain TLDs (.tk, .ml, .ga, .cf, .gq, .xyz, .top)

Recent domain registration (<30 days)

Multiple virus detection engines flagging as malicious

High abuse confidence score (>25%)

## 🌐 Connect With Us

[![Telegram](https://img.shields.io/badge/Telegram-Sigma_Ghost-blue?logo=telegram)](https://t.me/Sigma_Cyber_Ghost)  [![YouTube](https://img.shields.io/badge/YouTube-Sigma_Ghost-red?logo=youtube)](https://www.youtube.com/@sigma_ghost_hacking)  [![Instagram](https://img.shields.io/badge/Instagram-Safder_Khan-purple?logo=instagram)](https://www.instagram.com/safderkhan0800_/)  [![Twitter](https://img.shields.io/badge/Twitter-@safderkhan0800_-1DA1F2?logo=twitter)](https://twitter.com/safderkhan0800_)[![YouTube](https://img.shields.io/badge/YouTube-Sigma_Ghost-red?logo=youtube)](https://www.youtube.com/@Sigma-Cyber-Ghost) 
