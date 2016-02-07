import csv
from openpyxl import Workbook
from openpyxl.cell import get_column_letter

class XlsConv:

    def __init__(self, src_file, tgt_file, title="output.xlsx"):
        self.src_file = src_file
        self.tgt_file = tgt_file
        self.wb = #fixme
        self.ws = #fixme
        self.ws.title = #fixme
        self.reader = self.make_reader(src_file)

    def make_reader(self, src_file):
        #implementme


    def save_file(self, tgt_file, wb):
        #implementme


    def convert(self):
        print "The source file is %s" % #fixme
        print "The target file is %s" % #fixme

        print "Begin converting to xlsx..."
        #implementme

        print "Saving the converted file..."
        self.save_file(#fixme)
