# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

{
    'name': 'Comprobante de Ingresos / Recibo de Caja',
    'version': '1',
    "author" : "German Ponce Dominguez",
    "category" : "Almacen",
    'description': """

Este modulo añade un reporte para la Impresion de Pagos:
    - Cliente.
    - Proveedor.

    """,
    "website" : "http://integra.avalos.co",
    "license" : "AGPL-3",
    "depends" : ["account","account_voucher","jasper_reports"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "report.xml",
                    ],
    "installable" : True,
    "active" : False,
}
