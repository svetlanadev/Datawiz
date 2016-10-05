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
        # Getting turnover
        turnover1_get = settings.DW.get_categories_sale(categories=category_get,
                                                by='turnover',
                                                date_from=datetime.date(2015, 11, 18),
                                                date_to=datetime.date(2015, 11, 18)
                                                )
        turnover1 = turnover1_get.ix['2015-11-18', 'turnover']
        turnover2_get = settings.DW.get_categories_sale(categories=category_get,
                                                        by='turnover',
                                                        date_from=datetime.date(2015, 11, 17),
                                                        date_to=datetime.date(2015, 11, 17)
                                                        )
        turnover2 = turnover2_get.ix['2015-11-17', 'turnover']
        rate_diff = ((turnover2 - turnover1) / turnover1) * 100
        rate_diff_turnover = round(rate_diff, 2)
        diff = turnover2 - turnover1
        diff_turnover = round(diff, 2)

        # Getting qty
        qty1_get = settings.DW.get_categories_sale(categories=category_get,
                                              by='qty',
                                              date_from=datetime.date(2015, 11, 18),
                                              date_to=datetime.date(2015, 11, 18),
                                              )
        qty1 = qty1_get.ix['2015-11-18', 'qty']
        qty2_get = settings.DW.get_categories_sale(categories=category_get,
                                              by='qty',
                                              date_from=datetime.date(2015,11, 17),
                                              date_to=datetime.date(2015, 11, 17)
                                               )
        qty2 = qty2_get.ix['2015-11-17', 'qty']
        rate_diff = ((qty2 - qty1) / qty1) * 100
        rate_diff_qty = round(rate_diff, 2)
        diff = qty2 - qty1
        diff_qty = round(diff, 2)

        # Getting receipts_qty
        receipts_qty1_get = settings.DW.get_categories_sale(categories=category_get,
                                              by='receipts_qty',
                                              date_from=datetime.date(2015, 11, 18),
                                              date_to=datetime.date(2015, 11, 18),
                                              )
        receipts_qty1 = receipts_qty1_get.ix['2015-11-18', 'receipts_qty']
        receipts_qty2_get = settings.DW.get_categories_sale(categories=category_get,
                                              by='receipts_qty',
                                              date_from=datetime.date(2015,11, 17),
                                              date_to=datetime.date(2015, 11, 17)
                                               )
        receipts_qty2 = receipts_qty2_get.ix['2015-11-17', 'receipts_qty']
        rate_diff = ((receipts_qty2 - receipts_qty1) / receipts_qty1) * 100
        rate_diff_receipts_qty = round(rate_diff, 2)
        diff = receipts_qty2 - receipts_qty1
        diff_receipts_qty = round(diff, 2)

        # Getting avg_receipts
        avg_receipt1_get = settings.DW.get_categories_sale(categories=category_get,
                                                        by='avg_receipt',
                                                        date_from=datetime.date(2015, 11, 18),
                                                        date_to=datetime.date(2015, 11, 18)
                                                        )
        avg_receipt1 = avg_receipt1_get.ix['2015-11-18', 'avg_receipt']
        avg_receipt2_get = settings.DW.get_categories_sale(categories=category_get,
                                                        by='avg_receipt',
                                                        date_from=datetime.date(2015, 11, 17),
                                                        date_to=datetime.date(2015, 11, 17)
                                                        )
        avg_receipt2 = avg_receipt2_get.ix['2015-11-17', 'avg_receipt']
        rate_diff = ((avg_receipt2 - avg_receipt1) / avg_receipt1) * 100
        rate_diff_avg_receipt = round(rate_diff, 2)
        diff = avg_receipt2 - avg_receipt1
        diff_avg_receipt = round(diff, 2)
        return render(request, 'index.html', {'client': client, 'turnover1': turnover1, 'turnover2': turnover2, 'rate_diff_turnover': rate_diff_turnover, 'diff_turnover': diff_turnover, 'qty1': qty1, 'qty2': qty2, 'rate_diff_qty': rate_diff_qty, 'diff_qty': diff_qty,
                                              'receipts_qty1': receipts_qty1, 'receipts_qty2': receipts_qty2, 'rate_diff_receipts_qty': rate_diff_receipts_qty, 'diff_receipts_qty': diff_receipts_qty,
                                              'avg_receipt1': avg_receipt1, 'avg_receipt2': avg_receipt2, 'rate_diff_avg_receipt': rate_diff_avg_receipt, 'diff_avg_receipt': diff_avg_receipt })

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

# var = settings.DW.get_categories_sale(categories=category_get,
#                                                 by='avg_receipt',
#                                                 date_from=datetime.date(2015, 11, 18),
#                                                 date_to=datetime.date(2015, 11, 18)
#                                                 )
