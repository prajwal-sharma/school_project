from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from . import models


# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School
    # it searches for school_list.html by default if you have't specified the template name
    # if you have made a html file that is other that school_list.html then you have to specify the template name
    # template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    # template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School
    # success_url = reverse_lazy("basic_app:list")
    # if you don't have success_url then it will check for get_absolute_url by default


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    template_name = 'basic_app/school_del.html'
    success_url = reverse_lazy("basic_app:list")


class CBView(View):
    def get(self, request):
        return HttpResponse('Class Based Views are Cool!')


class StudentListView(ListView):
    model = models.Student


class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    model = models.Student


class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = models.Student


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:studentlist")
