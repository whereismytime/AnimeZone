from django.utils import timezone
from .time_class import get_main_time_class 

def add_filter_class_to_queryset(queryset):
    """
    Добавляет атрибут 'filter_class' к каждому объекту в QuerySet.
    Эта функция теперь находится в одном месте и может использоваться во всем проекте.
    """
    now = timezone.now()
    for item in queryset:
        if hasattr(item, 'created_at') and item.created_at:
            time_delta = now - item.created_at
            item.filter_class = get_main_time_class(time_delta)
        else:
            item.filter_class = ''
    return queryset