from django.shortcuts import render, get_object_or_404, redirect
from django.views import View ## to convert FVB to CBV
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
# Create your views here.


#
class CourseView(View):
    template_name = 'about.html'
    def get(self, request):
        return render(request, self.template_name, {})
    #or
    # return render(request, 'about.html', {})

class CourseDetailView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id= None, *args, **kwargs):
        if id is not None:
            obj= get_object_or_404(Course, id=id)
            context = {"object":obj}
            return render(request, self.template_name, context)


# def my_fbv(request):
#     print(request.method)
#     return render(request, 'about.html', {})

class CourseListView(View):
    template_name = 'courses/course_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        context = {"object":queryset}
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, *args, **kwargs):
        form= CourseModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form= CourseModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            form= CourseModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class CourseUpdateView(View):
    template_name = 'courses/course_create.html'

    def get_object(self):
        obj = get_object_or_404(Course, id=self.kwargs.get('id'))
        return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form= CourseModelForm(instance=obj)
        context = {"form":form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form= CourseModelForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            form= CourseModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

# in FVB the update will be
# def course_update_view(request, id):
#     course = get_object_or_404(Course, id=id)
#     form = CourseModelForm(request.POST or None, instance=course) ## you can notice here how to pass instance to edit on DB
#     if form.is_valid():
#         form.save()
#         return redirect('/courses/')
#     return render(request, "courses/course_update.html", {"form": form})

class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'

    def get_object(self):
        obj = get_object_or_404(Course, id=self.kwargs.get('id'))
        return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        context = {"object":obj}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect('/')

