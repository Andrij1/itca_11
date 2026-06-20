import xml.etree.ElementTree as ET
from .base import JobDTO


class RSSAdapter:

    def fetch(self, response_text: str):

        root = ET.fromstring(response_text)

        jobs = []

        for item in root.findall(".//item") or root.findall(".//entry"):

            title = item.findtext("title")
            link = item.findtext("link")

            if title and link:
                jobs.append(JobDTO(title=title.strip(), link=link.strip()))

        return jobs