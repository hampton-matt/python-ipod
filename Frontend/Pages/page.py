PAGE_LIST = 0
PAGE_NOW_PLAYING = 1

class Page:
    def __init__(self, page_type, title):
        self.page_type = page_type
        self.title = title

    # NAVIGATION EVENTS
    # Always return page item - None if not needed to render page
    # On Menu handled by page stack
    def on_select():
        return None

    def on_next():
        # Skip Song
        return None

    def on_prev():
        # Previous Song
        return None

    def on_play():
        return None

    # Returns list of items to display
    def on_down():
        pass

    def on_up():
        pass
