from django_filters import BaseInFilter, DateFilter, FilterSet

from app.models import Pixels


class PixelsFilter(FilterSet):
    """Filter for pixel view table"""

    countries = BaseInFilter(field_name="country")
    date_from = DateFilter(field_name="event_time", lookup_expr="gte")
    date_to = DateFilter(field_name="event_time", lookup_expr="lte")

    class Meta:
        model = Pixels
        fields = ["affiliateId", "action", "countries", "date_from", "date_to"]
