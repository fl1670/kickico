import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from FW.BaseFW import BaseFW


class waitingFW(BaseFW):

    def __init__(self, manager):
        super().__init__(manager)

    # ищем элемент "time_element_Wait" секунд ("time_element_Wait" = 15)
    def waiting_for_the_element(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.time_element_Wait).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            pass

    def waiting_element_to_be_clickable(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.time_element_Wait).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException as e:
            pass

    def waiting_for_item_to_hide(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.time_element_Wait).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            pass

    def waiting_for_item_not_display(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.time_element_Wait).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            pass

    def waiting_element_is_enabled(self, locator):
        index = 0
        while True:
            try:
                self.GetDriver().find_element_by_xpath(locator).is_enabled()
                if self.time_element_Wait < index:
                    break
                else:
                    time.sleep(0.5)
                    index = index + 0.5
            except NoSuchElementException:
                break

    # ищем элемент "time_element_Wait" секунд ("time_element_Wait" = 15)
    def waiting_for_the_element_to_be_clickable(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.time_element_Wait).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException as e:
            pass

    def waiting_for_loading_elements(self):
        index = 0
        while True:
            try:
                if self.time_element_Wait < index:
                    break
                self.GetDriver().find_element_by_id('section_loading')
                time.sleep(0.5)
                index = index + 0.5
            except NoSuchElementException:
                break

    # Ждет пока из атребута пропадет текст или пройдет время ожидания (30 сек)
    def waiting_loading_tag(self, locator, attribute, loading):
        index = 0
        while True:
            try:
                if self.time_element_Wait < index:
                    break
                text = self.GetDriver().find_element_by_xpath(locator).get_attribute(attribute)
                pass
                if loading in text:
                    time.sleep(0.5)
                    index = index + 0.5
                else:
                    break
            except NoSuchElementException:
                break

    def waiting_for_loading_elements_RequestList(self, id):
        index = 0
        while True:
            try:
                if self.time_element_Wait < index:
                    break
                textClass = self.GetDriver().find_element_by_id(id).get_attribute('class')
                if textClass.find('loading') == -1:
                    break
                time.sleep(0.5)
                index = index + 0.5
            except NoSuchElementException:
                break
        time.sleep(2)

    def waiting_for_text_to_appear(self, locator, text):
        index = 0
        while True:
            try:
                if self.time_element_Wait < index:
                    break
                if text in self.GetDriver().find_element_by_xpath(locator).text:
                    break
            except NoSuchElementException:
                time.sleep(0.5)
                index = index + 0.5
