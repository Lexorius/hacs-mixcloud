from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

import logging
_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "followers": {"name": "Follower", "icon": "mdi:account-multiple"},
    "uploads": {"name": "Uploads", "icon": "mdi:cloud-upload"},
    "last_upload": {"name": "Letzte Veröffentlichung", "icon": "mdi:music-note"},
}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    sensors = [
        MixcloudSensor(coordinator, entry, "followers"),
        MixcloudSensor(coordinator, entry, "uploads"),
        MixcloudSensor(coordinator, entry, "last_upload"),
    ]
    async_add_entities(sensors)

class MixcloudSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry, sensor_type):
        super().__init__(coordinator)
        self._type = sensor_type
        self._attr_unique_id = f"mixcloud_{entry.data['username']}_{sensor_type}"
        self._attr_name = f"Mixcloud {SENSOR_TYPES[sensor_type]['name']}"
        self._attr_icon = SENSOR_TYPES[sensor_type]["icon"]

    @property
    def state(self):
        data = self.coordinator.data
        if not data:
            return None
        if self._type == "followers":
            return data["profile"].get("followers_count")
        elif self._type == "uploads":
            return data["profile"].get("cloudcast_count")
        elif self._type == "last_upload":
            if data["last_upload"]:
                return data["last_upload"].get("name")
            return None

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data
        if self._type == "last_upload" and data and data.get("last_upload"):
            upload = data["last_upload"]
            return {
                "created_time": upload.get("created_time"),
                "url": upload.get("url"),
                "plays": upload.get("play_count"),
                "likes": upload.get("favorite_count"),
            }
        return {}