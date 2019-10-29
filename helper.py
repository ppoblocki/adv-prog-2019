def itemIsNamed(item, name):
    if item.name == name:
        return True
    else:
        return False

def itemHasValue(item):
    if item.quality > 0:
        return True
    else:
        return False