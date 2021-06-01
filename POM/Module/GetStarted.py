from POM.Locator.Locators import locator
from POM.Module.PersonalInformation import Personalinformationform


class Getstartform():
    def __init__(self,driver):
        self.driver = driver
        self.selectProduct = locator.selectProduct_css
        self.childDueDate = locator.childDueDate_id
        self.nextBtn1 = locator.nextBtn1_xpath
        self.personalInfo = Personalinformationform(driver)

    def getstartpage(self):
        self.driver.find_element_by_css_selector(self.selectProduct).click()
        self.driver.find_element_by_id(self.childDueDate).send_keys("01/06/2021")
        self.driver.find_element_by_xpath(self.nextBtn1).click()
        # It will call the "Personal information" page.
        self.personalInfo.personalinformationpage()