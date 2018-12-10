# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from .quantumalgorithm import QuantumAlgorithm
from .adaptive import VQE, QAOA, QSVMVariational
from .classical import ExactEigensolver, SVM_Classical
from .many_sample import EOH, QSVM_Kernel
from .single_sample import Grover, IQPE, QPE

__all__ = ['QuantumAlgorithm',
           'VQE',
           'QAOA',
           'QSVMVariational',
           'ExactEigensolver',
           'SVM_Classical',
           'EOH',
           'QSVM_Kernel',
           'Grover',
           'IQPE',
           'QPE',
           ]

try:
    from .classical import CPLEX_Ising
    __all__ += ['CPLEX_Ising']
except ImportError:
    pass