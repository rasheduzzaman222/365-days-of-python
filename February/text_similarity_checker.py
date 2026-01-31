def jaccard_similarity(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())

    intersection = set1 & set2
    union = set1 | set2

    return len(intersection) / len(union) if union else 0


if __name__ == "__main__":
    t1 = "python makes coding fun"
    t2 = "coding in python is fun"
    print(jaccard_similarity(t1, t2))
