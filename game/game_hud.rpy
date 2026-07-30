screen main_hud():
    zorder 100
    
    # Top Information Bar
    frame:
        xfill True
        ysize 64
        yalign 0.0
        padding (20, 10, 20, 10)
        
        hbox:
            xfill True
            yalign 0.5
            
            # Left side: Time Info
            hbox:
                spacing 20
                yalign 0.5
                add "images/ui/[ui_theme]/time_icon_[ui_theme].png" at hud_icon_scale
                text "Day [current_day] - [time_of_day]" size 40 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]
            
            # Right side: Stats
            hbox:
                spacing 30
                xalign 1.0
                yalign 0.5
                
                # Money
                hbox:
                    spacing 8
                    add "images/ui/[ui_theme]/money_icon_[ui_theme].png" at hud_icon_scale
                    text str(money) size 40 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]
                
                # Love
                hbox:
                    spacing 8
                    add "images/ui/[ui_theme]/love_icon_[ui_theme].png" at hud_icon_scale
                    text str(love_stat) size 40 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]
                    
                # Lust
                hbox:
                    spacing 8
                    add "images/ui/[ui_theme]/lust_icon_[ui_theme].png" at hud_icon_scale
                    text str(lust_stat) size 40 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]
                    
                # Adult
                hbox:
                    spacing 8
                    add "images/ui/[ui_theme]/adult_icon_[ui_theme].png" at hud_icon_scale
                    text str(adult_stat) size 40 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]

    # Left Side Toolbar
    frame:
        yalign 0.5
        xalign 0.0
        padding (10, 20, 10, 20)
        
        vbox:
            spacing 15
            
            imagebutton:
                idle "images/ui/[ui_theme]/menu_icon_[ui_theme].png"
                action ShowMenu("save")
                at side_toolbar_icon
            
            imagebutton:
                idle "images/ui/[ui_theme]/save_icon_[ui_theme].png"
                action ShowMenu("save")
                at side_toolbar_icon
                
            imagebutton:
                idle "images/ui/[ui_theme]/load_icon_[ui_theme].png"
                action ShowMenu("load")
                at side_toolbar_icon
                
            imagebutton:
                idle "images/ui/[ui_theme]/quest_icon_[ui_theme].png"
                action NullAction() 
                at side_toolbar_icon
                
            imagebutton:
                idle "images/ui/[ui_theme]/relations_icon_[ui_theme].png"
                action NullAction() 
                at side_toolbar_icon
                
            imagebutton:
                idle "images/ui/[ui_theme]/settings_icon_[ui_theme].png"
                action ShowMenu("preferences")
                at side_toolbar_icon

    # Bottom Docked Quest Tracker
    if q_manager.get_active_quest():
        frame:
            xalign 0.5
            yalign 0.98
            padding (20, 10, 20, 10)
            
            hbox:
                spacing 15
                add "images/ui/[ui_theme]/quest_icon_[ui_theme].png" at hud_icon_scale
                text "Active Objective: " + q_manager.get_active_quest()['description'] size 36 yalign 0.5 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]