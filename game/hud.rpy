screen top_hud():
    if hud_enabled:
        # Staple the gradient directly to the top of the screen
        add "images/ui/top_gradient.png":
            yalign 0.0
            xalign 0.5
            
        hbox:
            xalign 0.5 
            yalign 0.0
            yoffset 15 # Pushes text down slightly from the very top
            spacing 90 
            
            # 1. TIME
            hbox:
                spacing 10
                add "images/ui/time_icon.png" zoom 0.15 yalign 0.5
                text "TIME" font "gui/fonts/cambria.ttf" color "#ff66b2" size 22 bold True yalign 0.5 outlines [(1, "#4d001f", 0, 0)]
                
            # 2. MONEY
            hbox:
                spacing 10
                add "images/ui/money_icon.png" zoom 0.15 yalign 0.5
                text "MONEY" font "gui/fonts/cambria.ttf" color "#ff66b2" size 22 bold True yalign 0.5 outlines [(1, "#4d001f", 0, 0)]

            # 3. MOBILE
            hbox:
                spacing 10
                add "images/ui/mobile_icon.png" zoom 0.15 yalign 0.5
                text "JOURNAL" font "gui/fonts/cambria.ttf" color "#ff66b2" size 22 bold True yalign 0.5 outlines [(1, "#4d001f", 0, 0)]

screen bottom_hud():
    if hud_enabled:
        # The pill-shaped background graphic
        add "images/ui/bottom_gradient.png":
            yalign 1.0
            xalign 0.5
            
        hbox:
            xalign 0.5 
            yalign 1.0
            yoffset -2 # Lifts the row higher to vertically center it inside the pill
            spacing 80 # Tightens the gap so the buttons don't spill off the edges
            
            # BACK
            button:
                background None
                action Rollback()
                vbox:
                    xalign 0.5
                    spacing 2 # Adds a tiny gap between the icon and text
                    add "images/ui/back_icon.png" zoom 0.12 xalign 0.5
                    text "BACK" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5
                    
            # SKIP
            button:
                background None
                action Skip() alternate Skip(fast=True, confirm=True)
                vbox:
                    xalign 0.5
                    spacing 2
                    add "images/ui/skip_icon.png" zoom 0.12 xalign 0.5
                    text "SKIP" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5
                    
            # MENU
            button:
                background None
                action ShowMenu()
                vbox:
                    xalign 0.5
                    spacing 2
                    add "images/ui/menu_icon.png" zoom 0.12 xalign 0.5
                    text "MENU" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5
                    
            # SETTINGS
            button:
                background None
                action ShowMenu('preferences')
                vbox:
                    xalign 0.5
                    spacing 2
                    add "images/ui/settings_icon.png" zoom 0.12 xalign 0.5
                    text "SETTINGS" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5
                    
            # SAVE
            button:
                background None
                action ShowMenu('save')
                vbox:
                    xalign 0.5
                    spacing 2
                    add "images/ui/save_icon.png" zoom 0.12 xalign 0.5
                    text "SAVE" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5
                    
            # LOAD
            button:
                background None
                action ShowMenu('load')
                vbox:
                    xalign 0.5
                    spacing 2
                    add "images/ui/load_icon.png" zoom 0.12 xalign 0.5
                    text "LOAD" font "gui/fonts/cambria.ttf" size 16 color "#ff66b2" xalign 0.5