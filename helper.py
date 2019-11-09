def itemIsNamed(item, name):
    return item.name == name

def itemHasNonZeroValue(item):
    return item.quality > 0

def isUnderHighestQualityValue(item):
    return item.quality < 50

def left10DaysBeforeDropdown(item):
    return item.sell_in < 11

def left5DaysBeforeDropdown(item):
    return item.sell_in < 6
