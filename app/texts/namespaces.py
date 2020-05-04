""""""

from flask_restplus import Namespace, fields, reqparse


class TextNamespace:
    """"""

    ns = Namespace('texts')

    # Models
    get_text_model = ns.model('GetTextModel',
                              {'id': fields.Integer(),
                               'text': fields.String(),
                               'tags': fields.String(),
                               'creationDateTime': fields.DateTime(attribute='creation_dt'),
                               'lastUpdateDateTime': fields.DateTime(attribute='last_update_dt')
                               })

    get_text_all_model = ns.model('GetTextAllModel',
                                  {'texts': fields.List(fields.Nested(get_text_model))})

    post_expect_model = ns.model('PostExpectModel',
                                 {'text': fields.String(required=True)})

    post_response_model = ns.model('PostResponseModel',
                                   {'id': fields.Integer()})

    patch_expect_model = ns.model('PatchExpectModel',
                                  {'text': fields.String()})

    # Parsers
    texts_parser = reqparse.RequestParser()
    texts_parser.add_argument('creationDateFrom', type=str)
    texts_parser.add_argument('creationDateTo', type=str)
    texts_parser.add_argument('lastUpdateDateFrom', type=str)
    texts_parser.add_argument('lastUpdateDateTo', type=str)
