import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

def find_mixed_content(url, crawled_urls=set(), reported_urls=set(), max_depth=1, current_depth=0):
    if current_depth > max_depth or url in crawled_urls:
        return

    crawled_urls.add(url)

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch the URL: {url}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # List of tags and their attribute that contain URLs
        tags_attributes = {
            'img': 'src',
            'link': 'href',
            'script': 'src',
            'iframe': 'src',
            'video': 'src',
            'audio': 'src',
            'source': 'src',
            'embed': 'src',
            'object': 'data'
        }

        mixed_content = []
        for tag, attr in tags_attributes.items():
            for element in soup.find_all(tag):
                src = element.get(attr)
                if src and urlparse(src).scheme == 'http':
                    mixed_content.append(os.path.basename(src))

        if mixed_content and url not in reported_urls:
            print(f"Mixed content found on {url}:")
            for item in mixed_content:
                print(item)
            reported_urls.add(url)
        else:
            if url not in reported_urls:
                print(f"No mixed content found on {url}.")
                reported_urls.add(url)

        # If deep link parameter is enabled, find and check all internal links
        if current_depth < max_depth:
            for link in soup.find_all('a', href=True):
                link_url = urljoin(url, link['href'])
                parsed_link_url = urlparse(link_url)
                # Avoid crawling external links and already crawled links
                if parsed_link_url.scheme in ['http', 'https'] and link_url not in crawled_urls:
                    find_mixed_content(link_url, crawled_urls, reported_urls, max_depth, current_depth + 1)

    except Exception as e:
        print(f"An error occurred: {e}")

def check_urls_from_file(file_path, max_depth=2):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
            for url in urls:
                find_mixed_content(url, max_depth=max_depth)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# Example usage
file_path = 'urls.txt'  # Path to your file containing URLs
max_depth = 2  # Change the depth as needed
check_urls_from_file(file_path, max_depth=max_depth)
