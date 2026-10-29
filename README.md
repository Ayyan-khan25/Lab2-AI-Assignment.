# Lab 2 — Task 3: Stateful HVAC Controller

## Files
- `lab2_model.py`: controller logic and previous-mode storage.
- `lab2_percepts.py`: runs the required percept sequence and prints the trace.
- `lab2_check.py`: simple assertions for repeated percepts, boundaries, transition, and empty room.
- `trace.txt`: recorded run output.

## Assumptions
- Occupancy has priority: if the room is empty, the target is always `OFF`.
- If occupied: temperature below 18°C => `HEAT`; above 26°C => `COOL`; otherwise => `OFF`.
- Therefore, exactly 18°C and exactly 26°C both map to `OFF`.
- Initial previous target mode is `OFF`.
- A command is sent only when the newly calculated target differs from the previous target.

## Run
```bash
python lab2_percepts.py
python lab2_check.py
```
