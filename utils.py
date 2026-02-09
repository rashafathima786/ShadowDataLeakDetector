def calculate_behavior_score(
    password_reuse,
    public_wifi_usage,
    email_used_everywhere,
    password_change_frequency,
    platform_count
):
    """
    Calculates behavioral risk score based on user habits.
    Score range: 0 to 100
    """

    score = 0

    if password_reuse == 1:
        score += 25

    score += public_wifi_usage * 7

    if email_used_everywhere == 1:
        score += 20

    score += (3 - password_change_frequency) * 8

    if platform_count > 15:
        score += 20
    elif platform_count > 8:
        score += 10

    return min(score, 100)
