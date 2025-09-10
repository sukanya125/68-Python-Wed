
def analyze_user_activity(log_file_path: str) -> dict:
    unique_users = set()
    action_counts = Counter()
    user_action_counts = defaultdict(int)

    login_durations_sum = 0.0
    login_count = 0

    try:
        with open(log_file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 4:
                    continue  

                _, user_id, action, duration_str = parts
                try:
                    duration = float(duration_str)
                except ValueError:
                    continue  

                unique_users.add(user_id)

                action_counts[action] += 1
                user_action_counts[user_id] += 1

                if action.lower() == "login":
                    login_durations_sum += duration
                    login_count += 1
    except FileNotFoundError:
        return {
            "total_users": 0,
            "action_counts": {},
            "most_active_user": None,
            "average_session_time": 0.0,
        }
    most_active_user: Optional[str] = None
    if user_action_counts:
        most_active_user = max(user_action_counts.items(), key=lambda kv: kv[1])[0]

    average_session_time = (login_durations_sum / login_count) if login_count else 0.0

    return {
        "total_users": len(unique_users),
        "action_counts": dict(action_counts),
        "most_active_user": most_active_user,
        "average_session_time": float(average_session_time),
    }



if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
