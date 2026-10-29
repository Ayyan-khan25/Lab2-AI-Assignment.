class HVACController:
    """Stateful HVAC controller that suppresses duplicate commands."""

    def __init__(self):
        self.previous_mode = "OFF"

    def target_mode(self, temperature, occupied):
        # Occupancy has priority: an empty room must be OFF.
        if not occupied:
            return "OFF"
        if temperature < 18:
            return "HEAT"
        if temperature > 26:
            return "COOL"
        return "OFF"

    def update(self, temperature, occupied):
        target = self.target_mode(temperature, occupied)
        previous = self.previous_mode
        should_send = target != previous

        # Store the new target mode for the next percept.
        self.previous_mode = target
        return target, should_send, previous
