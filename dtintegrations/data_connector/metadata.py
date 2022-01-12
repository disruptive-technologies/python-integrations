from dtintegrations import outputs


class DeviceMetadata(outputs.OutputBase):
    """
    Represents the source device metadata.

    Attributes
    ----------
    device_id : str
        Unique identifier of the source device.
    project_id : str
        Unique identifier of the source project.
    device_type : str
        Source device type.
    product_number : str
        Source device product number.
    """

    def __init__(self, metadata: dict):
        self.device_id = metadata['deviceId']
        self.project_id = metadata['projectId']
        self.device_type = metadata['deviceType']
        self.product_number = metadata['productNumber']
