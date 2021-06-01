class locator():

    # Get Start Locators
    selectProduct_css = ".f_field > div:nth-child(1) span"
    childDueDate_id = "due-date"
    nextBtn1_xpath = "//button[@type='button']"

    # Personal Information Locators
    firstname_id = "first-name"
    lastname_id = "last-name"
    address1_id = "address-1"
    address2_id = "address-1"
    city_id = "city"
    state_id = "select2-state-container"
    searchState_css = ".select2-search__field"
    zip_id = "zip"
    motherBirthday_id = "mother-bday"
    email_id = "email"
    phone_id = "phone"
    nextBtn2_css = ".f_btn-wrapper:nth-child(2) > .btn-teal > span"

    # Insurance information
    insuranceType_id = "select2-insurance-type-container"
    insuranceTypeSearch_css = ".select2-search__field"
    insuranceId_id = "insurance-id"
    coverageTypeOutcome_xpath = "//div[@id='qti-step-2']/fieldset[4]/section/span/div/span/span/span/span[2]/b"
    coverageTypeOutcomeSearch_xpath = "//input[@type='search']"
    terms_xpath = "//label[contains(.,'I agree to the Terms')]"
    submitBtn_xpath = "//div[@id='qti-step-2']/div/button[2]/span"

    # Gmail Account
    G_email_id = "identifierId"
    nextBtnOfEmail_id = "identifierNext"
    G_password_xpath = "//input[@name='password']"
    nextBtnOfPassword_id = "passwordNext"
    G_selectBtn_xpath = "//div[@id=':1y']/div/div"
    # Locator of the select button.
    G_selectUnread_xpath = "//div[@id=':k9']/div"
    # Locator of the Unread button.
    allEmails_xpath = '//span[@class="bqe"]'
    # Locator of all emails in the Gmail. And get the subject line of email of unread.
    clickOnInboxBtn_xpath = '//*[@class="TO nZ aiq"]'
    clickOnPromotionBtn_xpath = '//*[@class="aAy aJi-aLe"]'

