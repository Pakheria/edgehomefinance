# Libraries importing
import requests
from bs4 import BeautifulSoup

# Getting urls form the sitemap
# def team_member(team_data):
url = 'https://edgehomefinance.com/our-team/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
team_members = soup.find_all('div', {'class': 'content p-3'})

import csv

# Define the headers for the CSV file
headers = ['First Name', 'Last Name', 'Title', 'NMLS #', 'Email', 'Phone']

counter = 0

# Open a CSV file in write mode
with open('team_members.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the headers to the CSV file
    
    # Iterate over each team member
    for member in team_members:
        if counter >= 10:
            break  # Exit the loop if 10 iterations have been completed
    # Extract information about the team member
        try:
            first_name = member.find('span', {'class' : 'first default-order'}).text.strip()
            last_name = str(member.find('span', {'class' : 'last default-order'}).text.strip())
            all_title = member.find_all('span')
            title = all_title[2].text.strip()
            nmls_number = member.find('span', {"class" : "profile-caption"}).text
            email = member.find('a', {'class':"email tippy"})['href'].split(':', 1)[-1]
            phone = member.find('a', {'class' : "phonee tippy"})['href'].split(':')[-1]
            # Write the extracted information to the CSV file
            writer.writerow([first_name, last_name, title, nmls_number, email, phone])
            
            counter += 1
        
        except IndexError:
            title = ''