from django.views.generic import CreateView
from django.forms import ModelForm
from django.conf import settings
from django.core.urlresolvers import reverse
from ifweknew.models import Wish
from twitter import Twitter, OAuth

class WishesView (CreateView):
    model = Wish
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('wishes', args=[])

    def form_valid(self, form):
        result = super(WishesView, self).form_valid(form)

        # Build the status message
        status_parts = {
            'mystery': self.object.mystery,
            'goal': self.object.goal,
            'place': self.object.place,
        }
        status = u'#IfWeKnew {mystery} then we could {goal} in {place}'.format(**status_parts)

        # Tweet
        twitter = Twitter(
            auth=OAuth(
                settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET,
                settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET
            ), api_version=1)
        twitter.statuses.update(status=status)

        return result

wishes_view = WishesView.as_view()
