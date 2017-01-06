

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    return content[:length + 1] + suffix
