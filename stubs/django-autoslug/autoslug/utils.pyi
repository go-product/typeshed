from collections.abc import Callable, Generator, Sequence
from typing import Any
from typing_extensions import TypeAlias

from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db.models import Field, Manager, Model
from django.template.defaultfilters import slugify as django_slugify

SlugifyFunction: TypeAlias = Callable[[str], str]
slugify = django_slugify

def get_prepopulated_value(field: Field, instance: Model) -> Any: ...
def generate_unique_slug(field: Field, instance: Model, slug: str, manager: Manager) -> str: ...
def get_uniqueness_lookups(
    field: Field, instance: Model, unique_with: str | Sequence[str]
) -> Generator[tuple[str, str], None, None]: ...
def crop_slug(field: Field, slug: str) -> str: ...

try:
    import translitcodec
except ImportError:
    pass
else:
    from re import Pattern

    PUNCT_RE: Pattern

    def translitcodec_slugify(codec: str) -> SlugifyFunction: ...

    translit_long: SlugifyFunction
    translit_short: SlugifyFunction
    translit_one: SlugifyFunction
