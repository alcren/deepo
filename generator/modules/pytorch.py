# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python


@dependency(Python)
@source('pip')
class Pytorch(Module):

    def build(self):
        cuver = 'cpu' if self.composer.cuda_ver is None else 'cu%d' % (
            float(self.composer.cuda_ver) * 10)
        return r'''
            $PIP_INSTALL \
                torch_nightly -f \
                https://download.pytorch.org/whl/nightly/%s/torch_nightly.html \
                && \
        ''' % cuver
