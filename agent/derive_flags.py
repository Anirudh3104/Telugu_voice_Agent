def derive_flags(user_profile):
    occupation = user_profile.get("occupation")

    user_profile["farmer"] = occupation == "farmer"
    user_profile["student"] = occupation == "student"
    user_profile["self_employed"] = occupation == "self-employed"
    user_profile["employed"] = occupation == "employee"
    user_profile["unemployed"] = occupation == "unemployed"

    # Ask land ownership only if farmer
    if user_profile["farmer"]:
        land = input("మీరు భూమి యజమానులా? (yes / no) ")
        user_profile["land_owner"] = land.lower() == "yes"
    else:
        user_profile["land_owner"] = False

    # Ask pregnancy only if female
    if user_profile.get("gender") == "female":
        preg = input("మీరు ప్రస్తుతం గర్భిణీనా? (yes / no) ")
        user_profile["pregnant_woman"] = preg.lower() == "yes"
    else:
        user_profile["pregnant_woman"] = False

    return user_profile
