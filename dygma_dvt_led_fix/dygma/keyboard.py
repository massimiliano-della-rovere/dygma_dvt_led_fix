from __future__ import annotations

from typing import TYPE_CHECKING

from dygma_dvt_led_fix.auxillary_types import RGBW
from dygma_dvt_led_fix.dygma.descriptors import (
    FirmwareVersionDescriptor, HardwareIdentifierDescriptor,
    HardwareVersionDescriptor, KeyboardLayoutDescriptor,
    NeuronIdentifierDescriptor, PaletteDescriptor, SettingsVersionDescriptor)
from dygma_dvt_led_fix.dygma.utils import neuron_io

if TYPE_CHECKING:
    from dygma_dvt_led_fix.dygma.utils import DetectedKeyboard


class DygmaKeyboard:
    def __init__(self, keyboard: DetectedKeyboard):
        self.keyboard = keyboard

    @property
    def device(self) -> str:
        return self.keyboard.serial_port.device

    @property
    def serial_number(self) -> str:
        return self.keyboard.serial_port.serial_number  # pyright: ignore [reportReturnType]

    @property
    def color_components_size(self) -> int:
        return 4 if self.keyboard.hardware_identifier.rgbw_mode else 3

    @property
    def rgbw_mode(self) -> bool:
        return self.keyboard.hardware_identifier.rgbw_mode 

    firmware_version = FirmwareVersionDescriptor()
    hardware_identifier = HardwareIdentifierDescriptor()
    hardware_version = HardwareVersionDescriptor()
    keyboard_layout = KeyboardLayoutDescriptor()
    neuron_identifier = NeuronIdentifierDescriptor()
    palette = PaletteDescriptor()
    settings_version = SettingsVersionDescriptor()
    
    def led_at(self, led_id: int, rgbw: RGBW | None = None) -> RGBW | None:
        request = ["led.at", str(led_id)]
        if rgbw is not None:
            request.extend(map(str, (rgbw.r, rgbw.g, rgbw.b)))
        request = " ".join(request)
        print(request, end=" -> ")
        
        reply = neuron_io(self.device, request)
        if rgbw is None:
            values = next(reply)
            print(values)
            return RGBW(*tuple(int(v) for v in values.split(" ")), w=0)
        else:
            print("")

