# Copyright 2019,2020,2021 Sony Corporation.
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

import pytest
import numpy as np
import nnabla.functions as F
from nbla_test_utils import list_context

ctxs = list_context('Pow2')


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inplace", [False, True])
def test_pow2_double_backward(inplace, seed, ctx, func_name):
    from nbla_test_utils import backward_function_tester
    rng = np.random.RandomState(seed)
    inputs = [(rng.randint(5, size=(2, 3)).astype(np.float32) + 1.0) * 0.75,
              rng.randn(2, 3).astype(np.float32), ]
    backward_function_tester(rng, F.pow2,
                             inputs=inputs,
                             func_args=[inplace], func_kwargs={},
                             atol_accum=5e-2,
                             dstep=1e-3,
                             ctx=ctx)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inplace", [False, True])
def test_pow2_forward_backward(inplace, seed, ctx, func_name):
    from nbla_test_utils import function_tester
    rng = np.random.RandomState(seed)
    inputs = [(rng.randint(5, size=(2, 3)).astype(np.float32) + 1.0) * 0.75,
              rng.randn(2, 3).astype(np.float32), ]
    function_tester(rng, F.pow2, np.power, inputs,
                    ctx=ctx, func_name=func_name, atol_b=2e-3)


@pytest.mark.parametrize("ctx, func_name", ctxs)
@pytest.mark.parametrize("seed", [313])
@pytest.mark.parametrize("inplace", [False, True])
def test_pow2_forward_backward_with_reset(inplace, seed, ctx, func_name):
    from nbla_test_utils import function_tester
    rng = np.random.RandomState(seed)
    inputs = [(rng.randint(3, size=(2, 3)).astype(np.float32) + 1.0) * 0.75,
              rng.randn(2, 3).astype(np.float32), ]
    reset_inputs = [(rng.randint(5, size=(2, 2)).astype(np.float32) + 1.0) * 0.75,
                    rng.randn(2, 2).astype(np.float32), ]
    function_tester(rng, F.pow2, np.power, inputs,
                    ctx=ctx, func_name=func_name, atol_b=2e-3, reset_inputs=reset_inputs)
