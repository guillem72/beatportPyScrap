import csv
class IO:


    def __init__(self,csvfile):
        self.csvfile=csvfile
        self.headers=None

    def read(self):
        with open(self.csvfile,"r") as csvfile:
            rows = csv.DictReader(csvfile)
        return rows

    def getFieldnames(self):
        with open(self.csvfile, "r") as csvfile:
            rows = csv.DictReader(csvfile)
            headers = rows.fieldnames
        return headers

    def write(self,rows, fieldnames):
        with open(self.csvfile, "rw") as csvfile:
            w=csv.DictWriter(csvfile,fieldnames)
            w.writeheader()
            w.writerows(rows)