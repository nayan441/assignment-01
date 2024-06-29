import requests
from bs4 import BeautifulSoup
import os

def download_image_2(url, folder_path, image_name):
    # print(url)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        img_data = requests.get(url).content
        with open(os.path.join(folder_path, image_name), 'wb') as handler:
            handler.write(img_data)
        print(f"Image downloaded: {image_name}")
    else:
        print(f"Failed to download image: {image_name}")


def main():
    url = "https://www.amazon.in/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            img_tags = soup.find_all("img")

            if not os.path.exists("downloaded_images_2"):
                os.makedirs("downloaded_images_2")

            count = 0
            for img in img_tags:
                if count >= 5:
                    break
                img_url = img.get("src") #dict img
                if img_url:
                    img_name = f"image_{count + 1}.jpg"
                    download_image_2(img_url, "downloaded_images_2", img_name)
                    count += 1
        else:
            print(f"Request failed")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve content from {url}. Error: {e}")
if __name__ == "__main__":
    main()
