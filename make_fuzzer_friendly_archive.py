#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#******************************************************************************
#  $Id: make_fuzzer_friendly_archive.py 32639 2016-01-01 16:41:52Z rouault $
#
#  Project:  GDAL
#  Purpose:  Make fuzzer friendly archive (only works in DEBUG mode)
#  Author:   Even Rouault, <even dot rouault at spatialys dot com>
#
#******************************************************************************
#  Copyright (c) 2016 Even Rouault, <even dot rouault at spatialys dot com>
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#******************************************************************************

import os
import sys

fout = open(sys.argv[1], "wb")
fout.write('FUZZER_FRIENDLY_ARCHIVE\n'.encode('ascii'))
for filename in sys.argv[2:]:
    fout.write(('***NEWFILE***:%s\n' % os.path.basename(filename)).encode('ascii'))
    fout.write(open(filename, 'rb').read())
fout.close()
