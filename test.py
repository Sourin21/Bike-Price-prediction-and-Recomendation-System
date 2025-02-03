from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if you don't want the browser UI

# Path to ChromeDriver
service = Service(r"C:\Users\artes\Desktop\4t\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the BikeDekho database
url = "https://www.bikedekho.com/find-new-bikes"

# Open the website
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Scroll down to load more bikes (if the site uses lazy loading)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # Allow time for loading

# Find all bike elements on the page
bikes = driver.find_elements(By.XPATH, "//a[@class='bikeTitle']")

# Create a CSV file to store the bike data
with open('bike_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Bike Name', 'Price', 'Specifications Link'])

    # Loop through all bike entries
    for bike in bikes:
        try:
            # Extract bike details
            bike_name = bike.text
            bike_url = bike.get_attribute('href')
            
            # Open each bike's detail page
            driver.get(bike_url)
            time.sleep(2)
            
            # Try to find the price of the bike
            try:
                price = driver.find_element(By.XPATH, "//*[contains(text(), 'Rs')]").text
            except:
                price = 'Not Available'
            
            # Write bike data to the CSV
            writer.writerow([bike_name, price, bike_url])
            
            # Go back to the bike listing page
            driver.get(url)
            time.sleep(2)

        except Exception as e:
            print(f"Error fetching bike info: {e}")

# Close the WebDriver
driver.quit()

print("Data has been exported to bike_data.csv")
