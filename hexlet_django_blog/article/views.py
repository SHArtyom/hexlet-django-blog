from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "article/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Articles'
        return context
