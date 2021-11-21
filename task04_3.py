from requests import get
import subprocess

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

download('https://epam.com', 'task04_testHTML')
