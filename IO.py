import csv

import os


class IO:
    minHeaders = ["title", "author", "brand", "genre", "id","remixers", "released"]

    def __init__(self,csvfile):
        self.csvfile=csvfile


    def read(self):
        songs=[]

        with open(self.csvfile,"r") as csvfile:
            rows = csv.DictReader(csvfile,delimiter=",")
            for row in rows:
                songs.append(row)
                #print row["id"]
        return songs

    def getFieldnames(self):
        if os.path.isfile(self.csvfile):
            with open(self.csvfile, "r") as csvfile:
                rows = csv.DictReader(csvfile)
                headers = rows.fieldnames
            return headers
        return IO.minHeaders


    def write(self, rows,fnames):
        f = open(self.csvfile, 'w')
        with f:
            #fnames = ['first_name', 'last_name']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writeheader()
            for row in rows:
                for field in fnames:
                   if not field in row:
                       row[field]="NA"
                writer.writerow(row)

