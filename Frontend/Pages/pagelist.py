import page

class Pagelist(page.Page):
    def __init__(self, page_type, title, content):
        super().__init__(page_type, title)
        self.index = 0
        self.offset = 0

    # OVERRIDE
    def on_select():
        pass

    def get_content():
        pass
