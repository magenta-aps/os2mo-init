# Generated by ariadne-codegen on 2024-08-13 19:15
# Source: queries.graphql

from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class RootOrgQuery(BaseModel):
    org: "RootOrgQueryOrg"


class RootOrgQueryOrg(BaseModel):
    uuid: UUID
    municipality_code: Optional[int]


RootOrgQuery.update_forward_refs()
RootOrgQueryOrg.update_forward_refs()
