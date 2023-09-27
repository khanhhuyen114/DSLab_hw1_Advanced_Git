from collections import defaultdict
def get_path1(path):
    # Create a defaultdict to group elements by their first element
    grouped = defaultdict(list)
    for element in path:
        grouped[element[0]].append(element)

    # Find the element e with the maximum second element for each group
    result = [max(group, key=lambda x: x[1]) for group in grouped.values()]

    return result
