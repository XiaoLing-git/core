"""Support for the Switchbot Smart Radiator Thermostat."""

from switchbot_api import Device, Remote, SwitchBotAPI

from homeassistant.components.water_heater import WaterHeaterEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import SwitchbotCloudData, SwitchBotCoordinator
from .const import DOMAIN
from .entity import SwitchBotCloudEntity


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up SwitchBot Cloud entry."""
    data: SwitchbotCloudData = hass.data[DOMAIN][config.entry_id]
    async_add_entities(
        _async_make_entity(data.api, device, coordinator)
        for device, coordinator in data.devices.water_heaters
    )


class SwitchBotSmartRadiatorThermostat(SwitchBotCloudEntity, WaterHeaterEntity):
    """Representation of a SwitchBot Smart Radiator Thermostat."""


@callback
def _async_make_entity(
    api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator
) -> SwitchBotSmartRadiatorThermostat:
    """Make a SwitchBot Smart Radiator Thermostat."""
    return SwitchBotSmartRadiatorThermostat(api, device, coordinator)
