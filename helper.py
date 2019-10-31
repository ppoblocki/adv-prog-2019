def itemIsNamed(item, name):
    return item.name == name

def itemHasNonZeroValue(item):
    return item.quality > 0

def isUnderHighestQualityValue(item):
    return item.quality < 50
