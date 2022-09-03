from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

from online_store.products.models import Product, Order


@dataclass
class ReportEntry:
    # month: int
    value: Decimal


@dataclass
class ReportParams:
    start_date: date
    end_date: date
    metric: str


def monthly_report(params: ReportParams):
    data = []

    if params.metric == 'price':
        queryset = Product.objects.filter(
            orders__date__gte=params.start_date,
            orders__date__lte=params.end_date,
        ).values('orders__products').annotate(
            value=Sum('price'),

        )

        for entry in queryset:
            report_entry = ReportEntry(
                # entry['month'],
                entry['value'],
            )

            data.append(report_entry)

    elif params.metric == 'count':
        queryset = Product.objects.filter(
            orders__date__gte=params.start_date,
            orders__date__lte=params.end_date,
        ).values('orders__products').annotate(
            value=Count('id')
        )

        for entry in queryset:
            report_entry = ReportEntry(
                # entry['month'],
                entry['value'],
            )
            data.append(report_entry)

    return data
