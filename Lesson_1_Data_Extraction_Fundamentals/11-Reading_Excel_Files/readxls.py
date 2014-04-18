#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min and max values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
   


    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(7200, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    max_candidate = sheet.cell_value(1, 1)
    max_row = 0
    min_candidate, min_row = max_candidate, max_row
    total = 0

    for r in range(1, sheet.nrows):
        # used for loop to only loop through list once,
        # but it has more comparisons and declarations
        # than slicing methods
        total += sheet.cell_value(r, 1)
        if sheet.cell_value(r, 1) > max_candidate:
            max_candidate = sheet.cell_value(r, 1)
            max_row = r
        elif sheet.cell_value(r, 1) < min_candidate:
            min_candidate = sheet.cell_value(r, 1)
            min_row = r


    data = {
            'maxtime': xlrd.xldate_as_tuple(sheet.cell_value(max_row, 0), 0),
            'maxvalue': max_candidate,
            'mintime': xlrd.xldate_as_tuple(sheet.cell_value(min_row, 0), 0),
            'minvalue': min_candidate,
            'avgcoast': total / (sheet.nrows - 1)
    }


    return data


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()