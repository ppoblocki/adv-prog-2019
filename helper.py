'''helper.py'''

def item_is_named(item, name):
    '''Checks item's name.'''
    return item.name == name

def item_has_non_zero_value(item):
    '''Check if item's quality is above 0.'''
    return item.quality > 0

def is_under_highest_quality_value(item):
    '''Checks if item's quality is below 50.'''
    return item.quality < 50

def left_10_days_before_dropdown(item):
    '''Checks if item's sell_in attribute is below 11.'''
    return item.sell_in < 11

def left_5_days_before_dropdown(item):
    '''Checks if item's sell_in attribute is below 6.'''
    return item.sell_in < 6
