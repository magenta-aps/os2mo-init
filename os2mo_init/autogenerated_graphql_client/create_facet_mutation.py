# Generated by ariadne-codegen on 2024-08-13 19:15
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class CreateFacetMutation(BaseModel):
    facet_create: "CreateFacetMutationFacetCreate"


class CreateFacetMutationFacetCreate(BaseModel):
    uuid: UUID


CreateFacetMutation.update_forward_refs()
CreateFacetMutationFacetCreate.update_forward_refs()
