# -*- coding: utf-8 -*-

import json

from restless.views import Endpoint
from restless.auth import BasicHttpAuthMixin, login_required
from django.template import Context as C
from django.template import Template as T

from mails.models import Application, Log, Template
from mails.mailserver import MailServer


def message(status, content):
    return {"status": status, "content": content}


class MailsAPI(Endpoint, BasicHttpAuthMixin):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
        except ValueError, e:
            return message(False, unicode(e))

        app_label = data.get("app")
        applications = Application.objects.filter(name=app_label)
        if not applications:
            return message(False, "Application not found.")
        application = applications[0]

        template_label = data.get("template")
        templates = Template.objects.filter(name=template_label)
        if not templates:
            return message(False, "Template not found.")
        template = templates[0]

        sender = application.default_sender
        receiver = data.get("receiver")
        context = data.get("context")
        subject = template.subject
        content = T(template.content).render(C(context))

        server = MailServer(
            application.host,
            application.port,
            application.username,
            application.password,
            application.use_ssl)

        server.sendmail(sender, receiver, subject, content)

        Log.objects.create(
            application=application,
            sender=sender,
            receiver=receiver,
            subject=subject,
            content=content)
        return message(True, "Messsage sent.")
