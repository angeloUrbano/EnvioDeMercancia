class AjaxMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.ajax_request = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        response = self.get_response(request)
        return response