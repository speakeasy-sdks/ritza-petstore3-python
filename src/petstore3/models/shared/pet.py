"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import category as shared_category
from ..shared import tag as shared_tag
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from petstore3 import utils
from typing import Optional

class PetStatus(str, Enum):
    r"""pet status in the store"""
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pet:
    r"""Create a new pet in the store"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }, 'form': { 'field_name': 'name' }})
    photo_urls: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoUrls') }, 'form': { 'field_name': 'photoUrls' }})
    category: Optional[shared_category.Category] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'category', 'json': True }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'id' }})
    status: Optional[PetStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'status' }})
    r"""pet status in the store"""
    tags: Optional[list[shared_tag.Tag]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'tags', 'json': True }})
    