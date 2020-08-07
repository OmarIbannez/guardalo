from metadata_parser import MetadataParser
import requests
from requests.exceptions import ConnectionError
from typing import Optional, Dict, AnyStr


class Link:
    def __init__(self, url: AnyStr, headers: Optional[Dict] = None) -> None:
        self.is_invalid = False
        self.title = None
        self.description = None
        self.image = None
        self.headers = (
            {
                "User-Agent": "Mozilla/5.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "close",
                "DNT": "1",
            }
            if not headers
            else headers
        )
        if "http" not in url:
            url = "http://" + url
        self.url = url

    def fetch(self) -> None:
        try:
            r = requests.get(self.url, headers=self.headers)
        except ConnectionError:
            self.is_invalid = True
            return

        r.encoding = "utf-8"
        page = MetadataParser(html=r.text)

        self.title = page.get_metadata("title")
        self.description = page.get_metadata("description")
        self.image = page.get_metadata("image")
