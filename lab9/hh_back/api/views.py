from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Company, Vacancy
# from .serializers import CompanySerializer, VacancySerializer


# @api_view(['GET', 'POST'])
# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def company_detail(request, id):
#     try:
#         company = Company.objects.get(id=id)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
#     except Company.DoesNotExist:
#         return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def company_vacancies(request, id):
#     try:
#         vacancies = Vacancy.objects.filter(company_id=id)
#         serializer = VacancySerializer(vacancies, many=True)
#         return Response(serializer.data)
#     except Vacancy.DoesNotExist:
#         return Response({"error": "Vacancies not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def vacancy_list(request):
#     vacancies = Vacancy.objects.all()
#     serializer = VacancySerializer(vacancies, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def vacancy_detail(request, id):
#     try:
#         vacancy = Vacancy.objects.get(id=id)
#         serializer = VacancySerializer(vacancy)
#         return Response(serializer.data)
#     except Vacancy.DoesNotExist:
#         return Response({"error": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def top_ten_vacancies(request):
#     vacancies = Vacancy.objects.order_by('-salary')[:10]
#     serializer = VacancySerializer(vacancies, many=True)
#     return Response(serializer.data)

from rest_framework import generics
from rest_framework.response import Response
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
from rest_framework.views import APIView

# List all companies
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# Get a single company by id
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# List vacancies by company id
class CompanyVacancyListView(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)

# List all vacancies
class VacancyListView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

# Get a single vacancy by id
class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

# List top 10 vacancies sorted by salary
class TopTenVacanciesView(APIView):
    def get(self, request):
        top_vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return Response(serializer.data)


