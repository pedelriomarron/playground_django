from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required,name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')



#class PageUpdate(StaffRequiredMixin,UpdateView):
@method_decorator(staff_member_required,name='dispatch')
class PageUpdate( UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id])+ '?ok'

@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

