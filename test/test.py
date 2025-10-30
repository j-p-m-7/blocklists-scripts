import json

# Function to recursively extract URLs from the JSON
def extract_urls(data, urls=None):
    if urls is None:
        urls = []
    
    if isinstance(data, dict):  # If the data is a dictionary
        for key, value in data.items():
            if key == "url" and isinstance(value, str):  # Check if the key is 'url' and value is a string
                urls.append(value)
            else:
                extract_urls(value, urls)  # Recurse for nested dictionaries or lists
    
    elif isinstance(data, list):  # If the data is a list
        for item in data:
            extract_urls(item, urls)  # Recurse for each item in the list
    
    return urls

# Load the JSON data from a file
with open('fox.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract all URLs from the JSON data
urls = extract_urls(data)

# Save the URLs to a .txt file (one URL per line)
with open('fox.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        file.write(url + '\n')

print(f"{len(urls)} URLs have been extracted and saved to blocklist.txt")
