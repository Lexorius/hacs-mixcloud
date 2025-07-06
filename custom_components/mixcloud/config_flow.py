import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_URL

from .const import DOMAIN

def _parse_username(user_input):
    if user_input.startswith("https://"):
        # Extract username from URL
        return user_input.rstrip('/').split("/")[-1]
    return user_input

class MixcloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            username = _parse_username(user_input["username"])
            return self.async_create_entry(
                title=username, data={"username": username}
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required("username", description="Benutzername oder Mixcloud-URL"): str}
            ),
            errors=errors,
        )