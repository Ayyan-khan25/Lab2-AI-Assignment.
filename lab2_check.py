from lab2_model import HVACController

def main():
    c = HVACController()
    assert c.update(17, True)[:2] == ("HEAT", True)
    assert c.update(17, True)[:2] == ("HEAT", False)  # duplicate suppressed
    assert c.update(18, True)[:2] == ("OFF", True)    # exact lower boundary
    assert c.update(26, True)[:2] == ("OFF", False)   # exact upper boundary
    assert c.update(27, True)[:2] == ("COOL", True)   # mode transition
    assert c.update(30, False)[:2] == ("OFF", True)   # occupancy priority
    print("All checks passed.")

if __name__ == "__main__":
    main()
