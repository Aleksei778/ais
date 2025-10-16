import requests
from typing import Dict
from collections import Counter
import time


def ping_localhost_80(N: int) -> Dict[str, int]:
    url = 'http://localhost:80/language'

    servers = []
    failed = 0
    delay = 0.1

    print("Начинаю обработку запросов...")

    for i in range(1, N + 1):
        try:
            response = requests.get(url, timeout=5)

            data = response.json()

            print(data)

            servers.append(data['language'])

            if i % 10 == 0:
                print(f"Обработано: {i}/{N} запросов")

        except requests.exceptions.RequestException as re:
            failed += 1
            print(f"Ошибка запроса #{i}: {re}")

    return dict(Counter(servers))

def main():
    N = 90

    servers = ping_localhost_80(N)

    print(f"Количество запросов к разным серверам: {servers}")

if __name__ == "__main__":
    main()