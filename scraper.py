import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a website
def scrape_jobs():
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    # Send a GET request to the website
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find job postings
    jobs = []
    for job in soup.find_all("li", class_="feature"):
        title = job.find("span", class_="title").get_text(strip=True)
        company = job.find("span", class_="company").get_text(strip=True)
        link = "https://weworkremotely.com" + job.find("a")["href"]
        
        jobs.append({"Title": title, "Company": company, "Link": link})
    
    # Save to a CSV file
    df = pd.DataFrame(jobs)
    df.to_csv("remote_jobs.csv", index=False)
    print("Jobs scraped and saved to remote_jobs.csv")

# Run the scraper
if __name__ == "__main__":
    scrape_jobs()

# import requests 
# import pandas as pd 
# from bs4 import BeautifulSoup

# def scrape_jobs(): 
#     url = "https://weworkremotely.com/categories/remote-programming-jobs"
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

#     response = requests.get(url, headers=headers) 

#     soup = BeautifulSoup(response.text, 'html.parser') 

#     jobs = [] 
#     for job in soup.find_all("li", class_="feature"):
#         title = job.find("span", class_="title").get_text(strip=True)
#         company = job.find("span", class_="company").get_text(strip=True) 
#         link = "https://weworkremotely.com" + job.find("a")("href")

#         jobs.append({"Title": title, "Company": company, "Link": link})
    
#     df = pd.DataFrame(jobs) 
#     df.to_csv("remote_jobs.csv", index=False)


# if __name__ == "__main__":
#     scrape_jobs()