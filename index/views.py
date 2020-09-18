from django.views.generic import TemplateView

from .forms import SearchForm


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        return {'greeting': 'Hello, Django!'}


class SearchView(TemplateView):
    template_name = 'index/search.html'

    def get_context_data(self, **kwargs):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('q')
            results = self.get_search_results(query)
            count = len(results)
            return {'query': query, 'results': results, 'count': count}
        else:
            return {}

    def get_search_results(self, query):
        return 'Search not yet implemented'.split()
