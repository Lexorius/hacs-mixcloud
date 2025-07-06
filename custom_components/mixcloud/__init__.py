DOMAIN = "mixcloud"
PLATFORMS = ["sensor"]

async def async_setup_entry(hass, entry):
    await hass.config_entries.async_forward_entry_setup(entry, "sensor")
    return True

async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")