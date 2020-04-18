from datetime import date, timedelta

from django_filters.views import FilterView

from app.filters import PixelsFilter
from app.models import Pixels


class PixelsListView(FilterView):
    """Pixels table view"""

    model = Pixels
    paginate_by = 100
    template_name = "app/pixels_list.html"
    filterset_class = PixelsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Variables for filters
        context["actions"] = list(filter(len, self.model.get_actions()))
        context["selected_action"] = self.request.GET.get("action", "")
        context["countries"] = list(filter(len, self.model.get_countries()))
        context["selected_countries"] = (self.request.GET.get("countries", "")
                                         .split(","))
        context["date_from"] = self.request.GET.get("date_from", "")
        context["date_to"] = self.request.GET.get("date_to", "")

        # Variables for date range shortcuts
        today = date.today()
        context["tomorrow"] = today + timedelta(days=1)
        context["today"] = today
        context["yesterday"] = today - timedelta(days=1)
        context["last_week"] = today - timedelta(days=7)
        context["last_month"] = today - timedelta(days=30)
        context["last_year"] = today - timedelta(days=365)

        return context
