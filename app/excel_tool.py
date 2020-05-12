import io

import xlsxwriter
import datetime

from django.views import View

from app.model import Main


def excel_2(context):
    print('context is', context)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.merge_range(0, 0, 0, 4, 'Организация:', context)


    workbook.close()

    output.seek(0)
    return output