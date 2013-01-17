#################################################################################
# Copyright (c) 2011-2013, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

# Author: David Alexander

import time
from pbcore.io import GffWriter
from GenomicConsensus import __VERSION__

class VariantsGffWriter(object):

    ONTOLOGY_URL = \
        "http://song.cvs.sourceforge.net/*checkout*/song/ontology/sofa.obo?revision=1.12"

    def __init__(self, f, shellCommand, referenceEntries):
        self._gffWriter = GffWriter(f)
        self._gffWriter.writeMetaData("pacbio-variant-version", "1.4")
        self._gffWriter.writeMetaData("date", time.ctime())
        self._gffWriter.writeMetaData("feature-ontology", self.ONTOLOGY_URL)
        self._gffWriter.writeMetaData("source", "GenomicConsensus %s" % __VERSION__)
        self._gffWriter.writeMetaData("source-commandline",  shellCommand)

        # Reference groups.
        for entry in referenceEntries:
            self._gffWriter.writeMetaData("sequence-region", "%s 1 %d" \
                                          % (entry.header, entry.length))

    def writeRecord(self, gffRecord):
        self._gffWriter.writeRecord(gffRecord)