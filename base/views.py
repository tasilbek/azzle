from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
class BlogDetailsPageView(TemplateView):
    template_name = 'pages/blog-details.html'
class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
class Error404PageView(TemplateView):
    template_name = 'pages/error-404.html'
class Faq2PageView(TemplateView):
    template_name = 'pages/faq-2.html'
class FaqPageView(TemplateView):
    template_name = 'pages/faq.html'
class Home2PageView(TemplateView):
    template_name = 'pages/index-2.html'
class Home3PageView(TemplateView):
    template_name = 'pages/index-3.html'
class Home4PageView(TemplateView):
    template_name = 'pages/index-4.html'
class HomePageView(TemplateView):
    template_name = 'pages/index.html'
class LoginPageView(TemplateView):
    template_name = 'pages/login.html'
class PortfolioDetailsPageView(TemplateView):
    template_name = 'pages/portfolio-details.html'
class PortfolioPageView(TemplateView):
    template_name = 'pages/portfolio.html'
class PricingPageView(TemplateView):
    template_name = 'pages/pricing.html'
class ResetPasswordPageView(TemplateView):
    template_name = 'pages/reset-password.html'
class ServiceDetailsPageView(TemplateView):
    template_name = 'pages/service-details.html'
class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'
class SignupPageView(TemplateView):
    template_name = 'pages/signup.html'
class TeamDetailsPageView(TemplateView):
    template_name = 'pages/team-details.html'
class TeamsPageView(TemplateView):
    template_name = 'pages/teams.html'
