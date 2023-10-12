import requests
from bs4 import BeautifulSoup
import time

# Main page URL
main_page_url = "https://www.dalfen.com/featured-properties/"

# Function to scrape details from the tile link
def scrape_tile_details(tile_link):
    response = requests.get(tile_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the address element
        address_element = soup.find("div", class_="property-address")
        if address_element:
            address_lines = address_element.find_all("p")
            address = "\n".join(line.get_text(strip=True) for line in address_lines)

            # Print or process the extracted address
            print("Address:")
            print(address)
        else:
            print("Address not found on the page.")

    else:
        print(f"Failed to fetch details page. Status code: {response.status_code}")

# Function to scrape the main page and process each tile link
def scrape_main_page(main_page_url):
    response = requests.get(main_page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        tile_links = soup.select(".propertysep-pic a[href]")
        for link in tile_links:
            tile_link = link["href"]
            # Scraping details from the tile link
            scrape_tile_details(tile_link)
            # Fetching the main page HTML again to simulate going back to the main page
            response = requests.get(main_page_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
            else:
                print(f"Failed to fetch the main page. Status code: {response.status_code}")
    else:
        print(f"Failed to fetch the main page. Status code: {response.status_code}")

# Start the scraping process
scrape_main_page(main_page_url)