import requests
import os

def download_image(url, folder):
    print(f"start downloaded image....")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Complete:: {filename}")
    except Exception as e:
        print(f"Oooops, error {url}: {e}")

def main():
    ecle_number = 1 
    base_folder = 'download_image'  
    os.makedirs(base_folder, exist_ok=True)  

    start_number = 4
    end_number = 276
    number_of_cycles = 1

    for cycle in range(number_of_cycles):
        current_folder = os.path.join(base_folder, str(ecle_number))  
        os.makedirs(current_folder, exist_ok=True)

        for number in range(start_number, end_number + 1):
            url = f"link image url"
            print(f"Download for:: {url}")
            download_image(url, current_folder)  

        ecle_number += 1  

if __name__ == "__main__":
    main()