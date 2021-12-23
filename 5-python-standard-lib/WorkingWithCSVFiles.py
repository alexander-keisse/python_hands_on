import csv

# Makes sense:

provided_file = './csv-files/Columbus_Ed_astro_pi_datalog.csv'
new_file = './csv-files/own_csv_file.csv'

# In this class we are going to work with CSV files which is an acronym for: Comma Separated File.
# It's like a simplified spreadsheet stored as a plain text file.

# We're going to start by creating a csv file using the good practices we already learned:

with open(new_file, 'w') as file:
    writer = csv.writer(file)
    # The first row is where we set the heading of our columns
    writer.writerow(['transaction_id', 'product_id', 'price'])
    # From the second row to the end of our csv file we fill in our values transaction_id: 1000, product_id: 1, price: 5
    writer.writerow([1000, 1, 5])
    # Some more hardcoded made up data:
    writer.writerow([1001, 2, 420])
    writer.writerow([1002, 1, 5])

# We can also readout a csv file:

with open(provided_file) as file:
    reader = csv.reader(file)
    # We can convert the content of the csv file into a list.
    list_csv = list(reader)
    # We pop our headers so that we can use those to display next to our values
    list_headers = list_csv.pop(0)
    for row in list_csv:
        for i in range(len(row)):  # This way we can easily grab our header and corresponding value
            print(f"{list_headers[i]} : {row[i]}")
        else:  # To make it cleaner, remember if our iteration is not triggering an exception this code gets executed.
            print()
