import imp
from django.conf.urls import url
from django.contrib import admin
from my_api import test_1, test_2, test_3, test_4
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home_send_email/', test_2.home_send_email),
    url(r'^send_email/', test_2.send_mail),
    url(r'^find_index/', test_3.find_index_of_max),
    url(r'^home_factorial', test_4.home_factorial),
    url(r'^factorial/', test_4.calculate_factorial),
    url(r'^add_todo_list/', test_1.taskAdd),
    url(r'^create_todo_list/', test_1.taskCreate),
    url(r'^get_todo_list/', test_1.get_todo_list),
    url(r'^complete/', test_1.complete_todo),
    url(r'^delete/', test_1.delete_todo),
    

]
