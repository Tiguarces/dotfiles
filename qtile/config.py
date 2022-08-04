from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
import os
import subprocess
from libqtile import hook

mod = "mod1"
terminal = "kitty"
rofi = "rofi -modi drun,run -show drun -font 'DejaVu Sans 13' -show-icons"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([mod], "p", lazy.spawn(rofi), desc="Spawn Rofi")
]

groups = [
    Group(" Web ", matches=[Match( wm_class = "firefox" )]),
    Group(" Code ", matches=[Match( wm_class = "jetbrains-idea-ce" )]),
    Group(" Code2 ", matches=[Match( wm_class = "Code" )]),
    Group(" Code3 ", matches=[Match( wm_class = "postman" )]),
    Group(" Utils ", matches=[Match( wm_class = "Gammy" ), Match( wm_class = "pulseEffects" )])
]

layouts = [
        layout.MonadTall(
            margin = 15,
            border_focus = "#9ccfd8",
            border_normal = "#31748f",
        ),

        layout.Columns(
            border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=15
        ),
    
        layout.Max(),
]

widget_defaults = dict(
    font="Font Awesome",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#9c2c33", "#9c2c33"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#508aa1", "#508aa1"],
          ["#c678dd", "#c678dd"],
          ["#50a3a2", "#50a3a2"],
          ["#a9a1e1", "#a9a1e1"],
          ["#808080", "#808080"],
          ["#909abd", "#909abd"],
          ["#000000", "#000000"],
          ["#101020", "#101020"],
          ["#4c678c", "#4c678c"],
          ["#cf9852", "#cf9852"],
          ["#6c8296", "#6c8296"],
          ["#5a6da1", "#5a6da1"],
          ["#3c6b7a", "#3c6b7a"]]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = colors[6],
                    inactive = colors[10],
                    rounded = False,
                    this_current_screen_border = colors[8],
                    highlight_method = "line",
                ),
                
                widget.Prompt(),

                widget.Spacer(
                    bar.STRETCH
                ),
                
                widget.CPU(
                    format = "<span font='9'>   </span><span font='9'>{load_percent}% </span>",
                    background = colors[6]
                ),

                widget.Memory(
                    format = "<span font='10'>   </span><span font='9'>{MemUsed: .0f} {mm} </span>",
                    update_internal = 0.2,
                    background = colors[17]
                ),
               
                widget.Net(
                    format = "<span font='9'>{down} <span color='#36d18c'>↓↑</span> {up} </span>",
                    background = colors[18],
                ),

                widget.Clock(
                    format="<span font='9'>   </span><span font='9'>%Y-%m-%d I %H:%M</span>",
                    background = colors[14]
                ),

                widget.TextBox(
                    text = "<span font='10'>   </span><span font='9'>Debian</span>",
                    background = colors[6]
                )
            ],
            27,
            background = colors[13],
            margin = [10, 10, -5, 10],
            border_width = 1,
            border_color = colors[14]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = simple_key_binder("mod1")
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen(home + "/.fehbg")
