from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    CoordinatorEntity,
)
from datetime import timedelta
import aiohttp
import asyncio

from .const import DOMAIN, API_BASE_URL

SENSOR_TYPES = {
    "followers": {"name": "Follower", "icon": "mdi:account-multiple"},
    "uploads": {"name": "Uploads", "icon": "mdi:cloud-upload"},
    "last_upload": {"name": "Letzte Veröffentlichung", "icon": "mdi:music-note"},
    # Add more as you need
}

async def async_setup_entry(hass, entry, async_add_entities):
    username = entry.data["username"]
    session = aiohttp.ClientSession()

    async def async_update_data():
        url = f"{API_BASE_URL}/user/{username}/"
        async with session.get(url) as resp:
            data = await resp.json()
            # Fetch last upload data
            uploads_url = data.get("uploads", {}).get("url")
            last_upload = None
            if uploads_url:
                async with session.get(uploads_url) as upload_resp:
                    uploads_data = await upload_resp.json()
                    if "data" in uploads_data and uploads_data["data"]:
                        last_upload = uploads_data["data"][0]
            return {"profile": data, "last_upload": last_upload}

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"mixcloud_{username}",
        update_method=async_update_data,
        update_interval=timedelta(minutes=10),
    )
    await coordinator.async_config_entry_first_refresh()

    sensors = [
        MixcloudSensor(coordinator, entry, "followers"),
        MixcloudSensor(coordinator, entry, "uploads"),
        MixcloudSensor(coordinator, entry, "last_upload"),
    ]
    async_add_entities(sensors)

import logging
_LOGGER = logging.getLogger(__name__)

class MixcloudSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry, sensor_type):
        super().__init__(coordinator)
        self.coordinator = coordinator
        self._type = sensor_type
        self._attr_unique_id = f"mixcloud_{entry.data['username']}_{sensor_type}"
        self._attr_name = f"Mixcloud {SENSOR_TYPES[sensor_type]['name']}"
        self._attr_icon = SENSOR_TYPES[sensor_type]["icon"]

    @property
    def state(self):
        data = self.coordinator.data
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
        if self._type == "last_upload" and self.coordinator.data["last_upload"]:
            upload = self.coordinator.data["last_upload"]
            return {
                "created_time": upload.get("created_time"),
                "url": upload.get("url"),
                "plays": upload.get("play_count"),
                "likes": upload.get("favorite_count"),
            }
        return {}