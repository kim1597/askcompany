from django.contrib import admin
from django.urls import path
from blog.views import hello_times
from blog.views import index, hello_times
from blog.views import articles_by_year
from blog.views import naver_realtime_keywords
from blog.views import naver_blog_search
from blog.views import 사원증_이미지_응답

from django.urls import register_converter
from blog.converters import FourDigitYearConverter

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/', inclulde('blog.urls'))
        path('naver/실시간검색어/', naver_realtime_keywords),
	    path('naver/네이버블로그검색/', naver_blog_search),
]