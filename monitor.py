import os
import requests

def avisar_telegram(mensaje):
    requests.post(
        f"https://api.telegram.org/bot{os.environ['TELEGRAM_TOKEN']}/sendMessage",
        data={"chat_id": os.environ["TELEGRAM_CHAT_ID"], "text": mensaje},
        timeout=10,
    )

def main():
    options = Options()
    options.add_argument("-headless")  # obligatorio en un servidor
    driver = webdriver.Firefox(options=options)
    try:
        if revisar_pagina(driver):
            avisar_telegram(f"🚨 ¡HAY BOTÓN COMPRAR! {URL_EVENTO}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
