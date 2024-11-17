import os 
from urllib.parse import quote
from openpyxl import Workbook

BASE_URL = "https://edwardsoen.github.io/Tokai-website-assets/"
PRODUCT_IMAGES_PATH = ".\product_images"


class ImageData: 
    def __init__(self, url_path,item_name):
        self.url_path = url_path
        self.item_name = item_name


def get_images_local_path():
    data = [] 
    for i in os.listdir(PRODUCT_IMAGES_PATH): 
        item_name = i 
        for images in os.listdir(os.path.join(PRODUCT_IMAGES_PATH, item_name)): 
            image_path = os.path.join(PRODUCT_IMAGES_PATH, item_name, images)
            image_url = get_image_url(image_path)
            image_data = ImageData(url_path=image_url, item_name=item_name)
            data.append(image_data)
    return data

def get_image_url(local_url):
    url = local_url.replace("\\", "/")
    url = quote(url[2:])
    url = BASE_URL+url
    return url 
    # if is_valid_image_url(url=url): 
        # return url 
    return None


import requests

def is_valid_image_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(url + " valid")
            return True
        return False
    except requests.exceptions.RequestException:
        # Catch network-related errors
        print("INVALID " + url)
        return False
    


def save_2d_list_to_excel(data, file_name="output.xlsx", sheet_name="Sheet1"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    for row in data:
        sheet.append(row)

    workbook.save(file_name)
    print(f"Excel file '{file_name}' created successfully!")



if __name__ == "__main__": 
    image_data_list = get_images_local_path()
    output = []
    for data in image_data_list: 
        output.append([data.url_path, data.item_name])
    save_2d_list_to_excel(output)

    
    






