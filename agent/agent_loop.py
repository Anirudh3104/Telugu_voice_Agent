from typing import Dict, Any, Optional
from agent.derive_flags import derive_flags
from agent.eligibility import find_eligible_schemes
from data.scheme import schemes

# Conversation state
agent_state: Dict[str, Any] = {
    "current_state": "START",
    "user_profile": {},
    "current_question_index": 0,
    "eligible": []
}

eligibility_questions = [
    ("age", "మీ వయస్సు ఎంత?"),
    ("gender", "మీ లింగం ఏమిటి? (male / female)"),
    ("marital_status", "మీ వివాహ స్థితి ఏమిటి?"),
    ("occupation", "మీ వృత్తి ఏమిటి?"),
    ("income", "మీ వార్షిక ఆదాయం ఎంత?"),
    ("bpl", "మీరు BPL కుటుంబానికి చెందినవారా? (yes / no)")
]


def run_agent(user_text: Optional[str]) -> str:

    # START
    if agent_state["current_state"] == "START":
        agent_state["current_state"] = "ASK_ELIGIBILITY"
        agent_state["current_question_index"] = 0
        return "నమస్కారం! ప్రభుత్వ పథకాల సహాయకుడికి స్వాగతం. మొదట కొన్ని ప్రశ్నలు అడుగుతాను."

    # ASK ELIGIBILITY
    if agent_state["current_state"] == "ASK_ELIGIBILITY":
        idx = agent_state["current_question_index"]

        # Save previous answer
        if user_text is not None and idx > 0:
            field, _ = eligibility_questions[idx - 1]
            try:
                answer = user_text.strip().lower()

                if answer in ["yes", "no"]:
                    value = answer == "yes"
                elif field in ["age", "income"]:
                    value = int(answer)
                else:
                    value = answer

                agent_state["user_profile"][field] = value

            except:
                agent_state["current_question_index"] -= 1
                return "❌ సరైన సమాచారం ఇవ్వలేదు. దయచేసి మళ్లీ చెప్పండి."

        # Ask next question
        if idx < len(eligibility_questions):
            question = eligibility_questions[idx][1]
            agent_state["current_question_index"] += 1
            return question

        agent_state["current_state"] = "CHECK_ELIGIBILITY"

    # CHECK ELIGIBILITY
    if agent_state["current_state"] == "CHECK_ELIGIBILITY":
        agent_state["user_profile"] = derive_flags(agent_state["user_profile"])
        eligible = find_eligible_schemes(agent_state["user_profile"], schemes)

        if not eligible:
            agent_state["current_state"] = "END"
            return "క్షమించండి. మీకు అర్హత ఉన్న పథకాలు లేవు."

        agent_state["eligible"] = eligible
        agent_state["current_state"] = "SHOW_SCHEMES"

        scheme_list = "\n".join(
            f"{i+1}. {s['scheme_name']}" for i, s in enumerate(eligible)
        )
        return f"మీకు అర్హత ఉన్న పథకాలు ఇవి:\n{scheme_list}\nఏ పథకం వివరాలు కావాలి?"

    # SHOW SCHEMES
    if agent_state["current_state"] == "SHOW_SCHEMES":
        if user_text is None:
            return "ఏ పథకం వివరాలు కావాలి?"

        spoken = user_text.strip().lower().replace(" ", "")

        for scheme in agent_state["eligible"]:
            name = scheme["scheme_name"].lower().replace(" ", "")
            if name in spoken:
                agent_state["current_state"] = "END"
                return (
                    f"{scheme['scheme_name']} గురించి వివరాలు:\n"
                    f"{scheme['benefits']}"
                )

        return "క్షమించండి. దయచేసి పథకం పేరు స్పష్టంగా చెప్పండి."

    # END
    return "ధన్యవాదాలు!"
