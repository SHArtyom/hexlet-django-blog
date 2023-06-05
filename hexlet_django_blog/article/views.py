from django.views import View
from django.shortcuts import render, redirect


class IndexView(View):

    def get(self, request, *args, **kwargs):
        if not kwargs:
            return redirect('article', tags='python', article_id=42)
        return render(request, 'article/index.html', context=kwargs)
