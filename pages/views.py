from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contacts.models import CompanyInformation, Testimonial, Portfolio, Services, ServicesLogos
# Create your views here.

def index(request):
    try:
        services = Services.objects.all()[:4]
        company = CompanyInformation.objects.get(id=1)
    except:
        services = []
        company = []

    context = {'services': services, 'company': company}
    return render(request, 'pages/index.html', context)

def about(request):
    try:
        company = CompanyInformation.objects.get(id=1)
        services = Services.objects.all()[2:4]
        testimonials = Testimonial.objects.all().order_by('upload_date')
    except:
        company = []
        services = []
        testimonials = []

    context = {'company': company, 'testimonials': testimonials, 'services': services}
    return render(request, 'pages/about.html', context)
    
def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('upload_date')    

   # listing per pagina
    paginator = Paginator(portfolios, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'portfolios': paged_listings}
    return render(request, 'pages/portfolio.html', context)

def services(request):
    services = Services.objects.all().order_by('upload_date')  
    logos = ServicesLogos.objects.all().order_by('upload_date')  

    context = {'services': services, 'logos': logos}
    return render(request, 'pages/services.html', context)