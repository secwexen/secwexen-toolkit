"""
OSINT Demo Script
This example demonstrates how to use the OSINT tools inside the project.
"""

from tools.osint.python.subdomain_finder import find_subdomains
from tools.osint.python.email_harvester import harvest_emails
from tools.osint.python.username_lookup import lookup_username


def main():
    target_domain = "example.com"
    username = "example"

    print("[+] Running OSINT demo...\n")

    print(f"[1] Subdomain scan for: {target_domain}")
    subdomains = find_subdomains(target_domain)
    print("Found subdomains:", subdomains, "\n")

    print(f"[2] Email harvesting for: {target_domain}")
    emails = harvest_emails(target_domain)
    print("Found emails:", emails, "\n")

    print(f"[3] Username lookup for: {username}")
    profiles = lookup_username(username)
    print("Found profiles:", profiles, "\n")

    print("[+] OSINT demo completed.")


if __name__ == "__main__":
    main()
