"""
https://github.com/Dygmalab/Bazecor/blob/development/FOCUS_API.md
https://github.com/Dygmalab/Raise-Firmware/blob/master/FOCUS_API.MD
"""


from dygma_dvt_led_fix.dygma.keyboard import DygmaKeyboard
from dygma_dvt_led_fix.dygma.utils import detect_dygma_keyboards


def main():
    raise2_configuration = next(
        keyboard
        for keyboard in detect_dygma_keyboards()
        if keyboard.hardware_identifier.product == "Raise2")
    raise2 = DygmaKeyboard(raise2_configuration)

    for led_id in range(69, 99):  # left side
        print(f"l.{led_id}{raise2.led_at(led_id)}")

    for led_id in range(99, 131):  # right side
        print(f"r.{led_id}{raise2.led_at(led_id)}")

    
if __name__ == "__main__":
    main()
