from django import template

register = template.Library()

@register.filter
def short_number(value):
    try:
        value = int(value)

        if value < 100:
            return str(value)

        if 100 <= value < 1000:
            return f'{value}'

        if 1_000 <= value < 1_500:
            return '~1k'

        if 1_500 <= value < 10_000:
            return f'{value // 1_000}.{(value % 1_000) // 100}k'

        if 10_000 <= value < 1_000_000:
            return f'{value // 1_000}k'

        if 1_000_000 <= value < 1_000_000_000:
            emoji = ' 🔥' if value >= 10_000_000 else ''
            return f'{value / 1_000_000:.1f}M{emoji}'.rstrip('0').rstrip('.')

        if value >= 1_000_000_000:
            return f'{value / 1_000_000_000:.1f}B 🧠'.rstrip('0').rstrip('.')

        return str(value)

    except (ValueError, TypeError):
        return value
