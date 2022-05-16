from django.contrib import admin
from django.urls import path, include
from transactions import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Plerk Challange",
      default_version='v1',
      description="Plerk Challange for BackEnd Developer",
      terms_of_service="https://www.notion.so/Django-Backend-Entrevista-9e048362475f45eaaad990f9837e146e",
      contact=openapi.Contact(email="ozk404@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("company/<uuid:company_id>/", views.CompanyService.as_view(), name="Company Service"),
    path("summary/", views.SummaryService.as_view(), name="Summary"),
    path("top/", views.TopCompanies.as_view(), name="TOP"),
    path("top/<int:top_entries>/", views.TopCompanies.as_view(), name="TOP Entries"),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name = 'Swagger')

]
