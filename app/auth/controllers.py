from http import HTTPStatus

from flask_restplus import Resource

from app.auth import views
from app.auth.namespaces import UserNamespace
from app.namespaces import ErrorNs


@UserNamespace.ns.route('/login')
class LogIn(Resource):
    @UserNamespace.ns.expect(UserNamespace.login_model)
    @UserNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase)
    @UserNamespace.ns.response(HTTPStatus.UNAUTHORIZED, HTTPStatus.UNAUTHORIZED.phrase,
                               model=ErrorNs.error_model)
    def post(self):
        """Log in"""

        views.login(UserNamespace.ns.payload)

        return {}, HTTPStatus.CREATED


@UserNamespace.ns.route('/logout')
class LogOut(Resource):
    @UserNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase)
    @UserNamespace.ns.response(HTTPStatus.UNAUTHORIZED, HTTPStatus.UNAUTHORIZED.phrase,
                               model=ErrorNs.error_model)
    def post(self):
        """Log out"""

        views.logout()

        return {}, HTTPStatus.CREATED


@UserNamespace.ns.route('/registration')
class Register(Resource):
    @UserNamespace.ns.expect(UserNamespace.registration_model)
    @UserNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase)
    @UserNamespace.ns.response(HTTPStatus.UNAUTHORIZED, HTTPStatus.UNAUTHORIZED.phrase,
                               model=ErrorNs.error_model)
    @UserNamespace.ns.response(HTTPStatus.CONFLICT, HTTPStatus.CONFLICT.phrase,
                               model=ErrorNs.error_model)
    def post(self):
        """Registration"""

        views.registration(UserNamespace.ns.payload)

        return {}, HTTPStatus.CREATED
