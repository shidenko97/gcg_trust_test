from django.views.generic import ListView

from app.models import Pixels


class PixelsListView(ListView):
    """Pixels table view"""

    model = Pixels
    paginate_by = 100
    template_name = "app/pixels_list.html"
