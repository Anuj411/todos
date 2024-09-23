import logging
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()

logger = logging.getLogger('user_activity')

class UserActivityLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and not request.session.get('has_logged_in'):
            self.log_user_login(request)
            request.session['has_logged_in'] = True

    def process_response(self, request, response):
        if not request.user.is_authenticated and request.session.get('has_logged_in') is None:
            self.log_user_logout(request)
            request.session['has_logged_in'] = False
        return response

    def log_user_login(self, request):
        user = request.user
        if user.is_authenticated:
            logger.info(f'User {user.username} logged in at {now()} from IP: {self.get_client_ip(request)}')

    def log_user_logout(self, request):
        user = request.user
        print(f"==>> user: {user}")
        logger.info(f'User {user.username} logged out at {now()} from IP: {self.get_client_ip(request)}')

    def get_client_ip(self, request):
        """Utility to get the client's IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
