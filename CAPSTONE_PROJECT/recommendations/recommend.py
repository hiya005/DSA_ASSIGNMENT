def recommend_users(profile_manager, graph, user_id):
    user = profile_manager.get_profile(user_id)
    if not user:
        return []

    scores = {}

    for other_id, other in profile_manager.users.items():
        if other_id == user_id or other_id in graph.get(user_id, []):
            continue

        common = len(user["interests"] & other["interests"])
        if common > 0:
            scores[other_id] = common

    # sort by common interests
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)