"""Weather

Displays the weather where you are.
"""

___name___         = "Weather"
___license___      = "MIT"
___dependencies___ = ["ugfx_helper"]
___categories___   = ["Homescreens"]
___bootstrapped___ = True # Whether or not apps get downloaded on first install. Defaults to "False", mostly likely you won't have to use this at all.


import ugfx_helper, ugfx, app
from tilda import Buttons
# import weather


ugfx_helper.init()
ugfx.clear(ugfx.BLACK)

ugfx.text(5, 5, "Hi Alan!", ugfx.WHITE)

Buttons.enable_interrupt(Buttons.BTN_B, lambda button_id: app.restart_to_default(), on_press=True, on_release=False)

while True:
    sleep.wfi()

ugfx.clear()
app.restart_to_default()
