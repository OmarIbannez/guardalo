"""test_conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from bookmark import urls as bookmark_urls
from bookmark.views import SaveBookmark, Bookmark
from users.views import user_login, user_logout
from django.contrib.auth.decorators import login_required
from webapp.views import SettingsView, ImportBookmarks


urlpatterns = [
    url(r'^settings/$', login_required(SettingsView.as_view(), login_url='login'), name='settings'),
    url(r'^settings/import-bookmarks/$', login_required(ImportBookmarks.as_view(), login_url='login'), name='import-bookmarks'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include(bookmark_urls)),
    url(r'^$', login_required(Bookmark.as_view(), login_url='login'), name='mainpage'),
    url(r'^(?P<url>(.*))$', login_required(SaveBookmark.as_view(), login_url='login')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
