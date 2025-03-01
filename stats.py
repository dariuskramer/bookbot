def count_words(content):
    return len(content.split())

def count_unique_chars(content):
    unique_chars = {}
    for char in content.lower():
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def sort_chars(unique_chars):
    sorted_list = []

    # {'character': 'a', 'count': 1}
    for k, v in unique_chars.items():
        sorted_list.append({'character': k, 'count': v})

    sorted_list.sort(reverse=True, key=lambda d: d['count'])
    return sorted_list


