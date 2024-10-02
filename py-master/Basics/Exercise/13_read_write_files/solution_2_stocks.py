with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f) # skip first line
    for lines in f:
        lines = lines.split(",")
        pe_ratio = round(float(lines[1]) / float(lines[2]), 2)
        price_to_book_ratio = round(float(lines[1]) / float(lines[3]), 2)
        out.write(f'{lines[0]},{pe_ratio},{price_to_book_ratio}\n')