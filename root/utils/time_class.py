from datetime import timedelta

def get_main_time_class(delta):
    """
    Возвращает одну из строк:
      - 'day'   — до 1 дня
      - 'week'  — до 7 дней
      - 'month' — до 30 дней
      - 'years' — всё, что старше месяца
    """
    days = delta.days
    if days <= 1:
        return "day"
    elif days <= 7:
        return "week"
    elif days <= 30:
        return "month"
    return "years"
