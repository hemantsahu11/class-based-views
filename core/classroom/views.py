from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher
from django.urls import reverse_lazy, reverse
# Create your views here.


# def home(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # url not a template.html
    success_url = '/classroom/thankyou'   # or reverse_lazy('classroom:thankyou')  # which url to go after successful submission of forms (actual url ) not html file name
                                        # we also can not use reverse function in success_url we can use reverse_lazy instead of it

    # what to do with form
    def form_valid(self, form):
        # form.save()
        print(form.cleaned_data)   # printing form data on screen
        return super().form_valid(form)               # same as ContactForm(request, POST )


class TeacherCreateView(CreateView):
    model = Teacher       # view connected with model it will directly create form for the creation of teacher
    #model_form.html    automatically called by looking at convention
    #form.save()
    fields = '__all__'       # here you need to mention which things you want to show into forms you can change the order also by passing the list
    success_url = reverse_lazy('classroom:thankyou')


class TeacherListView(ListView):
    #teacher_list.html   # by default call this by using convention
    model = Teacher    # this by default calls the objects.all() and links to the thing
    queryset = Teacher.objects.order_by('name')     # we are overiding the default query i.e. Teacher.objects.all()
    context_object_name = "teacher_list"   # this teacher list will be passed to html template


# the purpose of detail view is to view a single instance's all fields
class TeacherDetailView(DetailView):
    #looks for teacher_detail.html
    model = Teacher
    #pk--> {{teacher}}   find teacher by primary key and send object


class TeacherUpdateView(UpdateView):
    # share model_form.html file   and then show us filled form we can make changes to that
    model = Teacher
    fields = '__all__'    # list of values to update
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView(DetailView):
    # it send form----> that has confirm delete button
    # looks for model_confirm_delete.html
    template_name = 'classroom/teacher_confirm_delete.html'
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')



