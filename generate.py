import csv
with open('out.nt', 'w') as f:
    csvfile = csv.writer(f)
    maxsize = 1024 * 1024 * 4                # max file size in bytes
    while True:
        csvfile.writerow("a")
        if f.tell() > maxsize:    # f.tell() gives byte offset, no need to worry about multiwide chars
            break
