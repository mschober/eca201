import sys
from xlsconv import XlsConv
src_file = sys.argv[1]
tgt_file = sys.argv[2]

xconv = XlsConv(src_file, tgt_file)
xconv.convert()

print "Success!"
