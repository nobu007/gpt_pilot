from database.models.components.progress_step import ProgressStep
from peewee import TextField


class ProjectDescription(ProgressStep):
    prompt = TextField()
    summary = TextField()

    class Meta:
        table_name = "project_description"
