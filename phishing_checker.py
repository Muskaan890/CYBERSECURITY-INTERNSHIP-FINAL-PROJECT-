from urllib.parse import urlparse
import ipaddress
import re


def check_url(url: str) -> list[str]:
    """Return warning messages for simple URL-text checks.

    This is an awareness demo, not a security scanner. It does not visit URLs.
    """
    warnings = []

    url = url.strip()
    if not url:
        return ["Please enter a URL."]

    # urlparse expects a scheme to reliably separate the hostname.
    candidate = url if "://" in url else "https://" + url

    try:
        parsed = urlparse(candidate)
        hostname = parsed.hostname
    except ValueError:
        return ["The URL appears malformed; review it carefully."]

    if not hostname:
        return ["Could not identify a hostname. Check the URL format."]

    if "@" in url:
        warnings.append("Contains '@' — this can make a URL misleading.")

    if len(url) > 100:
        warnings.append("Long URL (over 100 characters) — review carefully.")

    # Detect IPv4 addresses in the hostname.
    try:
        ipaddress.ip_address(hostname)
        is_ip_address = True
    except ValueError:
        is_ip_address = False

    if is_ip_address:
        warnings.append("Hostname is an IP address rather than a typical domain name.")

    # Count hostname labels, e.g. login.account.example.com has 4.
    labels = hostname.rstrip(".").split(".")
    if len(labels) >= 5:
        warnings.append("Hostname has 5 or more segments.")

    if "xn--" in hostname.lower():
        warnings.append("Contains 'xn--' punycode marker; inspect the domain carefully.")

    if parsed.scheme.lower() == "http":
        warnings.append("Uses HTTP rather than HTTPS; the connection is not encrypted by HTTPS.")

    return warnings


def main() -> None:
    print("=" * 52)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 52)
    print("This tool checks URL text only. It never opens links.")
    print("Warnings are clues, not proof that a URL is malicious or safe.")
    print()

    while True:
        url = input("Enter a URL (or type 'quit' to exit): ").strip()
        if url.lower() in {"quit", "exit", "q"}:
            print("Goodbye. Stay alert online!")
            break

        warnings = check_url(url)
        print("\nResult:")
        if warnings:
            for warning in warnings:
                print(f"- {warning}")
            if warnings != ["Please enter a URL."]:
                print("Advice: Review the full domain and verify the sender independently.")
        else:
            print("- No warning signs from this simple checklist were detected.")
            print("- This does NOT mean the URL is safe.")
        print()


if __name__ == "__main__":
    main()
