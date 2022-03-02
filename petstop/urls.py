from django.urls import path
from . import views
urlpatterns = [
path('',views.home, name='home' ),
path('pshop/',views.pshop, name='pshop' ),
path('ishop/',views.ishop, name='ishop' ),
path('item/',views.item, name='item' ),
path('sign_in/',views.sign_in,name='sign_in'),
path('pshop/checkout/',views.pcheckout,name='pcheckout'),
path('ishop/checkout/',views.icheckout,name='icheckout'),
path('sign_up/',views.sign_up,name='sign_up'),
path('logout/',views.logout,name='logout')
]
