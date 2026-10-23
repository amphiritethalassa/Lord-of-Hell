
# ============================================
# MAIN MENU
# ============================================

screen main_menu():

    tag menu

    add Solid("#171520")

    vbox:
        xalign 0.95
        yalign 0.5
        spacing 18

        text "My Visual Novel":
            size 42
            color "#ffffff"

        textbutton "Start":
            style "custom_menu_button"
            text_style "custom_menu_button_text"
            action Start()

        textbutton "Load":
            style "custom_menu_button"
            text_style "custom_menu_button_text"
            action ShowMenu("load")

        textbutton "Preferences":
            style "custom_menu_button"
            text_style "custom_menu_button_text"
            action ShowMenu("preferences")

        textbutton "Quit":
            style "custom_menu_button"
            text_style "custom_menu_button_text"
            action Quit(confirm=False)


# ============================================
# MAIN MENU BUTTON STYLES
# ============================================

style custom_menu_button is button:
    xminimum 200
    padding (12, 8)

style custom_menu_button_text is button_text:
    size 28
    color "#cccccc"
    hover_color "#ffffff"


# ============================================
# QUICK MENU OVERLAY
# ============================================

init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")


# ============================================
# QUICK MENU
# Auto | Skip | Hide | History | Settings
# Positioned along the bottom of the textbox
# ============================================

screen quick_menu():

    zorder 100

    hbox:
        xalign 0.98
        yalign 0.97
        spacing 12

        textbutton _("Auto"):
            style "quick_button"
            text_style "quick_button_text"
            action Preference("auto-forward", "toggle")
            selected preferences.afm_enable

        textbutton _("Skip"):
            style "quick_button"
            text_style "quick_button_text"
            action Preference("begin skipping")

        textbutton _("Hide"):
            style "quick_button"
            text_style "quick_button_text"
            action HideInterface()

        textbutton _("History"):
            style "quick_button"
            text_style "quick_button_text"
            action ShowMenu("history")

        textbutton _("Settings"):
            style "quick_button"
            text_style "quick_button_text"
            action ShowMenu("preferences")


# ============================================
# QUICK MENU BUTTON STYLES
# ============================================

style quick_button:
    background None
    foreground None
    xpadding 8
    ypadding 5

style quick_button_text:
    size 18
    color "#ffffff"
    hover_color "#c9b7ff"
    selected_color "#c9b7ff"
    outlines [(2, "#00000099", 0, 0)]


# ============================================
# CHARACTER POSITIONS AND TRANSITIONS
#
# t = normal appearance
# h = hop when appearing
# All transforms use zoom 0.65.
# All transforms fade out when hidden.
# ============================================

# ONE-POSITION LAYOUT

transform t11:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h11:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0


# ============================================
# TWO-POSITION LAYOUT
# ============================================

transform t21:
    xalign 0.25
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h21:
    xalign 0.25
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t22:
    xalign 0.75
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h22:
    xalign 0.75
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0


# ============================================
# THREE-POSITION LAYOUT
# ============================================

transform t31:
    xalign 0.16
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h31:
    xalign 0.16
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t32:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h32:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t33:
    xalign 0.84
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h33:
    xalign 0.84
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0


# ============================================
# FOUR-POSITION LAYOUT
# ============================================

transform t41:
    xalign 0.12
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h41:
    xalign 0.12
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t42:
    xalign 0.37
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h42:
    xalign 0.37
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t43:
    xalign 0.63
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h43:
    xalign 0.63
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t44:
    xalign 0.88
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h44:
    xalign 0.88
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0


# ============================================
# FIVE-POSITION LAYOUT
# ============================================

transform t51:
    xalign 0.10
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h51:
    xalign 0.10
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t52:
    xalign 0.30
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h52:
    xalign 0.30
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t53:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h53:
    xalign 0.50
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t54:
    xalign 0.70
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h54:
    xalign 0.70
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0

transform t55:
    xalign 0.90
    yalign 1.0
    zoom 0.65
    on hide:
        linear 0.20 alpha 0.0

transform h55:
    xalign 0.90
    yalign 1.0
    zoom 0.65
    on show:
        yoffset 0
        easeout 0.12 yoffset -35
        easein 0.12 yoffset 0
    on hide:
        linear 0.20 alpha 0.0
