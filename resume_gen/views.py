from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm
from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponse
import pdfkit
from django.template import loader


# Create your views here.
class ProfileCreation(CreateView):
    template_name = "resume_gen/accept.html"
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("resume-list")

class ResumeDetailView(DetailView):
    template_name = "resume_gen/resume.html"
    context_object_name = "profile"
    model = Profile

    def render_to_response(self, context, **response_kwargs) -> HttpResponse:
        template = loader.get_template(self.template_name)
        html = template.render(context, self.request)
        options = {"page-size": "Letter", "encoding": "UTF-8"}
        pdf = pdfkit.from_string(html, False, options)
        # return super().render_to_response(context, **response_kwargs)
        return HttpResponse(pdf, content_type="application/pdf", headers={"Content-Disposition": "attachment"})


class ProfileListview(ListView):
    template_name = "resume_gen/list.html"
    model = Profile
    context_object_name= "profiles"
    