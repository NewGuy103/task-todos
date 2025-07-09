import uuid
from pydantic import BaseModel, AwareDatetime


class SubjectBase(BaseModel):
    subject: str
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
