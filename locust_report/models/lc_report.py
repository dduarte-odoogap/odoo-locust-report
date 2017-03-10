from odoo import http, models, fields, api


class LCReport(models.Model):
    _name = 'report.locust'

    @api.multi
    def lc_switch_report(self):
        status = self.env['ir.config_parameter'].get_param("report_locust.status")

        if status != 'run':
            status.write({'value': 'run'})
        else:
            status.write({'value': 'stop'})
