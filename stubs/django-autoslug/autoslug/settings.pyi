from collections.abc import Callable

from django import VERSION as VERSION

slugify_function_path: str
slugify: Callable[[str], str]
autoslug_modeltranslation_enable: bool
