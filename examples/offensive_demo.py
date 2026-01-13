"""
Offensive Demo Script
Demonstrates how to use offensive tools in the Secwexen framework.
"""

from utils import log_info
from tools.offensive.python.port_scanner.scanner import scan_ports
from tools.offensive.python.web_fuzzer import fuzz_url
from tools.offensive.python.ssh_bruteforce import ssh_bruteforce


def main():
    target_ip = "192.168.1.10"
    target_url = "http://example.com"
    ssh_target = ("192.168.1.15", "root")

    log_info("[OFFENSIVE] Starting offensive demo...")

    log_info(f"1) Scanning ports on {target_ip}")
    scan_ports(target_ip)

    log_info(f"2) Fuzzing URL: {target_url}")
    fuzz_url(target_url)

    log_info(f"3) Running SSH bruteforce on {ssh_target[0]}")
    ssh_bruteforce(ssh_target[0], ssh_target[1])

    log_info("[OFFENSIVE] Demo completed.")


if __name__ == "__main__":
    main()
