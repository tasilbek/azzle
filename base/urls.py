from django.urls import path
from .views import *

urlpatterns = [
    path('about', AboutPageView.as_view(), name='about'),
    path('blog-details', BlogDetailsPageView.as_view(), name='blog-details'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('error-404', Error404PageView.as_view(), name='error-404'),
    path('faq-2', Faq2PageView.as_view(), name='faq-2'),
    path('faq', FaqPageView.as_view(), name='faq'),
    path('home-2', Home2PageView.as_view(), name='home-2'),
    path('home-3', Home3PageView.as_view(), name='home-3'),
    path('home-4', Home4PageView.as_view(), name='home-4'),
    path('', HomePageView.as_view(), name='home'),
    path('login', LoginPageView.as_view(), name='login'),
    path('portfolio-details', PortfolioDetailsPageView.as_view(), name='portfolio-details'),
    path('portfolio', PortfolioPageView.as_view(), name='portfolio'),
    path('pricing', PricingPageView.as_view(), name='pricing'),
    path('reset-password', ResetPasswordPageView.as_view(), name='reset-password'),
    path('service-details', ServiceDetailsPageView.as_view(), name='service-details'),
    path('services', ServicesPageView.as_view(), name='services'),
    path('signup', SignupPageView.as_view(), name='signup'),
    path('team-details', TeamDetailsPageView.as_view(), name='team-details'),
    path('teams', TeamsPageView.as_view(), name='teams')
] 
