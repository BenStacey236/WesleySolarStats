import foxesscloud.openapi as f

def configure_connection(apiKey: str, serialNumber: str) -> f:
    """Configures the api connection
    
    :param apiKey: The API key use to acces data
    :param serialNumber: The serial number of the datalogger you want to access

    :raises TypeError: If apiKey or serialNumber provided are not type string
    """

    if type(apiKey) != str:
        raise TypeError(f"apiKey must be type string, instead got {type(apiKey)}")
    
    if type(serialNumber) != str:
        raise TypeError(f"serialNumber must be type string, instead got {type(serialNumber)}")

    f.api_key = apiKey
    f.device_sn = serialNumber
    f.time_zone = "Europe/London"

    return f