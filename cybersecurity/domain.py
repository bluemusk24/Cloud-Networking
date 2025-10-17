#!/usr/bin/env python3
import sys
import whois

def get_registrar(w):
    for key in ["registrar", "sponsoring registrar", "registrar name"]:
        for attr in w.keys():
            if attr.lower() == key.lower() and w[attr]:
                return w[attr]
    return None

def main():
    domains = sys.argv[1:]
    if not domains:
        print("Usage: python3 domain.py domain1.com domain2.com ...")
        sys.exit(1)

    for domain in domains:
        try:
            w = whois.whois(domain)
            registrar = get_registrar(w)
        except Exception as e:
            registrar = f"Error: {e}"
        print(f"{domain} -> Registrar: {registrar or 'Not found'}")

if __name__ == "__main__":
    main()
