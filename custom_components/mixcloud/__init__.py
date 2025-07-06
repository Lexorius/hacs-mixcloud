"""Mixcloud Integration für Home Assistant."""
from __future__ import annotations

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Mixcloud from a config entry."""
    username = entry.data["username"]
    session = async_get_clientsession(hass)

    # Im hass.data speichern
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "username": username,
        "session": session,
    }

    _LOGGER.debug("Setting up Mixcloud entry for user '%s'", username)

    # *** NEUE API: Plattformen als Liste, Entry als einzelnes Objekt! ***
    await hass.config_entries.async_forward_entry_setups(["sensor"], entry)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
        _LOGGER.debug("Unloaded Mixcloud entry for user '%s'", entry.data["username"])
    return unload_ok

async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Cleanup on removal."""
    hass.data[DOMAIN].pop(entry.entry_id, None)
    _LOGGER.debug("Removed Mixcloud entry for user '%s'", entry.data["username"])
