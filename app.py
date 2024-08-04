from fastapi import FastAPI


class App:
    def __init__(self, fast: FastAPI, *endpoints: list):
        self.name = "App"
        self.fast = fast
        self.initialize_endpoints(endpoints)

    def initialize_endpoints(self, endpoint_classes: list):
        for endpoint_class in endpoint_classes:
            self.fast.include_router(
                endpoint_class.router, tags=endpoint_class.tags
            )
