from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.MemberType import MemberType as MemberTypeModel
from ..models.MemberResponse import MemberResponse as MemberResponseModel


class Retrieve(BaseService):
    def member(
        self, member_slug: str, member_type: MemberTypeModel, group_slug: str
    ) -> MemberResponseModel:
        """
        Retrieve Member
        Parameters:
        ----------
            group_slug: str
                The group's slug
            member_type: MemberType
            member_slug: str
                The member's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{group_slug}/members/{member_type}/{member_slug}"
        headers = {}
        self._add_required_headers(headers)
        if not group_slug:
            raise ValueError(
                "Parameter group_slug is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{group_slug}",
            quote(
                str(query_serializer.serialize_path("simple", False, group_slug, None))
            ),
        )
        if not member_type:
            raise ValueError(
                "Parameter member_type is required, cannot be empty or blank."
            )
        validated_member_type = self._enum_matching(
            member_type, MemberTypeModel.list(), "member_type"
        )
        url_endpoint = url_endpoint.replace(
            "{member_type}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_member_type, None
                    )
                )
            ),
        )
        if not member_slug:
            raise ValueError(
                "Parameter member_slug is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{member_slug}",
            quote(
                str(query_serializer.serialize_path("simple", False, member_slug, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return MemberResponseModel(**res)
        return res
