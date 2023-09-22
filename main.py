import csv
import sys

from bs4 import BeautifulSoup

from http_requests import HttpRequests


def exec():
    """
        URL取得 exportCSV
    Author:
        tensho arai
    Args:
        .\exe.sh arg1(URL) arg2(取得要素キー) arg3(csvExportPath)
    """

    http_requests = HttpRequests()
    url = sys.argv[1]
    element_key = sys.argv[2]
    output_path = sys.argv[3]


    response = http_requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select(element_key)

    data = list()
    for link in links:
        target_url = link['href']
        if not target_url.startswith(url):
            target_url = url + target_url

        data.append([target_url])

    with open(output_path, "w", newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

    print("export csv")


exec()

# url = "https://dev.classmethod.jp"
# element_key = "div.post-container a.link"
# output_path = "./output.csv"
# exec(url, element_key, output_path)


