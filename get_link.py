import requests
from bs4 import BeautifulSoup
import argparse
import sys

def scrape_links_with_suffix(url, suffix):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all 'a' tags (hyperlinks) in the page
        links = soup.find_all('a')
        
        # Extract the href attribute from each 'a' tag and filter based on suffix
        required_links = []
        for link in links:
            href = link.get('href')
            if href and href.endswith(suffix):
                required_links.append(href) 
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
    return required_links

def main():
    parser = argparse.ArgumentParser(description="Process Url and suffix")
    parser.add_argument("-l", "--link", type=str, help="The required link of the page")
    parser.add_argument("-s", "--suffix", type=str, help="the suffix of the links required to be scrapped which equals .rar by default")
    args = parser.parse_args()

    if args.link == None:
        print("you forgot to specify a URL", file=sys.stderr)
        return 1
    
    
    url_to_scrape = args.link  
    suffix_to_find = ".rar"  # Change this to the suffix you want to filter for
    if args.suffix != None:
        suffix_to_find = args.suffix
    links = scrape_links_with_suffix(url_to_scrape, suffix_to_find)


    with open("links.txt", "w") as file:
        for link in links:
            file.write(link + "\n")
main()