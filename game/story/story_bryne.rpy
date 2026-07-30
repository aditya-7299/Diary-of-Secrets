label bryne_story:

    $ current_character = "bryne"
    $ ui_theme = "bryne"

    call hud_enable from _call_hud_enable

    scene black
    with fade

    centered "{size=60}BRYNE{/size}"

    pause 1.0

    scene black
    with dissolve

    b "Welcome to Bryne's story."

    "Coming Soon."

    return