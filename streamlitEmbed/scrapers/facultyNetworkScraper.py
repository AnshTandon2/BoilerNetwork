import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the webpage you want to scrape
url = 'https://apps.powerapps.com/play/e/default-4130bd39-7c53-419c-b1e5-8758d6d63f21/a/9cb3a75e-402c-4aa1-9662-30d6024232c6?tenantId=4130bd39-7c53-419c-b1e5-8758d6d63f21%22&action=view_details&projectID=16'  # Replace with the URL of your target webpage

# Send an HTTP GET request to the URL and get the HTML content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all text elements in the parsed HTML
    all_text = soup.get_text()
    
    # Define the path to the CSV file where you want to save the text
    csv_file_path = 'page_text.csv'  # Replace with your desired file path
    
    # Write the text to the CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Text'])  # Write header row
        csv_writer.writerow([all_text])  # Write the page text to the CSV
    
    print(f"Text has been saved to {csv_file_path}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


# from selenium import webdriver
# import csv

# # Define the URL of the web page you want to scrape
# url = 'https://apps.powerapps.com/play/e/default-4130bd39-7c53-419c-b1e5-8758d6d63f21/a/9cb3a75e-402c-4aa1-9662-30d6024232c6?tenantId=4130bd39-7c53-419c-b1e5-8758d6d63f21%22&action=view_details&projectID=23'  # Replace with your target URL

# # Executable driver path
# webdriver_path = r'C:\Users\arnav\Downloads\chromedriver-win64\chromedriver.exe'

# # Set ChromeDriver executable path
# webdriver_service = webdriver.chrome.service.Service(executable_path=webdriver_path)

# # Initialize WebDriver
# driver = webdriver.Chrome(service=webdriver_service)

# # Navigate to the web page
# driver.get(url)

# # Get all the text from the web page
# page_text = driver.find_element_by_tag_name('body').text

# # Close the WebDriver
# driver.quit()

# # Define the path to the CSV file where you want to save the text
# csv_file_path = 'page_text.csv'  # Replace with your desired file path

# # Write the text to the CSV file
# with open(csv_file_path, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Text'])  # Write header row
#     csv_writer.writerow([page_text])  # Write the page text to the CSV

# print(f"Text has been saved to {csv_file_path}")




# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import csv

# # # Executable driver path
# # path = r'C:\Users\arnav\Downloads\chromedriver-win64\chromedriver.exe'

# # # Set ChromeDriver executable path
# # webdriver_service = webdriver.chrome.service.Service(executable_path=path)

# # # Initialize WebDriver
# # driver = webdriver.Chrome(service=webdriver_service)

# # # Navigate to the PowerApp URL
# # powerapp_url = ''
# # driver.get(powerapp_url)

# # # List to store project titles
# # project_titles = []

# # # Find and store project titles from the "Project Title" column
# # title_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[11]/div/div/div/div/div/div/div/div/div[1]/table/thead/tr/th[2]/div/div[1]')  # Adjust the XPath and class name as per your HTML structure
# # for title_element in title_elements:
# #     project_titles.append(title_element.text)

# # # Iterate through project titles and click the corresponding buttons
# # for title in project_titles:
# #     # Locate the button associated with the project title (adjust the XPath or CSS selector)
# #     button = driver.find_elements(By.XPATH, '//*[@id="id_17_input"]')  # Adjust the XPath or selector based on your HTML structure
    
# #     # Click the button
# #     button.click()

# #     # Perform any scraping or data extraction here

# #     # Navigate back to the main page (assuming the button click opened a new page)
# #     driver.back()

# # print(project_titles)

# # # Close the WebDriver
# # driver.quit()