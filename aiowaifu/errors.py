class EndpointError(Exception):
    def __init__(self, type, category):
        self.type = type
        self.category = category

    def __str__(self) -> str:
        return f'Endpoint with "{self.type}" type or "{self.category}" category not found.\nget endpoints from https://waifu.pics/docs'
