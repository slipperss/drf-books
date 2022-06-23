from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter
from store.views import BookViewSet, auth, UserBooksRelationView

router = SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'book_relation', UserBooksRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    #path('__debug__/', include('debug_toolbar.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
urlpatterns += router.urls