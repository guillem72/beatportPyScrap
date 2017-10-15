import csv
class IO:


    def __init__(self,csvfile):
        self.csvfile=csvfile
        self.headers=None

    def read(self):
        songs=[]

        with open(self.csvfile,"r") as csvfile:
            rows = csv.DictReader(csvfile,delimiter=",")
            for row in rows:
                songs.append(row)
                #print row["id"]
        return songs

    def getFieldnames(self):
        with open(self.csvfile, "r") as csvfile:
            rows = csv.DictReader(csvfile)
            headers = rows.fieldnames
        return headers


    def write(self, rows,fnames):
        f = open(self.csvfile, 'w')
        with f:
            #fnames = ['first_name', 'last_name']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

