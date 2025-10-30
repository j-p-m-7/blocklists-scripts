import re

# Function to convert domains to URLs
def convert_to_url(domain):
    # Extract domain from inside parentheses, if present
    match = re.search(r'\((.*?)\)', domain)  # Regex to find text inside parentheses
    if match:
        domain = match.group(1)  # Get the first matching group (i.e., domain inside parentheses)

    # Remove any spaces from the domain name
    domain = domain.replace(" ", "")

    # Remove 'www.' if it exists at the beginning of the domain
    domain = domain.lstrip("www.")

    # If the domain doesn't start with 'http' or 'https', add 'http://'
    if not domain.startswith('http'):
        domain = 'www.' + domain

    # Ensure the domain is in a valid format (only letters, numbers, dots, and hyphens)
    if re.match(r'^[a-zA-Z0-9.-]+$', domain.split('://')[-1]):
        return domain
    else:
        return None  # Return None for invalid domains

# Read the list of domains from the input file
with open('domains.txt', 'r', encoding='utf-8') as file:
    domains = file.readlines()

# Clean up the domain names (remove extra spaces or newlines)
domains = [domain.strip() for domain in domains]

# Convert each domain in the list to a proper URL
urls = [convert_to_url(domain) for domain in domains]

# Filter out None values (invalid entries)
urls = [url for url in urls if url]

# Write the URLs to a new file (one URL per line)
with open('urls_blocklist.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        file.write(url + '\n')

print(f"{len(urls)} URLs have been extracted and saved to urls_blocklist.txt")
