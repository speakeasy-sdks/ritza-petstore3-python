"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user as shared_user
from typing import Optional



@dataclasses.dataclass
class CreateUserJSONResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    r"""successful operation"""
    

