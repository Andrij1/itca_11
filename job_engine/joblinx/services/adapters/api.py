from .base import JobDTO


class APIAdapter:

    def fetch(self, data):

        jobs = []

        if isinstance(data, list):
            for j in data:
                jobs.append(JobDTO(
                    title=j.get("title"),
                    link=j.get("link"),
                    mode=j.get("mode"),
                    location=j.get("location"),
                ))

        elif isinstance(data, dict):
            for j in data.get("jobs", []) or data.get("results", []):
                jobs.append(JobDTO(
                    title=j.get("title"),
                    link=j.get("link"),
                    mode=j.get("mode"),
                    location=j.get("location"),
                ))

        return jobs