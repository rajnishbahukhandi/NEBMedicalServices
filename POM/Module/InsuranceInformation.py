from POM.Locator.Locators import locator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.CredentialsFile.ConsonantCSV import var
import time
import random

coveragetype = ["Friend or Family", "My Doctor's Office", "Google Search/Ad", "Instagram", "Facebook",
                "Ameda", "Ardo", "Medela", "Spectra", "My Insurance Company", "Bump Box", "Other"]
randomcoverage = random.choice(coveragetype)


# Data directly upload from the CSV sheet.
class Insuranceinformationform():
    def __init__(self, driver):
        self.driver = driver
        self.insuranceType = locator.insuranceType_id
        self.insuranceTypeSearch = locator.insuranceTypeSearch_css
        self.insuranceId = locator.insuranceId_id
        self.coverageTypeOutcome = locator.coverageTypeOutcome_xpath
        self.coverageTypeOutcomeSearch = locator.coverageTypeOutcomeSearch_xpath
        self.terms = locator.terms_xpath
        self.submitBtn = locator.submitBtn_xpath
        self.varCSVData = var(driver)

    def insuranceinformationpage(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.coverageTypeOutcome)))
        element.click()
        self.driver.find_element_by_xpath(self.coverageTypeOutcomeSearch).send_keys(randomcoverage)
        print("coverageType-- ", randomcoverage)
        self.driver.find_element_by_xpath(self.coverageTypeOutcomeSearch).send_keys(Keys.ENTER)
        self.driver.find_element_by_id(self.insuranceType).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.insuranceTypeSearch).send_keys(self.varCSVData.insuranceTypeData)
        print("insuranceTypeData--", self.varCSVData.insuranceTypeData, end=", ")
        self.driver.find_element_by_css_selector(self.insuranceTypeSearch).send_keys(Keys.ENTER)
        self.driver.find_element_by_id(self.insuranceId).send_keys(self.varCSVData.insuranceIDData)
        print("insuranceIDData-- ", self.varCSVData.insuranceIDData, end=", \n\n")
        self.driver.find_element_by_xpath(self.terms).click()

        submit = self.driver.find_element_by_xpath(self.submitBtn)
        self.driver.execute_script("arguments[0].click();", submit)