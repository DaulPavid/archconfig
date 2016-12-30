from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Screen

wmname = 'qtile'
mod = 'mod4'

colors = {'frame': '#000000',
          'frame_focus': '#ffffff',
          'background': '#000000',
          'widget_frame': '#e0e0e0',
          'text': '#990000',
          'text_inactive': '#800000',
          'text_alert': '#808080'}

# Key bindings
keys = [
    # Window manager controls
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'r', lazy.spawncmd()),
    Key([mod], 'v', lazy.spawn('gvim')),
    Key([mod], 'Return', lazy.spawn('urxvt')),
    Key([mod], 'w',      lazy.window.kill()),

    Key([mod], 'Tab', lazy.layout.next()),
    Key([mod], 'Left', lazy.screen.prevgroup()),
    Key([mod], 'Right', lazy.screen.nextgroup()),

    # Layout modification
    Key([mod], 'f', lazy.window.toggle_fullscreen()),
    Key([mod], 'n', lazy.window.toggle_minimize()),

    # Switch between windows in current stack pane
    Key([mod], 'k', lazy.layout.down()),
    Key([mod], 'j', lazy.layout.up()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod], 'h', lazy.layout.left()),

    # Move windows up or down in current stack
    Key([mod, 'control'], 'k', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'j', lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], 'space', lazy.layout.next()),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout()),

    # Lock the screen
    Key([mod, 'control'], 'l', lazy.spawn('xlock')),
    Key([], 'XF86Launch1', lazy.spawn('xlock')),

    # Control volume
    Key([], 'XF86AudioMute', lazy.spawn('amixer -D pulse set Master toggle')),
    Key([], 'XF86AudioMicMute', lazy.spawn('amixer -D pulse set Master toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -c 0 -q set Master 2dB+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -c 0 -q set Master 2dB-')),
]

# Mouse bindings and options
mouse = (
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
)

bring_front_click = True
cursor_warp = False
follow_mouse_focus = True

# Groups
groups = [
    Group('1'),
    Group('2'),
    Group('3'),
    Group('4'),
    Group('5'),
]
for i in groups:
    # mod + letter of group = switch to group
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))

    # mod + shift + letter of group = switch to & move focused window to group
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))

dgroups_key_binder = None
dgroups_app_rules = []

# Layouts
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2,border_focus=colors['frame_focus']),
    layout.Tile(border_focus=colors['frame_focus']),
    layout.Matrix(border_focus=colors['frame_focus'])
]

# Screens and widget options
screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.GroupBox(
                    borderwidth=1,
                    inactive=colors['text_inactive'],
                    active=colors['text'],
                    this_current_screen_border=colors['text'],
                    urgent_text=colors['text_alert'],
                ),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.TaskList(
                    border=colors['text'],
                    max_title_width=500,
                    urgent_border=colors['text_alert']
                ),
                widget.CPUGraph(
                    graph_color=colors['text'],
                    border_color=colors['frame'],
                    samples=50
                ),
                widget.NetGraph(
                    graph_color=colors['text'],
                    border_color=colors['frame'],
                    samples=50
                ),
                widget.Volume(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %H:%M %p'),
            ],
            size=20,
            background=colors['background'],
        ),
    ),
]

widget_defaults = dict(
    font='DejaVu Sans Mono',
    fontsize=10,
)

auto_fullscreen = True
