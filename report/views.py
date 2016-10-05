from django.shortcuts import render
from django.conf import settings
import datetime
import pandas as pd

def index(request):
        #getting info about client
        client = settings.DW.get_client_info()
        #getting info about main category
        category_get = [cat['category_id'] for cat in settings.DW.get_category().get('results')]
        print category_get
        turnover1_get = settings.DW.get_categories_sale(categories=category_get,
                                                by='turnover',
                                                date_from=datetime.date(2015, 11, 17),
                                                date_to=datetime.date(2015, 11, 17)
                                                )
        turnover1 = turnover1_get.ix['2015-11-17', 'turnover']

        turnover2_get = settings.DW.get_categories_sale(categories=category_get,
                                                        by='turnover',
                                                        date_from=datetime.date(2015, 11, 18),
                                                        date_to=datetime.date(2015, 11, 18)
                                                        )
        turnover2 = turnover2_get.ix['2015-11-18', 'turnover']

        rate_diff_d = ((turnover2 - turnover1) / turnover1) * 100
        rate_diff = round(rate_diff_d, 2)
        diff_d = turnover2 - turnover1
        diff = round(diff_d, 2)

        return render(request, 'index.html', {'client': client, 'turnover1': turnover1, 'turnover2': turnover2, 'rate_diff': rate_diff, 'diff': diff })

def report(request):
    return render(request, 'report.html')


# # # [x.room_number() for x in people if check(x)]
# products = [p['product_id'] for p in settings.DW.get_product().get('results', [])]
# # product = settings.DW.get_product(products=['2894313', '2894313'])
# # print  '>>>>>>>>>>>>>',  products
# products.append('sum')
# # print products
# turnover1_get = settings.DW.get_products_sale(products=products,
#                                               by='turnover',
#                                               date_from=datetime.date(2015, 8, 9),
#                                               date_to=datetime.date(2015, 8, 9),
#                                               )
# turnover1 = turnover1_get.ix['2015-08-09', 'sum']
# turnover2_get = settings.DW.get_products_sale(products=products,
#                                               by='turnover',
#                                               date_from=datetime.date(2015, 11, 17),
#                                               date_to=datetime.date(2015, 11, 17),
#                                               )
# turnover2 = turnover2_get.ix['2015-11-17', 'sum']
#
# rate_diff_d = ((turnover2 - turnover1) / turnover1) * 100
# rate_diff = round(rate_diff_d, 2)
# diff_d = turnover2 - turnover1
# diff = round(diff_d, 2)
# return render(request, 'index.html', {'client': client, 'turnover1': turnover1, 'turnover2': turnover2, 'rate_diff': rate_diff,
#                    'diff': diff, 'p_cat': p_cat})


    # categories_get = settings.DW.get_category()
# # categories_get = settings.DW.get_category().get('results')[0].get('category_id')