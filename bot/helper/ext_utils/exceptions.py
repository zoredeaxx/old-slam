class DirectDownloadLinkException(Exception):
    """No method found for extracting direct download link from the http link"""
    pass


class NotSupportedExtractionArchive(Exception):
    """The archive format you are trying to extract is not supported"""
    pass
