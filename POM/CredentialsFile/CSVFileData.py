import csv


class csvDataextract():
        # open the file in read mode
        # Give the local path of the csv file. User can provide the csv local path.
        filename = open('/Users/ray.rajnish/Downloads/AutoApplyListforITH-HighEndCoverage.csv', 'r')

        # creating dictreader object
        file = csv.DictReader(filename)

        # lists for values save.
        Insurance = []
        InsuranceType = []
        InsuranceID = []
        CoverageTypeOutcome = []

        # iterating over each row and append
        # values to empty list
        for col in file:
            Insurance.append(col['test'])
            InsuranceType.append(col['Insurance Type'])
            InsuranceID.append(col['Insurance ID'])
            CoverageTypeOutcome.append(col['Coverage Type / Outcome'])
