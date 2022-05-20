from django.urls import path
from . import views
urlpatterns = [
path('',views.home, name='home' ),
path('pshop/',views.pshop, name='pshop' ),
path('ishop/',views.ishop, name='ishop' ),
path('item/',views.item, name='item' ),
path('sign_in/',views.sign_in,name='sign_in'),
path('pshop/checkout/',views.pcheckout,name='pcheckout'),
path('pet/tracker/',views.tracker,name='tracker'),
path('pet/',views.pet,name='pet'),
path('aboutus/',views.aboutus,name='aboutus'),
path('contactus/',views.contactus,name='contactus'),
path('faq/',views.faq,name='faq'),
path('tq/',views.tq,name='tq'),
path('cart/',views.cart,name='cart'),
path('cartadd/<int:item_id>/',views.cartadd,name='cartadd'),
path('cartremove/<int:item_id>/',views.cartremove,name='cartremove'),
path('cart/checkout/',views.icheckout,name='icheckout'),
path('sign_up/',views.sign_up,name='sign_up'),
path('logout/',views.logout,name='logout')
]
