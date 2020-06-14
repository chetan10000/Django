from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.security.websocket import AllowedHostsOriginValidator
import resume
from django.urls import re_path
from resume import consumers
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
        URLRouter(
             [
                 re_path(r'messages/$',consumers.ChatConsumer),

                 ]
             )
        )
    )
})