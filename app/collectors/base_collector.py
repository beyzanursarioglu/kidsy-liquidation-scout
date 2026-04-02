class BaseCollector:
    def collect(self):
        raise NotImplementedError("Each collector must implement collect()")