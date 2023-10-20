from collections.abc import Callable, Sequence
from typing import Any

from django.db.models import Manager, Model
from django.db.models.fields import SlugField

basestring = str

class AutoSlugField(SlugField):
    populate_from: str
    unique_with: str | Sequence[str]
    slugify: Callable[[str], str]
    index_sep: str
    allow_unicode: bool
    manager: type[Manager]
    manager_name: str
    always_update: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self) -> tuple[str, str, tuple, dict[str, Any]]: ...
    def pre_save(self, instance: Model, add: bool): ...
