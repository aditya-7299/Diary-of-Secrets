screen city_map():
    add "images/backgrounds/map_[time_of_day.lower()].jpg"
    
    grid 5 3:
        align (0.5, 0.5) 
        xspacing 20 
        yspacing 20
        
        # --- ROW 1 ---
        button:
            background None
            action Return("beach") 
            add "images/location_icons/beach.png" zoom 0.75
            
        button:
            background None
            action Return("cafe") 
            add "images/location_icons/cafe.png" zoom 0.75
            
        button:
            background None
            action Return("cinema") 
            add "images/location_icons/cinema.png" zoom 0.75
            
        button:
            background None
            action Return("gym") 
            add "images/location_icons/gym.png" zoom 0.75
            
        button:
            background None
            action Return("home") 
            add "images/location_icons/home.png" zoom 0.75
        
        # --- ROW 2 ---
        button:
            background None
            action Return("hospital") 
            add "images/location_icons/hospital.png" zoom 0.75
            
        button:
            background None
            action Return("hotel") 
            add "images/location_icons/hotel.png" zoom 0.75
            
        button:
            background None
            action Return("neighbor") 
            add "images/location_icons/neighbor.png" zoom 0.75
            
        button:
            background None
            action Return("nightclub") 
            add "images/location_icons/nightclub.png" zoom 0.75
            
        button:
            background None
            action Return("office") 
            add "images/location_icons/office.png" zoom 0.75
        
        # --- ROW 3 ---
        button:
            background None
            action Return("park") 
            add "images/location_icons/park.png" zoom 0.75
            
        button:
            background None
            action Return("police") 
            add "images/location_icons/police.png" zoom 0.75
            
        button:
            background None
            action Return("shopping") 
            add "images/location_icons/shopping.png" zoom 0.75
            
        button:
            background None
            action Return("studio") 
            add "images/location_icons/studio.png" zoom 0.75
            
        button:
            background None
            action Return("university") 
            add "images/location_icons/university.png" zoom 0.75

    use top_hud
    use bottom_hud