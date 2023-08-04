from homeassistant.const import (
    ATTR_GPS_ACCURACY,
    CONF_API_KEY,
    CONF_ICON,
    CONF_NAME,
    CONF_UNIQUE_ID,
    CONF_ZONE,
    Platform,
)

DOMAIN = "places"
VERSION = "v2.4"
EVENT_TYPE = DOMAIN + "_state_update"
PLATFORM = Platform.SENSOR
ENTITY_ID_FORMAT = Platform.SENSOR + ".{}"

# Defaults
DEFAULT_EXTENDED_ATTR = False
DEFAULT_HOME_ZONE = "zone.home"
DEFAULT_ICON = "mdi:map-search-outline"
DEFAULT_MAP_PROVIDER = "apple"
DEFAULT_MAP_ZOOM = 18
DEFAULT_DISPLAY_OPTIONS = "zone_name, place"
DEFAULT_SHOW_TIME = False
DEFAULT_USE_GPS = True

# Settings

TRACKING_DOMAINS = [
    str(Platform.DEVICE_TRACKER),
    str("person"),
    str(Platform.SENSOR),
    CONF_ZONE,
    "variable",
]
TRACKING_DOMAINS_NEED_LATLONG = [
    str(Platform.SENSOR),
    "variable",
]
HOME_LOCATION_DOMAINS = [CONF_ZONE]

# Config
CONF_DEVICETRACKER_ID = "devicetracker_id"
CONF_EXTENDED_ATTR = "extended_attr"
CONF_HOME_ZONE = "home_zone"
CONF_LANGUAGE = "language"
CONF_MAP_PROVIDER = "map_provider"
CONF_MAP_ZOOM = "map_zoom"
CONF_NATIVE_VALUE = "native_value"
CONF_DISPLAY_OPTIONS = "options"
CONF_SHOW_TIME = "show_time"
CONF_USE_GPS = "use_gps_accuracy"
CONF_YAML_HASH = "yaml_hash"

# Attributes
ATTR_CITY = "city"
ATTR_CITY_CLEAN = "city_clean"
ATTR_COUNTRY = "country"
ATTR_COUNTRY_CODE = "country_code"
ATTR_COUNTY = "county"
ATTR_DEVICETRACKER_ID = "devicetracker_entityid"
ATTR_DEVICETRACKER_ZONE = "devicetracker_zone"
ATTR_DEVICETRACKER_ZONE_NAME = "devicetracker_zone_name"
ATTR_DIRECTION_OF_TRAVEL = "direction_of_travel"
ATTR_DISPLAY_OPTIONS_LIST = "display_options_list"
ATTR_DISTANCE_FROM_HOME_KM = "distance_from_home_km"
ATTR_DISTANCE_FROM_HOME_M = "distance_from_home_m"
ATTR_DISTANCE_FROM_HOME_MI = "distance_from_home_mi"
ATTR_DISTANCE_TRAVELED_M = "distance_traveled_m"
ATTR_DISTANCE_TRAVELED_MI = "distance_traveled_mi"
ATTR_DRIVING = "driving"
ATTR_FORMATTED_ADDRESS = "formatted_address"
ATTR_FORMATTED_PLACE = "formatted_place"
ATTR_HOME_LATITUDE = "home_latitude"
ATTR_HOME_LOCATION = "home_location"
ATTR_HOME_LONGITUDE = "home_longitude"
ATTR_HOME_ZONE = "home_zone"
ATTR_INITIAL_UPDATE = "initial_update"
ATTR_JSON_FILENAME = "json_filename"
ATTR_LAST_CHANGED = "last_changed"
ATTR_LAST_PLACE_NAME = "last_place_name"
ATTR_LAST_UPDATED = "last_updated"
ATTR_LATITUDE = "current_latitude"
ATTR_LATITUDE_OLD = "previous_latitude"
ATTR_LOCATION_CURRENT = "current_location"
ATTR_LOCATION_PREVIOUS = "previous_location"
ATTR_LONGITUDE = "current_longitude"
ATTR_LONGITUDE_OLD = "previous_longitude"
ATTR_MAP_LINK = "map_link"
ATTR_NATIVE_VALUE = "native_value"
ATTR_DISPLAY_OPTIONS = "display_options"
ATTR_OSM_DETAILS_DICT = "osm_details_dict"
ATTR_OSM_DICT = "osm_dict"
ATTR_OSM_ID = "osm_id"
ATTR_OSM_TYPE = "osm_type"
ATTR_PICTURE = "entity_picture"
ATTR_PLACE_CATEGORY = "place_category"
ATTR_PLACE_NAME = "place_name"
ATTR_PLACE_NAME_NO_DUPE = "place_name_no_dupe"
ATTR_PLACE_NEIGHBOURHOOD = "neighbourhood"
ATTR_PLACE_TYPE = "place_type"
ATTR_POSTAL_CODE = "postal_code"
ATTR_POSTAL_TOWN = "postal_town"
ATTR_PREVIOUS_STATE = "previous_state"
ATTR_REGION = "state_province"
ATTR_SHOW_DATE = "show_date"
ATTR_STATE_ABBR = "state_abbr"
ATTR_STREET = "street"
ATTR_STREET_REF = "street_ref"
ATTR_STREET_NUMBER = "street_number"
# ATTR_UPDATES_SKIPPED = "updates_skipped"
ATTR_WIKIDATA_DICT = "wikidata_dict"
ATTR_WIKIDATA_ID = "wikidata_id"


# Attribute Lists
CONFIG_ATTRIBUTES_LIST = [
    CONF_API_KEY,
    CONF_DEVICETRACKER_ID,
    CONF_EXTENDED_ATTR,
    CONF_HOME_ZONE,
    CONF_ICON,
    CONF_LANGUAGE,
    CONF_MAP_PROVIDER,
    CONF_MAP_ZOOM,
    CONF_NAME,
    CONF_DISPLAY_OPTIONS,
    CONF_SHOW_TIME,
    CONF_USE_GPS,
    CONF_UNIQUE_ID,
]
RESET_ATTRIBUTE_LIST = [
    ATTR_CITY,
    ATTR_CITY_CLEAN,
    ATTR_COUNTRY,
    ATTR_COUNTRY_CODE,
    ATTR_COUNTY,
    ATTR_DRIVING,
    ATTR_FORMATTED_ADDRESS,
    ATTR_FORMATTED_PLACE,
    ATTR_MAP_LINK,
    ATTR_OSM_DETAILS_DICT,
    ATTR_OSM_DICT,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
    ATTR_PLACE_CATEGORY,
    ATTR_PLACE_NAME,
    ATTR_PLACE_NAME_NO_DUPE,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_PLACE_TYPE,
    ATTR_POSTAL_CODE,
    ATTR_POSTAL_TOWN,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_STREET_REF,
    ATTR_WIKIDATA_DICT,
    ATTR_WIKIDATA_ID,
]
EXTRA_STATE_ATTRIBUTE_LIST = [
    ATTR_PLACE_NAME,
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_CITY,
    ATTR_POSTAL_TOWN,
    ATTR_POSTAL_CODE,
    ATTR_COUNTY,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_COUNTRY,
    ATTR_COUNTRY_CODE,
    ATTR_FORMATTED_PLACE,
    ATTR_FORMATTED_ADDRESS,
    ATTR_PLACE_TYPE,
    ATTR_PLACE_CATEGORY,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
    ATTR_LATITUDE_OLD,
    ATTR_LONGITUDE_OLD,
    ATTR_DEVICETRACKER_ID,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_HOME_ZONE,
    ATTR_HOME_LATITUDE,
    ATTR_HOME_LONGITUDE,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_LAST_PLACE_NAME,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
    ATTR_MAP_LINK,
    ATTR_GPS_ACCURACY,
    ATTR_PICTURE,
    ATTR_DISPLAY_OPTIONS,
    ATTR_LAST_CHANGED,
    ATTR_LAST_UPDATED,
]
JSON_IGNORE_ATTRIBUTE_LIST = [
    ATTR_DEVICETRACKER_ID,
    ATTR_DISPLAY_OPTIONS,
    ATTR_DISPLAY_OPTIONS_LIST,
    ATTR_HOME_LATITUDE,
    ATTR_HOME_LOCATION,
    ATTR_HOME_LONGITUDE,
    ATTR_INITIAL_UPDATE,
    ATTR_DRIVING,
    ATTR_JSON_FILENAME,
    ATTR_LOCATION_CURRENT,
    ATTR_LOCATION_PREVIOUS,
    ATTR_PREVIOUS_STATE,
]
JSON_ATTRIBUTE_LIST = [
    ATTR_CITY,
    ATTR_CITY_CLEAN,
    ATTR_COUNTRY,
    ATTR_COUNTY,
    ATTR_COUNTRY_CODE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_FORMATTED_ADDRESS,
    ATTR_FORMATTED_PLACE,
    ATTR_GPS_ACCURACY,
    ATTR_LAST_CHANGED,
    ATTR_LAST_PLACE_NAME,
    ATTR_LAST_UPDATED,
    ATTR_LATITUDE_OLD,
    ATTR_LATITUDE,
    ATTR_LONGITUDE_OLD,
    ATTR_LONGITUDE,
    ATTR_MAP_LINK,
    ATTR_NATIVE_VALUE,
    ATTR_OSM_DETAILS_DICT,
    ATTR_OSM_DICT,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
    ATTR_PLACE_CATEGORY,
    ATTR_PLACE_NAME,
    ATTR_PLACE_NAME_NO_DUPE,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_PLACE_TYPE,
    ATTR_POSTAL_CODE,
    ATTR_POSTAL_TOWN,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_STREET_REF,
    ATTR_WIKIDATA_DICT,
    ATTR_WIKIDATA_ID,
    ATTR_SHOW_DATE,
]
EVENT_ATTRIBUTE_LIST = [
    ATTR_PLACE_NAME,
    ATTR_LAST_CHANGED,
    ATTR_LAST_PLACE_NAME,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
    ATTR_LATITUDE_OLD,
    ATTR_LONGITUDE_OLD,
    ATTR_MAP_LINK,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
]
EXTENDED_ATTRIBUTE_LIST = [
    ATTR_WIKIDATA_ID,
    ATTR_OSM_DICT,
    ATTR_OSM_DETAILS_DICT,
    ATTR_WIKIDATA_DICT,
]
PLACE_NAME_DUPLICATE_LIST = [
    ATTR_STREET,
    ATTR_STREET_REF,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_CITY,
    ATTR_POSTAL_TOWN,
    ATTR_POSTAL_CODE,
    ATTR_COUNTY,
    ATTR_REGION,
    ATTR_COUNTRY,
    ATTR_PLACE_TYPE,
    ATTR_PLACE_CATEGORY,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
]

DISPLAY_OPTIONS_MAP = {
    "driving": ATTR_DRIVING,
    "place_name": ATTR_PLACE_NAME,
    "name": ATTR_PLACE_NAME,
    "place_name_no_dupe": ATTR_PLACE_NAME_NO_DUPE,
    "name_no_dupe": ATTR_PLACE_NAME_NO_DUPE,
    "place_type": ATTR_PLACE_TYPE,
    "place_category": ATTR_PLACE_CATEGORY,
    "type": ATTR_PLACE_TYPE,
    "category": ATTR_PLACE_CATEGORY,
    "street_number": ATTR_STREET_NUMBER,
    "house_number": ATTR_STREET_NUMBER,
    "street": ATTR_STREET,
    "street_ref": ATTR_STREET_REF,
    "route_number": ATTR_STREET_REF,
    "neighborhood": ATTR_PLACE_NEIGHBOURHOOD,
    "neighbourhood": ATTR_PLACE_NEIGHBOURHOOD,
    "place_neighborhood": ATTR_PLACE_NEIGHBOURHOOD,
    "place_neighbourhood": ATTR_PLACE_NEIGHBOURHOOD,
    "city": ATTR_CITY,
    "city_clean": ATTR_CITY_CLEAN,
    "postal_town": ATTR_POSTAL_TOWN,
    "region": ATTR_REGION,
    "state": ATTR_REGION,
    "state_abbr": ATTR_STATE_ABBR,
    "county": ATTR_COUNTY,
    "country": ATTR_COUNTRY,
    "country_code": ATTR_COUNTRY_CODE,
    "postal_code": ATTR_POSTAL_CODE,
    "zip_code": ATTR_POSTAL_CODE,
    "latitude": ATTR_LATITUDE,
    "longitude": ATTR_LONGITUDE,
    "zone": ATTR_DEVICETRACKER_ZONE,
    "zone_name": ATTR_DEVICETRACKER_ZONE_NAME,
}
