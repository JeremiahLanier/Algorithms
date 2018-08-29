def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    j_1 = start_1
    j_2 = start_2
    j_t = 0

    while j_1 < end_1 or j_2 < end_2:
        if j_1 < end_1 and j_2 < end_2:
            if items[j_1] < items[j_2]:
                temporary_storage[j_t] = items[j_1]
                j_1 += 1
            else:
                temporary_storage[j_t] = items[j_2]
                j_2 += 1
            j_t += 1
        elif j_1 < end_1:
            for j in range(j_1, end_1):
                temporary_storage[j_t] = items[j_1]
                j_1 += 1
                j_t += 1
        else:
            for j in range(j_2, end_2):
                temporary_storage[j_t] = items[j_2]
                j_2 += 1
                j_t += 1

    for j in range(j_t):
        items[start_1 + j] = temporary_storage[j]


def merge_sort(items):
    l = len(items)
    temporary_storage = [None] * l
    size_of_subsections = 1

    while size_of_subsections < l:
        for j in range(0, l, size_of_subsections * 2):
            j1_start, jl_end = j, min(j + size_of_subsections, l)
            j2_start, j2_end = jl_end, min(jl_end + size_of_subsections, l)
            sections = (j1_start, jl_end), (j2_start, j2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    return items
