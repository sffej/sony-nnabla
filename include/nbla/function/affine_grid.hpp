// Copyright (c) 2017 Sony Corporation. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef NBLA_FUNCTION_AFFINE_GRID_HPP
#define NBLA_FUNCTION_AFFINE_GRID_HPP

#include <nbla/cpu.hpp>
#include <nbla/function.hpp>
#include <nbla/function/batch_matmul.hpp>
#include <nbla/function_registry.hpp>
#include <nbla/imperative.hpp>

namespace nbla {

NBLA_REGISTER_FUNCTION_HEADER(AffineGrid, const vector<int> &, bool);

/**
    @todo Write doc.

Inputs:

Outputs:

\ingroup FunctionImplGrp
 */
template <typename T>
class AffineGrid : public BaseFunction<const vector<int> &, bool> {
protected:
  const vector<int> size_;
  bool align_corners_;
  shared_ptr<Function> batch_matmul_;

public:
  AffineGrid(const Context &ctx, const vector<int> &size, bool align_corners)
      : BaseFunction(ctx, size, align_corners), size_(size),
        align_corners_(align_corners) {}
  virtual ~AffineGrid() {}
  virtual shared_ptr<Function> copy() const {
    return create_AffineGrid(ctx_, size_, align_corners_);
  }
  virtual int min_inputs() { return 1; }
  virtual int min_outputs() { return 1; }
  virtual vector<dtypes> in_types() { return vector<dtypes>{get_dtype<T>()}; }
  virtual vector<dtypes> out_types() { return vector<dtypes>{get_dtype<T>()}; }
  virtual vector<string> allowed_array_classes() {
    return SingletonManager::get<Cpu>()->array_classes();
  }
  virtual string name() { return "AffineGrid"; }

protected:
  NBLA_API virtual void setup_impl(const Variables &inputs,
                                   const Variables &outputs);
  NBLA_API virtual void forward_impl(const Variables &inputs,
                                     const Variables &outputs);
  NBLA_API virtual void backward_impl(const Variables &inputs,
                                      const Variables &outputs,
                                      const vector<bool> &propagate_down,
                                      const vector<bool> &accum);
};
}
#endif
