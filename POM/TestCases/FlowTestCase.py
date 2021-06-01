from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from POM.Module.GetStarted import Getstartform
from POM.CredentialsFile.GmailCheck import Gmail
import unittest
import time

URL_Gmail = "https://mail.google.com/mail/u/0/?tab=rm&ogbl"
URL_NEBMedical = "https://nebmedical.nvtlabs.com/qualify-breast-pump-through-insurance/"


class NEBMedical(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()

    def testForm(self):
        driver = self.driver
        driver.get(URL_NEBMedical)
        time.sleep(1)
        getstart = Getstartform(driver)
        # Flow of NEB Medical page InsuranceInfromation -> PersonalInformation -> GetStarted
        # All are interlinked
        getstart.getstartpage()
        driver.implicitly_wait(18)
        driver.execute_script("window.open()")
        # use the window handle. It will open the gmail on new tab.
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(7)
        driver.get(URL_Gmail)
        gmailIn = Gmail(driver)
        gmailIn.gmailInbox()

    @classmethod
    def tearDownClass(cls):
        time.sleep(7)
        cls.driver.close()
        print("TearDownClass")