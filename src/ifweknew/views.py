from django.views.generic import CreateView
from django.forms import ModelForm
from ifweknew.models import Wish

class WishesView (CreateView):
    model = Wish
    template_name = 'index.html'

wishes_view = WishesView.as_view()
