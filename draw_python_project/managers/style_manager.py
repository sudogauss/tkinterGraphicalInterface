class StyleManager:

    style_menu = None

    @classmethod
    def set_style_menu(cls, style_menu):
        cls.style_menu = style_menu

    @classmethod
    def get_fill_color(cls):
        return cls.style_menu.fill_colors.get()

    @classmethod
    def get_outline_color(cls):
        return cls.style_menu.outline_colors.get()
