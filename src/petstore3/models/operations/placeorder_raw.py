"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import order as shared_order
from typing import Optional



@dataclasses.dataclass
class PlaceOrderRawResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    order: Optional[shared_order.Order] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

