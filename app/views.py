from django.shortcuts import render, get_object_or_404
from app.models import About
from app.models import AboutFeed
from app.models import Service
from app.models import Staff
from app.models import Consultancyservice
from blog.models import Categories, Posts
from app.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse


# Create your views here.
def index(request):
    homeabout = About.objects.get(title='Aimurafaty')
    homeservices = Service.objects.all()[:6]
    categories = Categories.objects.all()
    posts = Posts.objects.all()[:5]
    clientfeeds = AboutFeed.objects.all()
    context_dict = {'about': homeabout, 'services': homeservices, 'feeds': clientfeeds,
                    'categories': categories, 'posts': posts}
    return render(request, 'app/index.html', context=context_dict)


def about(request):
    aboutus = About.objects.get(title='Aimurafaty')
    skills = Service.objects.all()
    cskills = Consultancyservice.objects.all()[:6]
    staff = Staff.objects.all()
    context_dict = {'about': aboutus, 'skills': skills, 'cskills': cskills, 'staff': staff}
    return render(request, 'app/about.html', context=context_dict)


def services(request):
    service = Service.objects.all()
    cservices = Consultancyservice.objects.all()[:2]
    context_dict = {'services': service, 'cservices': cservices}
    return render(request, 'app/services.html', context=context_dict)


def services_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context_dict = {'service': service}
    return render(request, 'app/services_detail.html', context=context_dict)


def cservices_detail(request, pk):
    cservice = get_object_or_404(Consultancyservice, pk=pk)
    context_dict = {'cservice': cservice}
    return render(request, 'app/cservices_detail.html', context=context_dict)


def staff(request):
    staffs = Staff.objects.all()[:6]
    context_dict = {'staff': staffs}
    return render(request, 'app/staff.html', context=context_dict)


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['aimurafaty@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Your Message was sent successfully')
            return redirect('contact')
    return render(request, 'app/contact.html', {'form': form_class})

