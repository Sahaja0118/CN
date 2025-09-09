# dns_client.py

import socket
import dns.resolver

DOMAIN = "google.com"
LOG_FILE = "dns_results.txt"

def resolve_ip(domain, log_file):
    """Resolve domain IP using socket."""
    try:
        ip = socket.gethostbyname(domain)
        log_file.write(f"IP Address of {domain}: {ip}\n\n")
    except socket.gaierror:
        log_file.write(f"Could not resolve IP for {domain}\n\n")

def resolve_record(domain, record_type, log_file):
    """Resolve specific DNS record (A, MX, CNAME) and log results."""
    try:
        records = dns.resolver.resolve(domain, record_type)
        log_file.write(f"{record_type} records for {domain}:\n")
        for r in records:
            log_file.write(str(r) + "\n")
        log_file.write("\n")
    except dns.resolver.NoAnswer:
        log_file.write(f"No {record_type} record found.\n\n")
    except dns.resolver.NXDOMAIN:
        log_file.write(f"Domain {domain} does not exist.\n\n")
    except Exception as e:
        log_file.write(f"Error resolving {record_type} record: {e}\n\n")

def main():
    try:
        with open(LOG_FILE, "w") as log_file:
            # Resolve IP
            resolve_ip(DOMAIN, log_file)

            # Resolve DNS records
            for record_type in ["A", "MX", "CNAME"]:
                resolve_record(DOMAIN, record_type, log_file)

        print(f"DNS query completed and results logged into {LOG_FILE}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
