def build_clusters(keywords):

    clusters = {}

    for kw in keywords:

        words = kw.split()

        if len(words) >= 2:
            root = " ".join(words[:2])
        else:
            root = kw

        clusters.setdefault(root, []).append(kw)

    return clusters
