# Create your views here.
import json
from django.views.generic import (
  ListView,
  UpdateView,
  CreateView,
)

from django.core.urlresolvers import reverse
from contractions.models import Contraction
from django.http import HttpResponse

from django.http import HttpResponseRedirect

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class ContractionList(ListView):
  model = Contraction
  template_name = 'list_contractions.html'

class ContractionListTable(ListView):
  model = Contraction
  template_name = 'list_contractions_table.html'

class UpdateIntensity(AjaxableResponseMixin,UpdateView):
  model = Contraction
  template_name = 'list_contractions.html'

  def get_success_url(self):
    return reverse('ContractionList')

class UpdateIntensity2(UpdateView):
  model = Contraction
  template_name = 'edit_contractions.html'

  def get_success_url(self):
    return reverse('ContractionList')

class StartContraction(CreateView):
  model = Contraction
  template_name = 'list_contractions.html'

  def get_success_url(self):
    return reverse('ContractionList')

class StopContraction(AjaxableResponseMixin,UpdateView):
  model = Contraction
  template_name = 'list_contractions.html'
  
  def get_success_url(self):
    return reverse('ContractionList')
