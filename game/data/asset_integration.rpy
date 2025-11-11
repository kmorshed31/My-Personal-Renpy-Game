# Side portraits (small versions). Add all moods you need.
image side m neutral = Transform("images/sprites/m_neutral.png", zoom=0.6)
image side m angry   = Transform("images/sprites/m_angry.png",   zoom=0.6)
image side m sad     = Transform("images/sprites/m_sad.png",     zoom=0.6)
image side m happy   = Transform("images/sprites/m_happy.png",   zoom=0.6)

image side a neutral = Transform("images/sprites/a_neutral.png", zoom=0.6)
image side a angry   = Transform("images/sprites/a_angry.png",   zoom=0.6)
image side a sad     = Transform("images/sprites/a_sad.png",     zoom=0.6)
image side a happy   = Transform("images/sprites/a_happy.png",   zoom=0.6)

image side me neutral = Transform("images/sprites/me_neutral.png", zoom=0.67034482758)
image side me angry   = Transform("images/sprites/me_angry.png",   zoom=0.67034482758)
image side me sad     = Transform("images/sprites/me_sad.png",     zoom=0.67034482758)
image side me happy   = Transform("images/sprites/me_happy.png",   zoom=0.67034482758)

image side mi neutral = Transform("images/sprites/mi_neutral.png", zoom=0.648)
image side mi angry   = Transform("images/sprites/mi_angry.png",   zoom=0.648)
image side mi sad     = Transform("images/sprites/mi_sad.png",     zoom=0.648)
image side mi happy   = Transform("images/sprites/mi_happy.png",   zoom=0.648)


image bg dining_room = Transform(
    "images/backgrounds/DiningTable.png",
    size=(config.screen_width, config.screen_height),
    fit="cover",          # fill window, crop excess if aspect differs
    xalign=0.8, yalign=0.8
)

image bg bedroom = Transform(
    "images/backgrounds/bedroom.png",
    size=(config.screen_width, config.screen_height),
    fit="cover",          # fill window, crop excess if aspect differs
    xalign=0.8, yalign=0.8
)

image bg bathroom = Transform(
    "images/backgrounds/bathroom.png",
    size=(config.screen_width, config.screen_height),
    fit="cover",          # fill window, crop excess if aspect differs
    xalign=0.8, yalign=0.8
)