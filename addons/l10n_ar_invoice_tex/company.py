# -*- coding: utf-8 -*-
from openerp import models, fields, api


class company(models.Model):
    _inherit = "res.company"

    invtex_show_bonif = fields.Boolean(
        string="Show bonification in Tex Invoice",
        default=True
    )
    invtex_lines_size = fields.Selection(
        selection=[('small', 'Small'),
                   ('normal', 'Normal'),
                   ('big', 'Big')],
        string="Line sizes in Tex Invoice",
        default='normal'
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
