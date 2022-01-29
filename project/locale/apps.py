import time

from django.apps import AppConfig
from django.core.management import call_command


class ApiToolsConfig(AppConfig):
    name = "project.locale"

    def ready(self) -> None:
        print("Compiling translations ...")
        t = time.monotonic()
        call_command("compilemessages", "--verbosity=0")
        duration = time.monotonic() - t
        print(f"Done in {duration*1000:.0f} ms.\n")
