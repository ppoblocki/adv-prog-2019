def item_is_named(item, name):
    return item.name == name

def item_has_non_zero_value(item):
    return item.quality > 0

def is_under_highest_quality_value(item):
    return item.quality < 50

def left_10_days_before_dropdown(item):
    return item.sell_in < 11

def left_5_days_before_dropdown(item):
    return item.sell_in < 6
