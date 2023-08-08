from django.views.generic import TemplateView


class CalculatorView(TemplateView):
    template_name = "index.html"
