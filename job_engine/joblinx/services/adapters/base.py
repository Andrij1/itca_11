class BaseAdapter:
    def fetch(self, url: str):
        raise NotImplementedError


class JobDTO:
    def __init__(self, title, link, mode=None, location=None):
        self.title = self._clean(title)
        self.link = link
        self.mode = mode
        self.location = location

    def _clean(self, title):
        if not title:
            return ""

        title = str(title).strip()

        # prevent HTML injection / nav pollution
        if "<html" in title.lower() or "doctype" in title.lower():
            return ""

        if title.startswith("http") or title.startswith("/"):
            return ""

        return title