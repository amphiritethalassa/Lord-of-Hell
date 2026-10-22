
# Placeholder dialogue screen for a 1280x720 visual novel.

screen say(who, what):

    window:
        id "window"

        xalign 0.5
        yalign 1.0
        xsize 1180
        ysize 180

        background Solid("#202030")

        padding (35, 25)

        vbox:
            spacing 10

            if who is not None:
                text who:
                    id "who"
                    size 28
                    color "#ffb7d5"

            text what:
                id "what"
                size 24
                color "#ffffff"
                xmaximum 1110
                ymaximum 115
