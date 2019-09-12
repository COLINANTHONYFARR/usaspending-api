import logging

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from usaspending_api.awards.models import FinancialAccountsByAwards
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.common.validator.tinyshield import TinyShield
from usaspending_api.common.validator.award import get_internal_or_generated_award_id_model


logger = logging.getLogger("console")


class FederalAccountCountRetrieveViewSet(APIView):
    """
    This route sends a request to the backend to retrieve data about a specific award
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/awards/federal_account_count.md"

    def _parse_and_validate_request(self, provided_award_id: str) -> dict:
        request_dict = {"award_id": provided_award_id}
        models = get_internal_or_generated_award_id_model()
        return TinyShield([models]).block(request_dict)

    def _business_logic(self, request_data: dict) -> list:

        award_id = request_data["award_id"]
        award_id_column = "award_id" if type(award_id) is int else "award__generated_unique_award_id"
        filter = {award_id_column: award_id}

        federal_account_queryset = FinancialAccountsByAwards.objects.filter(**filter).count()
        response_content = {"federal_accounts": federal_account_queryset}
        return response_content

    @cache_response()
    def get(self, request: Request, requested_award: str) -> Response:
        request_data = self._parse_and_validate_request(requested_award)
        results = self._business_logic(request_data)
        return Response(results)
