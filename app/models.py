import uuid
from pydantic import BaseModel, AwareDatetime
from enum import IntEnum


class SortingModeEnum(IntEnum):
    disabled = 0
    deadline = 1
    alphabetical = 2


class DeadlineSortingEnum(IntEnum):
    closest_to_deadline = 0
    farthest_to_deadline = 1


class AlphabeticalSortingEnum(IntEnum):
    a_to_z = 0
    z_to_a = 1


class FilterCompletedTasksEnum(IntEnum):
    incomplete = 0
    complete = 1
    dont_filter = 2


class BuiltinCategories(IntEnum):
    quiz = 0
    essay = 1
    individual_work = 2
    group_work = 3
    project = 4
    notes = 5
    custom = 6


class SubjectBase(BaseModel):
    subject: str
    category: BuiltinCategories = BuiltinCategories.custom
    deadline: AwareDatetime
    task: str


class EditedSubjectTask(SubjectBase):
    pass


class EditedTaskWithID(SubjectBase):
    completed: bool
    task_id: uuid.UUID


class SubjectTask(SubjectBase):
    completed: bool
    task_id: uuid.UUID


# State models
class SortState(BaseModel):
    sort_mode: SortingModeEnum = SortingModeEnum.disabled
    sort_option: DeadlineSortingEnum | AlphabeticalSortingEnum | None = None


class DeadlineFilterState(BaseModel):
    enabled: bool
    not_before: AwareDatetime
    not_after: AwareDatetime


class FilterState(BaseModel):
    """Filter state.

    `subject` and `category` being a boolean means either:
      - True: Include all subjects
      - False: Don't include any subjects from this filter

    """

    subject: str | bool
    category: BuiltinCategories | bool
    deadline: DeadlineFilterState
    completed: FilterCompletedTasksEnum


class SortAndFilterState(BaseModel):
    sort_state: SortState
    filter_state: FilterState
