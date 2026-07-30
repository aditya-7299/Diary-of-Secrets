label start:
    "The city is waiting."
    jump map_loop

# --- The Main Hub ---
label map_loop:
    # 1. Turn our custom UI on!
    $ hud_enabled = True
    $ quick_menu = False 
    
    call screen city_map
    $ location = _return
    
    # 2. Turn the custom UI off so it doesn't show over story screens!
    $ hud_enabled = False
    
    # 3. Route the player based on their choice
    if location == "home":
        jump home_event
        
    elif location == "office":
        jump office_event
        
    else:
        # 4. The Catch-All for unfinished locations
        scene black
        
        # 'centered' is a special Ren'Py character that puts text in the middle of the screen
        centered "{size=50}This location is coming soon.{/size}"
        
        # Once the player clicks, bounce them right back to the map
        jump map_loop

# --- Story Arcs ---

label home_event:
    # 1. Show the exterior of the house based on the time of day
    if time_of_day == "Morning":
        scene expression "images/backgrounds/house_morning.jpg"
    elif time_of_day == "Afternoon":
        scene expression "images/backgrounds/house_afternoon.jpg"
    else:
        # Fallback to evening for both Evening and Night
        scene expression "images/backgrounds/house_evening.jpg"
        
    "It feels good to be back home."
    
    # 2. Smoothly transition inside
    scene expression "images/backgrounds/home_1st_floor.jpg" with dissolve
    "The first floor is pretty quiet."
    
    # 3. Head upstairs
    scene expression "images/backgrounds/home_second_floor_top.jpg" with dissolve
    "Time to head to my room and get some rest."
    
    # 4. Advance the time of day and return to the map
    $ advance_time()
    jump map_loop
    
    
label office_event:
    # 1. Show the exterior of the office based on time of day
    if time_of_day == "Morning" or time_of_day == "Afternoon":
        scene expression "images/backgrounds/office_outdoor_morning.jpg"
    elif time_of_day == "Evening":
        scene expression "images/backgrounds/office_outdoor_evening.jpg"
    else:
        scene expression "images/backgrounds/office_outdoor_night.jpg"
        
    "The corporate grind never sleeps."
    
    # 2. Transition inside to the work floor
    scene expression "images/backgrounds/office_top.jpg" with dissolve
    "Looks like everyone is already busy at their desks."
    
    # 3. A quick washroom event
    "I should probably freshen up before my first meeting."
    scene expression "images/backgrounds/office_washroom.jpg" with dissolve
    "Perfect. Let's get to work."
    
    # 4. Advance the time of day and return to the map
    $ advance_time()
    jump map_loop