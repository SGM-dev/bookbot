def get_num_words(str):
    return len(str.split())


def get_occurence_words(str):
    freq = {}

    for char in str.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1   \

    return freq


def get_sorted_list(dict):
    list = []

    for char in dict:
        list.append({
            "char": char,
            "num": dict[char]
        })

    def sort_on(dict):
        return dict["num"]

    list.sort(reverse=True, key=sort_on)
    return list
