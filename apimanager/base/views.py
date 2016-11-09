# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['OAUTH_API'] = settings.OAUTH_API
        return context
