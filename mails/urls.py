from django.conf.urls import patterns, url

from mails.views import MailsAPI

urlpatterns = patterns(
    '',
    url(r'^$', MailsAPI.as_view()),
)
