from selenium import webdriver
from selenium.webdriver.common.by import By

class YFExchangeGateway:
    def __init__(self, year, month, date):
        self.url = f'https://info.finance.yahoo.co.jp/history/?code=USDJPY%3DX&sy={year}&sm={month}&sd={date}&ey={year}&em={month}&ed={date}&tm=d'

    def get_data(self):
        browser = webdriver.Chrome()
        browser.get(self.url)

        elem_boardFin = browser.find_elements(by=By.CLASS_NAME, value='boardFin')

        elems_th = elem_boardFin[0].find_elements(by=By.TAG_NAME, value='th')
        titles = []
        for _ in elems_th:
            titles.append(_.text)

        elems_td = elem_boardFin[0].find_elements(by=By.TAG_NAME, value='td')
        values = []
        for _ in elems_td:
            values.append(_.text)

        browser.quit()

        return titles, values
