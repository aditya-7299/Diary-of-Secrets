label merlyn_story:

    $ current_character = "merlyn"
    $ ui_theme = "merlyn"

    call hud_enable from _call_hud_enable_1

    scene black
    with fade

    centered "{size=60}MERLYN{/size}"

    pause 1.0

    scene black
    with dissolve

    m "Welcome to Merlyn's story."

    "Coming Soon."

    return