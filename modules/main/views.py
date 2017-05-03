# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .models import Employee, Skill, Experience, Project


class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        user = Employee.objects.filter().first()
        context.update({
            'user': user,
            'skills': Skill.objects.filter(employee_id=user.id),
            'works': Experience.objects.all(),
            'projects': Project.objects.all()
        })
        return context

home_page = HomePageView.as_view()


class RobotsPageView(TemplateView):
    template_name = 'robots.txt'

robots_page = RobotsPageView.as_view(content_type='text/plain')


class ErrorPageView(TemplateView):
    """
        Дочерние вьюхи должны иметь установленное значение параметра
        status_code - возвращаемый статус ответа
    """
    status_code = None

    def get(self, request, *args, **kwargs):
        response = super(ErrorPageView, self).get(request, *args, **kwargs)
        response.status_code = self.status_code
        return response


class Page404View(ErrorPageView):
    template_name = "404.html"
    status_code = 404

page_404 = Page404View.as_view()


class Page500View(ErrorPageView):
    template_name = "500.html"
    status_code = 500


page_500 = Page500View.as_view()


def load_services(request):
    services_file = open("static/files/services.docx", "rb")
    response = HttpResponse(content=services_file)
    response['Content-Type'] = 'application/docx'
    response['Content-Disposition'] = 'attachment; filename="{}.docx"'\
                                      .format('services')
    return response
