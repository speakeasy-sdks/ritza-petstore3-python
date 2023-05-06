"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class LoginUserRequest:
    
    password: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'password', 'style': 'form', 'explode': True }})
    r"""The password for login in clear text"""
    username: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'username', 'style': 'form', 'explode': True }})
    r"""The user name for login"""
    

@dataclasses.dataclass
class LoginUserResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    login_user_200_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""successful operation"""
    login_user_200_application_xml_string: Optional[str] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    