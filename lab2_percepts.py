from lab2_model import HVACController

def run_trace():
    controller = HVACController()
    tests = [
        ("repeated cold percept 1", 17.0, True),
        ("repeated cold percept 2", 17.0, True),
        ("lower exact boundary", 18.0, True),
        ("upper exact boundary", 26.0, True),
        ("mode transition", 27.0, True),
        ("empty room", 30.0, False),
    ]

    print("CASE | PREVIOUS MODE | PERCEPT | TARGET | OUTCOME")
    for label, temperature, occupied in tests:
        target, should_send, previous = controller.update(temperature, occupied)
        outcome = "SEND COMMAND" if should_send else "NO COMMAND"
        percept = f"temperature={temperature}°C, occupied={occupied}"
        print(f"{label} | {previous} | {percept} | {target} | {outcome}")

if __name__ == "__main__":
    run_trace()
