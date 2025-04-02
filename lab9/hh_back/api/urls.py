# from django.urls import path
# from .views import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail, top_ten_vacancies

# urlpatterns = [
#     path('companies/', company_list),
#     path('companies/<int:id>/', company_detail),
#     path('companies/<int:id>/vacancies/', company_vacancies),
#     path('vacancies/', vacancy_list),
#     path('vacancies/<int:id>/', vacancy_detail),
#     path('vacancies/top_ten/', top_ten_vacancies),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<int:id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<int:id>/vacancies/', views.CompanyVacancyListView.as_view(), name='company_vacancies'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:id>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/top_ten/', views.TopTenVacanciesView.as_view(), name='top_ten_vacancies'),
]





