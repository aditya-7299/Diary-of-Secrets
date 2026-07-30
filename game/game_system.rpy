init python:
    def advance_time():
        global time_of_day, current_day
        
        if time_of_day == "Morning":
            time_of_day = "Afternoon"
        elif time_of_day == "Afternoon":
            time_of_day = "Evening"
        elif time_of_day == "Evening":
            time_of_day = "Night"
        else:
            time_of_day = "Morning"
            current_day += 1

# Force top bar icons to a strict 45x45 box
transform hud_icon_scale:
    xysize (45, 45)
    fit "contain"

# Force side toolbar icons to a strict 60x60 box
transform side_toolbar_icon:
    xysize (60, 60)
    fit "contain"
    on hover:
        alpha 0.8
    on idle:
        alpha 1.0

label coming_soon_location:
    scene black
    hide screen main_hud
    
    # Displays a centered message on the black screen, waiting for a click
    centered "{size=50}This location is coming soon.{/size}"
    
    # Return immediately back from wherever this was called
    return

# Force side toolbar icons to a strict 60x60 box with a flowing hover animation
transform side_toolbar_icon:
    # Keep the strict size to prevent breaking your layout
    xysize (60, 60)
    fit "contain"
    
    on idle:
        # Smoothly ease back to its original state when the mouse leaves
        easein 0.3 zoom 1.0 yoffset 0 alpha 1.0
        
    on hover:
        # 1. Initial quick pop and highlight when the mouse touches it
        easein 0.2 zoom 1.1 alpha 1.0
        
        # 2. The continuous "flow" loop
        block:
            # Gently float up
            ease 1.2 yoffset -5
            # Gently float back down
            ease 1.2 yoffset 0
            # Loop this block forever as long as the mouse stays hovered
            repeat

