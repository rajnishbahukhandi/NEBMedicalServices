from POM.Locator.Locators import locator
from POM.CredentialsFile.UserInputs import userValue
import time

# Some important email subject lines, which need to check for NEB Medical.
inboxMessage = "New Qualify Through Insurance Application"
promotionMessagesForThanks = "Thanks for choosing Neb Medical!"
promotionMessagesForApproved = "You're approved!"


class Gmail():
    def __init__(self,driver):
        self.driver = driver
        self.G_email = locator.G_email_id
        self.nextBtnOfEmail = locator.nextBtnOfEmail_id
        self.G_password = locator.G_password_xpath
        self.nextBtnOfPassword = locator.nextBtnOfPassword_id
        self.G_selectBtn = locator.G_selectBtn_xpath
        self.G_selectUnread = locator.G_selectUnread_xpath
        self.allEmails = locator.allEmails_xpath
        self.clickOnInboxBtn = locator.clickOnInboxBtn_xpath
        self.clickOnPromotionBtn = locator.clickOnPromotionBtn_xpath
        self.enterEmail = userValue.enterTheGmailId
        self.enterPassword = userValue.enterTheGmailPassword

    def gmailInbox(self):
        self.driver.find_element_by_id(self.G_email).send_keys(self.enterEmail)
        self.driver.find_element_by_id(self.nextBtnOfEmail).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.G_password).send_keys(self.enterPassword)
        self.driver.find_element_by_id(self.nextBtnOfPassword).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.G_selectBtn).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.G_selectUnread).click()
        time.sleep(3)
        testUnread = self.driver.find_element_by_xpath(self.allEmails).text
        # It will print the selected first unread email of inbox.
        # And will compare with some important NEB Medical subject lines.
        print(testUnread)
        if inboxMessage in testUnread:
            print("Pass inboxMessage \n")
            # Match the subject text of email.
            # Click on the matched subject email. Now enter into the email.
            self.driver.find_element_by_xpath(self.allEmails).click()

            # # Commented code is working. It redirects to the "promotions" emails.
            #
            # time.sleep(3)
            # # Now click on the "Inbox" button. And exit from the open email.
            # self.driver.find_element_by_xpath(self.clickOnInboxBtn).click()
            # time.sleep(3)
            # # Now click on the "Promotion" button. And check the emails of NEB Medical come in "promotion".
            # self.driver.find_element_by_xpath(self.clickOnPromotionBtn).click()
            # time.sleep(3)
            # self.driver.find_element_by_xpath(self.G_selectBtn).click()
            # self.driver.find_element_by_xpath(self.G_selectUnread).click()
            # time.sleep(15)
            # testUnread2 = self.driver.find_element_by_xpath(self.allEmails).text
            # # It will print the selected first unread email.
            # # And will compare with some important NEB Medical subject lines.
            # print(testUnread2)
            # if promotionMessagesForThanks in testUnread2:
            #     print("Pass promotionMessagesForThanks \n")
            #     self.driver.find_element_by_xpath(self.allEmails).click()
            #     time.sleep(3)
            #     # Now click on "Inbox" button. And exit from the email.
            #     self.driver.find_element_by_xpath(self.clickOnInboxBtn).click()
            #     time.sleep(3)
            #     self.driver.find_element_by_xpath(self.clickOnPromotionBtn).click()
            #     time.sleep(14)
            #     self.driver.find_element_by_xpath(self.G_selectBtn).click()
            #     self.driver.find_element_by_xpath(self.G_selectUnread).click()
            #     time.sleep(3)
            #     testUnread3 = self.driver.find_element_by_xpath(self.allEmails).text
            #     # It will print the selected first unread email.
            #     # And will compare with some important NEB Medical subject lines.
            #     print(testUnread3)
            #     if promotionMessagesForApproved in testUnread3:
            #         print("Pass promotionMessagesForApproved \n")
            #         self.driver.find_element_by_xpath(self.allEmails).click()
            #     else:
            #         print("Not opening promotionMessagesForApproved \n")
            # else:
            #     print("Not opening promotionMessagesForThanks \n")
        else:
            print("Not opening inboxMessage \n")