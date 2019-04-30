from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self , *args , **kwargs):
        return super().dispatch(*args , **kwargs)



class HttpResponseMixin(object):
    is_json=False
    content_type="text/html"
    def render_to_response(self, data , status=200):
        if self.is_json:
            content_type = "application/json"
        return HttpResponse(data  , content_type=content_type , status = status )
