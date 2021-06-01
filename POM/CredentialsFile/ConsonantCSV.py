from POM.CredentialsFile.CSVFileData import csvDataextract
from POM.CredentialsFile.forloop import forvalue

# saved the CSV data in the list, and provided these data to the required files.
class var():
    def __init__(self, driver):
        self.driver = driver
        self.csvInsurance = csvDataextract.Insurance
        self.csvInsuranceID = csvDataextract.InsuranceID
        self.csvInsuranceType = csvDataextract.InsuranceType
        self.valuePut = forvalue.csvrowvalue

        self.insuranceData = self.csvInsurance[self.valuePut]
        self.insuranceIDData = self.csvInsuranceID[self.valuePut]
        self.insuranceTypeData = self.csvInsuranceType[self.valuePut]