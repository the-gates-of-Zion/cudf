/*
 * Copyright (c) 2019, NVIDIA CORPORATION.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#pragma once

#include <cudf/strings/strings_column_view.hpp>
#include <cudf/column/column.hpp>

namespace cudf
{
namespace strings
{

/**---------------------------------------------------------------------------*
 * @brief Returns a new numeric column parsing integer values from the
 * provided strings column.
 *
 * @param strings Strings instance for this operation.
 * @param mr Resource for allocating device memory.
 * @return New strings column with integers as strings.
 *---------------------------------------------------------------------------**/
std::unique_ptr<cudf::column> to_integers( strings_column_view strings,
                                           rmm::mr::device_memory_resource* mr = rmm::mr::get_default_resource() );


/**---------------------------------------------------------------------------*
 * @brief Returns a new strings column converting the integer values from the
 * provided column into strings.
 *
 * @param column Numeric column to convert.
 * @param mr Resource for allocating device memory.
 * @return New strings column with integers as strings.
 *---------------------------------------------------------------------------**/
std::unique_ptr<cudf::column> from_integers( column_view integers,
                                             rmm::mr::device_memory_resource* mr = rmm::mr::get_default_resource() );


} // namespace strings
} // namespace cudf
