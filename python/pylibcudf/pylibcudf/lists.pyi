# Copyright (c) 2024, NVIDIA CORPORATION.

from enum import IntEnum

from pylibcudf.column import Column
from pylibcudf.scalar import Scalar
from pylibcudf.table import Table
from pylibcudf.types import NanEquality, NullEquality, NullOrder, Order

class ConcatenateNullPolicy(IntEnum):
    IGNORE = ...
    NULLIFY_OUTPUT_ROW = ...

class DuplicateFindOption(IntEnum):
    FIND_FIRST = ...
    FIND_LAST = ...

def explode_outer(input: Table, explode_column_idx: int) -> Table: ...
def concatenate_rows(input: Table) -> Column: ...
def concatenate_list_elements(
    input: Column, null_policy: ConcatenateNullPolicy
) -> Column: ...
def contains(input: Column, search_key: Column | Scalar) -> Column: ...
def contains_nulls(input: Column) -> Column: ...
def index_of(
    input: Column,
    search_key: Column | Scalar,
    find_option: DuplicateFindOption,
) -> Column: ...
def reverse(input: Column) -> Column: ...
def segmented_gather(input: Column, gather_map_list: Column) -> Column: ...
def extract_list_element(input: Column, index: Column | int) -> Column: ...
def count_elements(input: Column) -> Column: ...
def sequences(
    starts: Column, sizes: Column, steps: Column | None = None
) -> Column: ...
def sort_lists(
    input: Column,
    sort_order: Order,
    na_position: NullOrder,
    stable: bool = False,
) -> Column: ...
def difference_distinct(
    lhs: Column,
    rhs: Column,
    nulls_equal: NullEquality = NullEquality.EQUAL,
    nans_equal: NanEquality = NanEquality.ALL_EQUAL,
) -> Column: ...
def have_overlap(
    lhs: Column,
    rhs: Column,
    nulls_equal: NullEquality = NullEquality.EQUAL,
    nans_equal: NanEquality = NanEquality.ALL_EQUAL,
) -> Column: ...
def intersect_distinct(
    lhs: Column,
    rhs: Column,
    nulls_equal: NullEquality = NullEquality.EQUAL,
    nans_equal: NanEquality = NanEquality.ALL_EQUAL,
) -> Column: ...
def union_distinct(
    lhs: Column,
    rhs: Column,
    nulls_equal: NullEquality = NullEquality.EQUAL,
    nans_equal: NanEquality = NanEquality.ALL_EQUAL,
) -> Column: ...
def apply_boolean_mask(input: Column, boolean_mask: Column) -> Column: ...
def distinct(
    input: Column, nulls_equal: NullEquality, nans_equal: NanEquality
) -> Column: ...