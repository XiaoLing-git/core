"""Platform for sensor integration."""

from switchbot_api import Device, SwitchBotAPI

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import SwitchbotCloudData
from .const import (
    COMMON_SENSOR_DESCRIPTION_LIST,
    DOMAIN,
    SENSOR_DESCRIPTIONS_BY_DEVICE_TYPES,
)
from .coordinator import SwitchBotCoordinator
from .entity import SwitchBotCloudEntity


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up SwitchBot Cloud entry."""
    data: SwitchbotCloudData = hass.data[DOMAIN][config.entry_id]

    cloud_sensor_entities: list[SwitchBotCloudSensor] = []
    for device, coordinator in data.devices.sensors:
        if not coordinator.data:
            continue
        if device.device_type in list(SENSOR_DESCRIPTIONS_BY_DEVICE_TYPES):
            for description in SENSOR_DESCRIPTIONS_BY_DEVICE_TYPES[device.device_type]:
                if coordinator.data.get(description.key):
                    cloud_sensor_entities.extend(
                        [
                            SwitchBotCloudSensor(
                                data.api, device, coordinator, description
                            )
                        ]
                    )
        else:
            for description in COMMON_SENSOR_DESCRIPTION_LIST:
                if coordinator.data.get(description.key):
                    cloud_sensor_entities.extend(
                        [
                            SwitchBotCloudSensor(
                                data.api, device, coordinator, description
                            )
                        ]
                    )

    async_add_entities(cloud_sensor_entities)


class SwitchBotCloudSensor(SwitchBotCloudEntity, SensorEntity):
    """Representation of a SwitchBot Cloud sensor entity."""

    def __init__(
        self,
        api: SwitchBotAPI,
        device: Device,
        coordinator: SwitchBotCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize SwitchBot Cloud sensor entity."""
        super().__init__(api, device, coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{device.device_id}_{description.key}"

    def _set_attributes(self) -> None:
        """Set attributes from coordinator data."""
        if not self.coordinator.data:
            return
        self._attr_native_value = self.coordinator.data.get(self.entity_description.key)
