# -*- coding: utf-8 -*-
from openerp import models, fields


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
    invtex_bank_id = fields.Many2one(
        "res.partner.bank",
        string="Bank account to show in Tex Invoice",
    )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
