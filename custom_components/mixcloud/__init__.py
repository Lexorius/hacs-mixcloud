DOMAIN = "mixcloud"
PLATFORMS = ["sensor"]

async def async_setup_entry(hass, entry):
    # Fallback für alte und neue Versionen:
    try:
        # Neue Methode (ab 2024.5)
        await hass.config_entries.async_forward_entry_setups("sensor", [entry])
    except AttributeError:
        # Alte Methode (2024.4 und älter)
        await hass.config_entries.async_forward_entry_setup(entry, "sensor")
    return True

async def async_unload_entry(hass, entry):
    try:
        return await hass.config_entries.async_forward_entry_unloads("sensor", [entry])
    except AttributeError:
        return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
