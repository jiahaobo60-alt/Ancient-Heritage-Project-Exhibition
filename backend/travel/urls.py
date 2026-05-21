from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

from api import views

# 自定义Django Admin登录视图 - 登录成功后跳转到Vue后台
class CustomAdminLoginView(LoginView):
    template_name = 'admin/login.html'
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'http://localhost:9527/'
        return context
    
    def get_success_url(self):
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        return 'http://localhost:9527/'

# Admin站点配置
class AdminSite(admin.AdminSite):
    login_view = 'custom_admin_login'
    
admin_site = AdminSite()

router = routers.DefaultRouter()
router.register('api_info', views.scenery)

schema_view = get_schema_view(
    openapi.Info(
        title="个性化非遗文旅推荐系统",
        default_version='v1.0',
        description="测试工程接口文档",
        terms_of_service="https://cict.hnuahe.edu.cn/",
        contact=openapi.Contact(email="hanssong1019@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 自定义admin登录视图
    path('admin/login/', CustomAdminLoginView.as_view(), name='custom_admin_login'),
    path('admin/', admin.site.urls),
    # 配置django-rest-framwork API路由
    # path('', include('api.url')),
    path('api/', include('api.url')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # 古建筑主题API路由
    path('architecture/', include('api.urls_architecture')),

    # 配置drf-yasg路由
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# Serve frontend static files from /frontend/
urlpatterns += static('/frontend/', document_root=os.path.join(settings.BASE_DIR, '..', 'frontend'))

# Serve img files from /img/
urlpatterns += static('/img/', document_root=os.path.join(settings.BASE_DIR, '..', 'frontend', 'img'))

# Redirect root to frontend index.html
urlpatterns += [
    path('', RedirectView.as_view(url='/frontend/index.html', permanent=False)),
]
