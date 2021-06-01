from POM.Locator.Locators import locator
from selenium.webdriver.common.keys import Keys
from POM.Module.InsuranceInformation import Insuranceinformationform
from POM.CredentialsFile.ConsonantCSV import var
from POM.CredentialsFile.UserInputs import userValue
import time
from faker import Faker
fake = Faker()
name = fake.name()
last = fake.last_name()
address = fake.address()
city = fake.city_suffix()
phone = fake.phone_number()


# Data directly upload from the CSV sheet.
class Personalinformationform():
    def __init__(self,driver):
        self.driver = driver
        self.firstname = locator.firstname_id
        self.lastname = locator.lastname_id
        self.address1 = locator.address1_id
        self.address2 = locator.address2_id
        self.city = locator.city_id
        self.state = locator.state_id
        self.searchState = locator.searchState_css
        self.zip = locator.zip_id
        self.motherBirthday = locator.motherBirthday_id
        self.email = locator.email_id
        self.phone = locator.phone_id
        self.nextBtn2 = locator.nextBtn2_css
        self.InsuranceInfo = Insuranceinformationform(driver)
        self.varCSVData = var(driver)
        self.emailPut = userValue.email


    def personalinformationpage(self):
        self.driver.find_element_by_id(self.firstname).send_keys(name)
        self.driver.find_element_by_id(self.lastname).send_keys(last)
        self.driver.find_element_by_id(self.address1).send_keys(address)
        self.driver.find_element_by_id(self.address2).send_keys(address)
        self.driver.find_element_by_id(self.city).send_keys(city)
        self.driver.find_element_by_id(self.state).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.searchState).send_keys(self.varCSVData.insuranceData)
        print("insuranceData-- ", self.varCSVData.insuranceData, end=", ")
        self.driver.find_element_by_css_selector(self.searchState).send_keys(Keys.ENTER)
        self.driver.find_element_by_id(self.zip).send_keys("80067")
        self.driver.find_element_by_id(self.motherBirthday).send_keys("12/12/1994")
        self.driver.find_element_by_id(self.email).send_keys(self.emailPut)
        self.driver.find_element_by_id(self.phone).send_keys(phone)
        button = self.driver.find_element_by_css_selector(self.nextBtn2)
        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        # It will call the "Insurance Information" Page.
        self.InsuranceInfo.insuranceinformationpage()