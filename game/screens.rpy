# Main Menu

screen main_menu():

    tag menu

    # Background
    add Solid("#171520")

    # Menu contents on the left
    vbox:
        xalign 0.05
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


# Button styles

style custom_menu_button is button:
    xminimum 200
    padding (12, 8)

style custom_menu_button_text is button_text:
    size 28
    color "#cccccc"
    hover_color "#ffffff"
