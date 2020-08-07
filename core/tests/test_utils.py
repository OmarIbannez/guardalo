from typing import Dict, AnyStr, Optional


class MockResponse:
    def __init__(
        self, data: Optional[Dict] = None, status_code: int = 200, text: AnyStr = ""
    ) -> None:
        self.data = data if data else {}
        self.status_code = status_code
        self.text = text

    def json(self) -> Dict:
        return self.data
