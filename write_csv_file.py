from csv import writer

header = ["ID", "Title", "Quant", "Match","Context", "Speakers", "Date", "Link", "Amount of clauses"]

def write_csv():
    with open('countries.csv', 'w', encoding='UTF8') as f:
        csv_writer = writer(f)
        csv_writer.writerow(header)

        #write data