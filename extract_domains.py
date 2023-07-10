import tldextract
import sys
from urllib.parse import urlparse


def extract_domain(line):
    scheme = urlparse(line).scheme
    extracted = tldextract.extract(line)

    prefix = "blog." if extracted.subdomain == "blog" else ""
    return f'{scheme}://{prefix}{extracted.domain}.{extracted.suffix}'


def extract_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            domain = extract_domain(line.strip())
            print(domain)


def extract_from_stdin():
    for line in sys.stdin:
        domain = extract_domain(line.strip())
        print(domain)


def extract_domains():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        extract_from_file(file_path)
    else:
        extract_from_stdin()


if __name__ == '__main__':
    extract_domains()

