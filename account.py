# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime, timedelta
import time
from openerp import SUPERUSER_ID

class account_voucher(osv.osv):
    _name = 'account.voucher'
    _inherit ='account.voucher'
    _columns = {
        }

    _defaults = {
        }

    def print_jasper_voucher(self, cr, uid, ids, context=None):
        self_br = self.browse(cr, uid, ids[0], context=None)
        if self_br.type == 'receipt':
            value = {
                'type': 'ir.actions.report.xml',
                'report_name': 'Comprobante.Ingresos',
                'datas': {
                            'model' : 'account.voucher',
                            'ids'   : ids,
                            }
                        }
        else:
            value = {
                'type': 'ir.actions.report.xml',
                'report_name': 'Comprobante.Egresos',
                'datas': {
                            'model' : 'account.voucher',
                            'ids'   : ids,
                            }
                        }
        return value

