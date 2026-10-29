# Phishing URL Awareness Checker

## Overview
A beginner-friendly Python cybersecurity mini-project that checks the *text* of a URL for a few warning signs commonly discussed in phishing awareness.

**Important:** This is an educational checklist, not a phishing detector or a guarantee of safety. It does not open URLs, visit websites, send data, or scan website content.

## Features
- Checks for an `@` symbol.
- Flags URLs longer than 100 characters.
- Detects an IP address used as the hostname.
- Flags hostnames with 5 or more dot-separated segments.
- Detects the `xn--` punycode marker.
- Flags URLs using HTTP instead of HTTPS.
- Handles some malformed or empty input.
- Allows repeated checks; type `quit` to exit.

## Requirements
- Python 3.10 or newer
- No third-party packages required

## Run the project
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   **Windows**
   ```bash
   python phishing_checker.py
   ```

   **macOS/Linux**
   ```bash
   python3 phishing_checker.py
   ```

4. Enter a URL to check. Type `quit` to exit.

## Example
Input:
```text
http://192.0.2.10/account
```
Expected warning signs:
- Hostname is an IP address rather than a typical domain name.
- Uses HTTP rather than HTTPS.

## Test samples
See [`tests/test_samples.md`](tests/test_samples.md) for sample inputs and expected warning signs. Record the actual result when you run each test.

## Screenshots
The `screenshots` folder contains illustrative terminal-style examples. Replace them with screenshots from your own run before submission if your instructor requires evidence captured from your device.

## Improvements included
- Repeated URL checks and a `quit` option.
- Clear warning messages and safety advice.
- Basic handling for malformed and empty input.
- Explicit limitation message so users do not mistake the result for a safety guarantee.

## Limitations
- A warning can appear on a legitimate URL, and a phishing URL can trigger no warnings.
- HTTPS does not prove that a website is trustworthy.
- The program does not check domain reputation, certificates, redirects, page content, or live threat feeds.
- This tool does not replace browser security warnings or expert review.

## Ethical use
Use the project for learning and awareness. Do not use it to harass people, collect credentials, or test systems without permission.

## Author
Name: [Your Name]  
Course/Class: [Your Course/Class]
