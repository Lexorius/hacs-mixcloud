from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class MixcloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mixcloud."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Hier könntest du ggf. noch Validierung machen
            return self.async_create_entry(title=user_input["username"], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("username"): str,
            }),
            errors=errors,
        )