from selenium import webdriver

def testar_webdriver():
    try:
        driver = webdriver.Chrome()  # Substitua pelo driver correto, se necessário
        driver.get("https://www.google.com")
        print("WebDriver funcionando corretamente!")
        driver.quit()
    except Exception as e:
        print(f"Erro ao iniciar o WebDriver: {e}")

if __name__ == "__main__":
    testar_webdriver()