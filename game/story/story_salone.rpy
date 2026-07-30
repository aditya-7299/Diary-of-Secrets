label salone_story:

    $ current_character = "salone"
    $ ui_theme = "salone"

    call hud_enable from _call_hud_enable_2

    scene black
    with fade

    centered "{size=60}SALONE{/size}"

    pause 1.0

    scene bg house_morning
    with dissolve

    s "Welcome to Salone's story."

    "Coming Soon."

    return