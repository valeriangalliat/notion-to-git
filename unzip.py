#
# Custom script to truncate filename too long since no existing CLI tool
# does that.
#

import os
import sys
import zipfile

with zipfile.ZipFile(sys.argv[1], 'r') as zip_ref:
    for file_info in zip_ref.infolist():
        filename = file_info.filename
        basename = os.path.basename(filename)

        if len(basename) > 255:
            print('Truncating', basename)
            dirname = os.path.dirname(filename)
            basename = basename[0:255]
            filename = dirname + '/' + basename
            file_info.filename = filename
            zip_ref.extract(file_info)
        else:
            zip_ref.extract(file_info)
