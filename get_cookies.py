import pickle

from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GetCookie:

    """Класс получения cookie файла для дальнейшего взаимодействия с веб-кошельком"""

    def __init__(self):
        """
        Инициализация:
         Браузера;
         Рандомного User-Agent;
         Опций браузера для работы в безоконном режиме

        """
        useragent = UserAgent()
        options = webdriver.FirefoxOptions()
        options.add_argument(f"User-Agent={useragent.random}")
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def get_cookie(self):

        """
        Метод авторизации в кошельке и извлечения cookie для дальнейшей работы
        :return: name file cookie
        """

        self.driver.get('#')
        print('Авторизируйтесь')

        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[5]/input'))).send_keys(
            input('gmail: '))

        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[7]/span/input'))).send_keys(
            input('password: '))

        self.driver.find_element(By.CSS_SELECTOR, '.sc-vuxumm-0 > button:nth-child(1) > span:nth-child(1)').click()
        try:
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/div[2]/input'))).send_keys(
                input('code: '))

            self.driver.find_element(By.CSS_SELECTOR, '.ant-btn > span:nth-child(1)').click()
        except:
            print('Код не понадобился')

        name_account = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]'))).text

        pickle.dump(self.driver.get_cookies(), open(f"{name_account.replace('.', '_')}", 'wb'))

        print(f'Cookie: {name_account} - Save')

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    Get = GetCookie()
    Get.get_cookie()




