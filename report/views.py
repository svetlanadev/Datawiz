from django.shortcuts import render
from django.conf import settings
import datetime


# def index(request):
#             result = settings.DW.get_products_sale(products = [2833024, 2286946, 'sum'],by='turnover',
#                               shops = [305, 306, 318, 321],
#                               date_from = datetime.date(2015, 8, 9),
#                               date_to = datetime.date(2015, 9, 9),
#                               interval = datawiz.WEEKS)
#             return render(request, 'index.html', {'result' : result.to_html()})


def index(request):
        client = settings.DW.get_client_info()
        product = settings.DW.get_product()
        result = settings.DW.get_products_sale(by='turnover',
                                               date_from=datetime.date(2015, 8, 9),
                                               date_to=datetime.date(2015, 8, 9),
                                               )
        return render(request, 'index.html', {'client': client, 'product': product, 'result' : result.to_html()})



# def index(request):
#         result = settings.DW.get_products_sale(by='turnover',
#                               date_from = datetime.date(2015, 8, 9),
#                               date_to = datetime.date(2015, 8, 9),
#                               )
#         return render(request, 'index.html', {'result' : result.to_html()})

# def f(x):
#     return x[0] + x[1]
# test_apply = df.apply(f, axis=1)


def report(request):
        return render(request, 'report.html')