from http import HTTPStatus

from flask_restplus import Resource

from app.auth import views
from app.auth.namespaces import AuthNamespace
from app.namespaces import ErrorNs


@AuthNamespace.ns.route('/login')
class LogIn(Resource):
    @AuthNamespace.ns.expect(AuthNamespace.login_model)
    @AuthNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase)
    @AuthNamespace.ns.response(HTTPStatus.UNAUTHORIZED, HTTPStatus.UNAUTHORIZED.phrase,
                               model=ErrorNs.error_model)
    def post(self):
        """Log in"""

        views.login(AuthNamespace.ns.payload)

        return {}, HTTPStatus.CREATED


@AuthNamespace.ns.route('/logout')
class LogOut(Resource):
    @AuthNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase)
    @AuthNamespace.ns.response(HTTPStatus.UNAUTHORIZED, HTTPStatus.UNAUTHORIZED.phrase,
                               model=ErrorNs.error_model)
    def post(self):
        """Log out"""

        views.logout()

        return {}, HTTPStatus.CREATED
