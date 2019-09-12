import logging

from django.db.models import Max
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from usaspending_api.awards.models import Award
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.common.validator.tinyshield import TinyShield
from usaspending_api.common.validator.award import get_internal_or_generated_award_id_model


logger = logging.getLogger("console")


class SubawardCountRetrieveViewSet(APIView):
    """
    This route sends a request to the backend to retrieve data about a specific award
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/awards/subaward_count.md"

    def _parse_and_validate_request(self, provided_award_id: str) -> dict:
        request_dict = {"award_id": provided_award_id}
        models = get_internal_or_generated_award_id_model()
        return TinyShield([models]).block(request_dict)

    def _business_logic(self, request_data: dict) -> list:

        award_id = request_data["award_id"]
        award_id_column = "id" if type(award_id) is int else "generated_unique_award_id"
        filter = {award_id_column: award_id}

        try:
            subaward_queryset = Award.objects.get(**filter)
        except Award.DoesNotExist:
            logger.info("No Award found with: '{}'".format(award_id))
            raise NotFound("No Award found with: '{}'".format(award_id))
        response_content = {"subawards": subaward_queryset.subaward_count}
        return response_content

    @cache_response()
    def get(self, request: Request, requested_award: str) -> Response:
        request_data = self._parse_and_validate_request(requested_award)
        results = self._business_logic(request_data)
        return Response(results)
