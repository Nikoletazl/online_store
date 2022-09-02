from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from django.db.models import Sum, Count

from online_store.products.models import Product


@dataclass
class ReportEntry:
    value: Decimal
    count: int


@dataclass
class ReportParams:
    start_date: date
    end_date: date


def monthly_report(params: ReportParams):
    data = []

    queryset = Product.objects.filter(
        orders__date__gte=params.start_date,
        orders__date__lte=params.end_date,
    ).values('orders__products').annotate(
        value=Sum('price'),
        count=Count('id')
    )

    for entry in queryset:
        report_entry = ReportEntry(
            # month,
            entry['value'],
            entry['count']
        )

        data.append(report_entry)

    return data