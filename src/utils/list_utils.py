from typing import List, TypeVar, Optional

T = TypeVar("T")


class ListUtils:
  def is_empty(list: List[T]) -> bool:
    return len(list) == 0

  """
  Given a list and a value, returns the index of value or None if value is not
  found.
  """
  def index_of_or_none(list: List[T], value: T) -> Optional[int]:
    try:
      return list.index(value)
    except ValueError:
      return None
