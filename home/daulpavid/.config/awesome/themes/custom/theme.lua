local theme_assets = require("beautiful.theme_assets")
local xresources = require("beautiful.xresources")
local gears = require("gears")

local apply_dpi = xresources.apply_dpi

local theme = {}

-- Theme settings and colors
theme.dir = os.getenv("HOME") .. "/.config/awesome/themes/daul-dark"

theme.font          = "Terminus 9"
theme.wallpaper     = theme.dir .. "/wallpaper/background_0.png"

theme.bg_normal     = "#4c4b4b"
theme.bg_focus      = "#5e5e5e"
theme.bg_urgent     = "#353535"
theme.bg_minimize   = "#2d2d2d"
theme.bg_systray    = theme.bg_normal

theme.fg_normal     = "#9c9c9c"
theme.fg_focus      = "#eeeeee"
theme.fg_urgent     = "#ef8f8f"
theme.fg_minimize   = "#eeeeee"

theme.border_width  = apply_dpi(2)
theme.border_normal = "#3a3a3a"
theme.border_focus  = "#4c4c4c"
theme.border_marked = "#592020"

-- Generate Awesome icon:
theme.awesome_icon = theme_assets.awesome_icon(
    theme.menu_height, theme.bg_focus, theme.fg_focus
)

-- Define the icon theme for application icons. If not set then the icons
-- from /usr/share/icons and /usr/share/icons/hicolor will be used.
theme.icon_theme = nil

return theme
