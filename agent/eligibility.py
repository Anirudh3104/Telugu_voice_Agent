def is_eligible(user, scheme):
    rules = scheme.get("eligibility", {})

    for key, value in rules.items():
        if key == "min_age" and user.get("age", 0) < value:
            return False
        if key == "max_age" and user.get("age", 100) > value:
            return False
        if key == "max_income" and user.get("income", 0) > value:
            return False
        if key in user and user.get(key) != value:
            return False

    return True


def find_eligible_schemes(user, schemes):
    return [s for s in schemes if is_eligible(user, s)]
