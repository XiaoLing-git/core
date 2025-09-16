"""Support for the Switchbot Smart Radiator Thermostat."""

from switchbot_api import SmartRadiatorThermostatMode

from homeassistant.components.water_heater import (
    WaterHeaterEntity,
    WaterHeaterEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import SwitchbotCloudData
from .const import DOMAIN
from .entity import SwitchBotCloudEntity

operation_list = [i.name for i in SmartRadiatorThermostatMode.get_all_modes()]


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up SwitchBot Cloud entry."""
    data: SwitchbotCloudData = hass.data[DOMAIN][config.entry_id]
    async_add_entities(
        SwitchBotSmartRadiatorThermostat(data.api, device, coordinator)
        for device, coordinator in data.devices.water_heaters
    )


class SwitchBotSmartRadiatorThermostat(SwitchBotCloudEntity, WaterHeaterEntity):
    """Representation of a SwitchBot Smart Radiator Thermostat."""

    _attr_name = None
    _attr_supported_features = (
        WaterHeaterEntityFeature.TARGET_TEMPERATURE
        | WaterHeaterEntityFeature.ON_OFF
        | WaterHeaterEntityFeature.OPERATION_MODE
    )
    _attr_temperature_unit = UnitOfTemperature.CELSIUS

    # async def async_set_temperature(self, **kwargs: Any) -> None:
    #     print(f"async_set_temperature was call {kwargs}")
    #     # target_temperature = kwargs["temperature"]
    #     # if self._attr_current_operation == SmartRadiatorThermostatMode.MANUEL.name:
    #     #     await self.send_api_command(
    #     #         command=SmartRadiatorThermostatCommands.SET_MANUAL_MODE_TEMPERATURE,
    #     #         parameters=str(target_temperature),
    #     #     )
    #     #     await asyncio.sleep(10)
    #     #     await self.coordinator.async_request_refresh()
    #     #     self._attr_target_temperature = target_temperature
    #
    # async def async_set_operation_mode(self, operation_mode: str) -> None:
    #     print(f"async_set_operation_mode {operation_mode}")
    #     # parameters = self.__mode_map_value(operation_mode)
    #     # await self.send_api_command(
    #     #     command=SmartRadiatorThermostatCommands.SET_MODE,
    #     #     parameters=str(parameters),
    #     # )
    #     # await asyncio.sleep(10)
    #     # await self.coordinator.async_request_refresh()

    # async def async_turn_on(self, **kwargs: Any) -> None:
    #     print(f"async_turn_on was call {kwargs}")
    #
    # async def async_turn_off(self, **kwargs: Any) -> None:
    #     print(f"async_turn_off was call {kwargs}")
    #
    # async def async_turn_away_mode_on(self) -> None:
    #     print("async_turn_away_mode_on was call ")
    #
    # async def async_turn_away_mode_off(self) -> None:
    #     print("async_turn_away_mode_off was call ")

    def _set_attributes(self) -> None:
        """Set attributes from coordinator data."""
        if self.coordinator.data is None:
            return
        # print(self.coordinator.data)
        # mode: int | None = self.coordinator.data.get("mode")
        # temperature: str | None = self.coordinator.data.get("temperature")
        # self._attr_current_temperature = temperature
        # self._attr_current_operation = self.__value_map_mode(mode)

        # if self._attr_current_operation == SmartRadiatorThermostatMode.MANUEL.name:
        #     self._attr_supported_features =(
        #             WaterHeaterEntityFeature.TARGET_TEMPERATURE
        #             | WaterHeaterEntityFeature.OPERATION_MODE
        #             # | WaterHeaterEntityFeature.AWAY_MODE
        #             | WaterHeaterEntityFeature.ON_OFF
        #                 )
        # else:
        #     self._attr_supported_features = (
        #             WaterHeaterEntityFeature.OPERATION_MODE
        #             # | WaterHeaterEntityFeature.AWAY_MODE
        #             | WaterHeaterEntityFeature.ON_OFF
        #     )

    # def __value_map_mode(self,value:int)->str:
    #     for i in SmartRadiatorThermostatMode.get_all_modes():
    #         if i.value == value:
    #             return i.name
    #     # raise NotImplementedError(f"{value} Not Supported")
    #
    # def __mode_map_value(self,mode:str)->int:
    #     for i in SmartRadiatorThermostatMode.get_all_modes():
    #         if i.name == mode:
    #             return i.value
    #
    #     # raise NotImplementedError(f"{mode} Not Supported")
