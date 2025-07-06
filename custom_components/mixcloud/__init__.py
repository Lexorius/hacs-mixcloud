"""Mixcloud Integration für Home Assistant."""
from __future__ import annotations

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, API_BASE_URL

PLATFORMS = ["sensor"]
_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Mixcloud from a config entry."""

    username = entry.data["username"]
    session = async_get_clientsession(hass)

    # Du kannst später hier einen DataUpdateCoordinator (oder eigene API-Klasse) initialisieren:
    # Für den Anfang speichern wir den username, die session und ggf. später weitere Objekte
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "username": username,
        "session": session,
        # "coordinator": ... (falls du einen Coordinator zentral nutzen willst)
    }

    _LOGGER.debug("Setting up Mixcloud entry for user '%s'", username)

    # Plattformen laden (sensor.py etc.)
    await hass.config_entries.async_forward_entry_setups(PLATFORMS, entry)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    _LOGGER.debug("Unloaded Mixcloud entry for user '%s'", entry.data["username"])
    return unload_ok


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Cleanup on removal."""
    hass.data[DOMAIN].pop(entry.entry_id, None)
    _LOGGER.debug("Removed Mixcloud entry for user '%s'", entry.data["username"])
