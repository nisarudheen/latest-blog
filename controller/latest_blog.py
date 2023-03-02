import itertools
import operator
from odoo.addons.http_routing.models.ir_http import slug
from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(['/latest_blog'], type="json", auth="public")
    def sold_total(self):
        blogs = []
        for i in request.env['blog.post'].sudo().search([]):
            blogs.append([
                i.name,i.id,slug(i.blog_id)
            ])
        list = blogs[0:4]
        return list