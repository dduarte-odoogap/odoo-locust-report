from odoo.http import request
from odoo.addons.web.controllers.main import DataSet


class ReportDataset(DataSet):
    def _call_kw(self, model, method, args, kwargs):
        rpc_request = [
            request.env[model]._name,
            method,
            str(request.env[model].search.__code__.co_varnames),
            str(args),
            str(kwargs),
        ]
        file_path = request.env['ir.config_parameter'].get_param("report_locust.filepath")
        status = request.env['ir.config_parameter'].get_param("report_locust.status")

        if file_path and status == 'run':
            with open(file_path+'lc_report.txt', 'a+') as f:
                f.write('\n%s' % ','.join(rpc_request))
                f.close()

        return super(ReportDataset, self)._call_kw(model, method, args, kwargs)