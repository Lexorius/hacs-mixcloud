# Mixcloud Home Assistant Integration

**Version 1.0.0**

This custom component integrates [Mixcloud](https://www.mixcloud.com/) user data into [Home Assistant](https://www.home-assistant.io/) via HACS. It provides sensors for follower counts, uploads, and profile information for any public Mixcloud user.

---

## Features

- **Sensors for all count fields**: Follower count, following count, cloudcast count, favorite count, listen count.
- **Profile sensor**: All other profile information (bio, city, country, etc.) is available as attributes of a single sensor.
- **Last upload sensor**: Shows the latest upload and its details.
- **Flexible config flow**: Enter either your Mixcloud username or the full profile URL during setup.

---

## Installation

1. **Via HACS (recommended):**
   - Go to HACS → Integrations → Custom repositories.
   - Add this repository URL and select "Integration".
   - Search for "Mixcloud" and install.

2. **Manual:**
   - Copy the `mixcloud` folder into your `custom_components` directory.

3. **Restart Home Assistant** after installation.

---

## Configuration

### Add via UI

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Mixcloud**.
3. Enter either your Mixcloud username (e.g. `knockwood`) **or** your profile URL (e.g. `https://api.mixcloud.com/knockwood/`).
4. Confirm and finish setup.

### Options

- **Scan interval**: By default, data is updated every 5 minutes (300 seconds). You can adjust this in the integration options.

---

## Sensors

After setup, the following sensors will be created (replace `yourusername` with your Mixcloud username):

- `sensor.mixcloud_yourusername_follower_count`
- `sensor.mixcloud_yourusername_following_count`
- `sensor.mixcloud_yourusername_cloudcast_count`
- `sensor.mixcloud_yourusername_favorite_count`
- `sensor.mixcloud_yourusername_listen_count`
- `sensor.mixcloud_yourusername_profile`  
  - Attributes: `biog`, `created_time`, `updated_time`, `is_pro`, `is_premium`, `city`, `country`, `cover_pictures`, etc.
- `sensor.mixcloud_yourusername_last_upload`  
  - State: Name of the last upload  
  - Attributes: `created_time`, `url`, `plays`, `likes`

---

## Example

**Profile sensor attributes:**
```yaml
biog: "The german dj and radio-host..."
created_time: "2013-12-16T22:55:03Z"
city: "Stuttgart"
country: "Germany"
is_pro: true
cover_pictures:
  835wx120h: "https://thumbnailer.mixcloud.com/..."
  ...
```

---

## Troubleshooting

- If you see `Network error` or `invalid_username`, check your username or URL.
- Only public Mixcloud profiles are supported.
- Make sure your Home Assistant instance can reach `api.mixcloud.com`.

---

## Version

**1.0.0**

---

## Credits

- [Mixcloud API](https://www.mixcloud.com/developers/)
- Home Assistant Community

---

## License

MIT License