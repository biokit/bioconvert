# -*- coding: utf-8 -*-
##############################################################################
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
##############################################################################
""" description """
import colorlog
from bioconvert import ConvBase, extensions
from bioconvert.bam2bed import BAM2BED
from bioconvert.bedgraph2bigwig import BEDGRAPH2BIGWIG
from easydev import TempFile


_log = colorlog.getLogger(__name__)

__all__ = ["BAM2BIGWIG"]


class BAM2BIGWIG(ConvBase):
    """Convert :term:`BAM` file to :term:`BIGWIG` file

    Some description.

    """

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input BAM file
        :param str outfile: output BIGWIG filename

        command used::
            bamCoverage -bam {} –-outFileFormat bigwig --outFileName {}


        """
        super(BAM2BIGWIG, self).__init__(infile, outfile, *args, **kargs)

        self._default_method = "bamCoverage"

    def _method_bamCoverage(self, *args, **kwargs):
        """run bam2bigwig from deeptools package"""
        cmd = "bamCoverage --bam {} --outFileFormat bigwig --outFileName {}".format(self.infile, self.outfile)
        self.execute(cmd)

#     def _method_ucsc(self, *args, **kwargs):
#         """run bam2bigwig using bioconvert bam2Bed and ucsc tool bedGraphToBigWig"""
#         with TempFile(suffix='.bed') as fh:
#             convertbam2bed = BAM2BED(self.infile, fh.name)
#             convertbam2bed()
#             convertbed2bw = BEDGRAPH2BIGWIG(fh.name, self.outfile)
#             convertbed2bw()


