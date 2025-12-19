from agent.agent_loop import run_agent
from voice.stt import listen
from voice.tts import speak


def main():
    user_text = None

    while True:
        # Agent responds
        response = run_agent(user_text)

        print("AGENT:", response)
        speak(response)

        # Stop conditions
        if "ధన్యవాదాలు" in response or "క్షమించండి" in response:
            break

        # 🔑 ONLY listen if agent asked a question
        if "?" not in response and "ఏ పథకం" not in response:
            user_text = None
            continue

        user_text = listen()

        if not user_text or not user_text.strip():
            user_text = None
            continue

        print("USER:", user_text)


if __name__ == "__main__":
    main()
