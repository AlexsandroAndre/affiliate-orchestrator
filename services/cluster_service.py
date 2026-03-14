def build_clusters(keywords):

    clusters = {}

    for kw in keywords:

        root = kw.split()[0]

        clusters.setdefault(root, []).append(kw)

    return clusters
