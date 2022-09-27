# places


[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]

<!--- [![Discord][discord-shield]][discord] -->
<!--- [![Community Forum][forum-shield]][forum] -->

_Component to integrate with OpenStreetMap Reverse Geocode_

## Installation

### Installation via HACS

Unless you have a good reason not to, you probably want to install this component via HACS (Home Assistant Community Store)
1. Ensure that [HACS](https://hacs.xyz/) is installed
1. Navigate to HACS -> Integrations
1. Open the three-dot menu and select 'Custom Repositories'
1. Put 'https://github.com/custom-components/places' into the 'Repository' textbox.
1. Select 'Integration' as the category
1. Press 'Add'.
1. Find the Places integration in the HACS integration list and install it
1. Add your configuration
1. Restart Home Assistant

### Manual Installation

You probably do not want to do this! Use the HACS method above unless you have a very good reason why you are installing manually

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`)
1. If you do not have a `custom_components` directory (folder) there, you need to create it
1. In the `custom_components` directory (folder) create a new folder called `places`
1. Download _all_ the files from the `custom_components/places/` directory (folder) in this repository
1. Place the files you downloaded in the new directory (folder) you created
1. Add your configuration
1. Restart Home Assistant

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/places/__init__.py
custom_components/places/manifest.json
custom_components/places/sensor.py
```

## Configuration options

Key | Type | Required | Description | Default |
-- | -- | -- | -- | --
`devicetracker_id` | `entity_id` | `True` | The location device to track | None
`name` | `string` | `True` | Friendly name of the places sensor | None
`home_zone` | `entity_id` | `False` | Used to calculate distance from home and direction of travel | `zone.home`
`api_key` | `string` | `False` | OpenStreetMap API key (your email address). | None
`map_provider` | `string` | `False` | `google`, `apple`, `osm` | `apple`
`map_zoom` | `number` | `False` | Level of zoom for the generated map link <1-20> | `18`
`language` | `string` | `False` | Requested<sup>\*</sup> language(s) for state and attributes. Two-Letter language code(s), separated by commas.<br><sup>\*</sup>Refer to [Notes](#notes) | location's local language
`scan_interval` | `number` | `False` | How often in seconds the sensor will poll for updates (separate from when the devicetracker_id's state changes which also triggers an update) <30-3,600> | `600`
`extended_attr` | `boolean` | `False` | Show extended attributes: wikidata_id, osm_dict, osm_details_dict, wikidata_dict *(if they exist)*. Provides many additional attributes for advanced logic. **Warning, will make the attributes very long!** | `False`
`options` | `string` | `False` | Display options: `formatted_place` *(exclusive option)*, `driving` *(can be used with formatted_place or other options)*, `zone` or `zone_name`, `place`, `place_name`, `street_number`, `street`, `city`, `county`, `state`, `postal_code`, `country`, `formatted_address`, `do_not_show_not_home` | `zone`, `place`

Sample attributes that can be used in notifications, alerts, automations, etc:
```json
{
  "formatted_address": "Richmond Hill GO Station, 6, Newkirk Road, Beverley Acres, Richmond Hill, York Region, Ontario, L4C 1B3, Canada",
  "friendly_name": "sharon",
  "current_latitude": "43.874149009154095",
  "distance_from_home_km": 7.24,
  "country": "Canada",
  "postal_code": "L4C 1B3",
  "direction_of_travel": "towards home",
  "neighbourhood": "Beverley Acres",
  "entity_picture": "/local/sharon.png",
  "street_number": "6",
  "devicetracker_entityid": "device_tracker.sharon_iphone7",
  "home_longitude": "-79.7323453871",
  "devicetracker_zone": "not_home",
  "distance_from_home_m": 17239.053,
  "home_latitude": "43.983234888",
  "previous_location": "43.86684124904056,-79.4253896502715",
  "previous_longitude": "-79.4253896502715",
  "place_category": "building",
  "map_link": "https://maps.apple.com/maps/?ll=43.874149009154095,-79.42642783709209&z=18",
  "last_changed": "2018-05-02 13:44:51.019837",
  "state_province": "Ontario",
  "county": "York Region",
  "current_longitude": "-79.42642783709209",
  "current_location": "43.874149009154095,-79.42642783709209",
  "place_type": "building",
  "previous_latitude": "43.86684124904056",
  "place_name": "Richmond Hill GO Station",
  "street": "Newkirk Road",
  "city": "Richmond Hill",
  "home_zone": "zone.sharon_home"
}
```

Sample generic automations.yaml snippet to send an iOS notify on any device state change:
(the only difference is the second one uses a condition to only trigger for a specific user)
```yaml
- alias: ReverseLocateEveryone
  initial_state: 'on'
  trigger:
    platform: event
    event_type: places_state_update
  action:
  - service: notify.ios_jim_iphone8
    data_template:
      title: 'ReverseLocate: {{ trigger.event.data.entity }} ({{ trigger.event.data.devicetracker_zone }}) {{ trigger.event.data.place_name }}'
      message: |-
        {{ trigger.event.data.entity }} ({{ trigger.event.data.devicetracker_zone }})
        {{ trigger.event.data.place_name }}
        {{ trigger.event.data.distance_from_home_km }} km from home and traveling {{ trigger.event.data.direction_of_travel }}
        {{ trigger.event.data.to_state }} ({{ trigger.event.data.last_changed }})
      data:
        attachment:
          url: '{{ trigger.event.data.map_link }}'
          hide_thumbnail: false

- alias: ReverseLocateAidan
  initial_state: 'on'
  trigger:
    platform: event
    event_type: places_state_update
  condition:
    condition: template
    value_template: '{{ trigger.event.data.entity == "aidan" }}'
  action:
  - service: notify.ios_jim_iphone8
    data_template:
      title: 'ReverseLocate: {{ trigger.event.data.entity }} ({{ trigger.event.data.devicetracker_zone }}) {{ trigger.event.data.place_name }}'
      message: |-
        {{ trigger.event.data.entity }} ({{ trigger.event.data.devicetracker_zone }})
        {{ trigger.event.data.place_name }}
        {{ trigger.event.data.distance_from_home_km }} km from home and traveling {{ trigger.event.data.direction_of_travel }}
        {{ trigger.event.data.to_state }} ({{ trigger.event.data.last_changed }})
      data:
        attachment:
          url: '{{ trigger.event.data.map_link }}'
          hide_thumbnail: false
```

## Notes:

* This component is only useful to those who have device tracking enabled via a mechanism that provides latitude and longitude coordinates (such as Owntracks or iCloud).
* The OpenStreetMap database is very flexible with regards to tag_names in their database schema.  If you come across a set of coordinates that do not parse properly, you can enable debug messages to see the actual JSON that is returned from the query.
* The OpenStreetMap API requests that you include your valid e-mail address in each API call if you are making a large numbers of requests.  They say that this information will be kept confidential and only used to contact you in the event of a problem, see their Usage Policy for more details.
* The map link that gets generated for Google, Apple or OpenStreetMaps has a push pin marking the users location. Note that when opening the Apple link on a non-Apple device, it will open in Google Maps.
* When no `language` value is given, default language will be location's local language. When a comma separated list of languages is provided - the component will attempt to fill each address field in desired languages by order.
* Translations are partial in OpenStreetMap database. For each field, if a translation is missing in first requested language it will be resolved with a language following in the provided list, defaulting to local language if no matching translations were found for the list.
* To enable detailed logging for this component, add the following to your configuration.yaml file
```yaml
  logger:
    default: warning
    logs:
      custom_components.places: debug  
```

## Prior Contributions:
* Original Author: [Jim Thompson](https://github.com/tenly2000)
* Subsequent Authors: [Ian Richardson](https://github.com/iantrich) & [Snuffy2](https://github.com/Snuffy2)

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[places]: https://github.com/custom-components/places
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/places.svg?style=for-the-badge
[commits]: https://github.com/custom-components/places/commits/master
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/reverse-geocode-sensor-places-using-openstreetmap-custom-component
[license-shield]: https://img.shields.io/github/license/custom-components/places.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Ian%20Richardson%20%40iantrich-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/places.svg?style=for-the-badge
[releases]: https://github.com/custom-components/places/releases
