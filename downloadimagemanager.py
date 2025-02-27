import requests
import os

def download_image(url, folder):
    print(f"Начало загрузки: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()

        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Загружено: {filename}")
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")

def main():
    base_url = "https://resheba.top/GDZ/10-rus-2020/1/"
    base_folder = "GDZ/RUSSIAN10/GLAVA"
    os.makedirs(base_folder, exist_ok=True)

    start_number = 1
    end_number = 491

    for number in range(start_number, end_number + 1):
        url = f"{base_url}{number}.png"
        download_image(url, base_folder)  # Используем правильное название функции

if __name__ == "__main__":
    main()

        ecle_number += 1  

if __name__ == "__main__":
    main()
