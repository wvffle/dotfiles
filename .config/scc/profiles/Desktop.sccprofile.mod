{
    "_": "", 
    "buttons": {
        "A": {
            "action": "button(Keys.KEY_ENTER)"
        }, 
        "B": {
            "action": "button(Keys.KEY_ESC)"
        }, 
        "BACK": {
            "action": "mode(START, name('Lock screen', shell('loginctl lock-session')), RGRIP, name('Fix Audio', shell(' amixer -c 0 sset \"Auto-Mute Mode\" Enabled')), None)"
        }, 
        "C": {
            "action": "feedback(BOTH, 512.0, doubleclick(keyboard(), hold(turnoff(), menu('Default.menu')), 0.9))"
        }, 
        "CPADPRESS": {
            "action": "button(Keys.BTN_MOUSE)"
        }, 
        "LB": {
            "action": "button(Keys.KEY_LEFTCTRL)"
        }, 
        "LGRIP": {
            "action": "button(Keys.KEY_LEFTMETA)"
        }, 
        "RB": {
            "action": "mode(LB, name('Toggle SCC', button(Keys.KEY_LEFTALT) and button(Keys.KEY_LEFTSHIFT) and button(Keys.KEY_LEFTCTRL) and button(Keys.KEY_F12)), button(Keys.KEY_LEFTALT))"
        }, 
        "RPAD": {
            "action": "button(Keys.BTN_MOUSE)"
        }, 
        "START": {
            "action": "mode(BACK, name('Unlock Screen', shell('loginctl unlock-session')), button(Keys.KEY_LEFTSHIFT))"
        }, 
        "STICKPRESS": {
            "action": "radialmenu('test',RIGHT)"
        }, 
        "X": {
            "action": "button(Keys.KEY_SPACE)"
        }, 
        "Y": {
            "action": "button(Keys.KEY_TAB)"
        }
    }, 
    "cpad": {
        "action": "mouse()"
    }, 
    "gyro": {
        "action": "mode(RGRIP, sens(1.5, 1.5, 1.5, mouse(ROLL)), None)"
    }, 
    "is_template": false, 
    "menus": {
        "test": [{
            "action": "osd(1.0,1,'meh')", 
            "id": "item1", 
            "name": "meh"
        }]
    }, 
    "pad_left": {
        "action": "mode(RGRIP, feedback(LEFT, 884.0, sens(0.2, 0.2, circular(button(Keys.KEY_VOLUMEUP, Keys.KEY_VOLUMEDOWN)))), rotate(25.6, smooth(16, 0.75, 53, feedback(LEFT, 702, sens(0.0, 0.0, ball(0.003, circular(mouse(Rels.REL_WHEEL))))))))"
    }, 
    "pad_right": {
        "action": "mode(RGRIP, feedback(LEFT, 4047, sens(-0.5, -0.5, circular(mouse(Rels.REL_WHEEL, 1)))), smooth(8, 0.78, 11, feedback(RIGHT, 128, 1.0, sens(0.7, 0.7, ball(15.849, mouse())))))"
    }, 
    "stick": {
        "action": "dpad(1, mode(LGRIP, button(Keys.KEY_LEFTMETA) and button(Keys.KEY_Z), button(Keys.KEY_UP)), mode(LGRIP, shell('~/.local/bin/magnify'), button(Keys.KEY_DOWN)), mode(LGRIP, button(Keys.BTN_SIDE), button(Keys.KEY_LEFT)), mode(LGRIP, button(Keys.BTN_EXTRA), button(Keys.KEY_RIGHT)))"
    }, 
    "trigger_left": {
        "action": "feedback(LEFT, 4096, trigger(50, 255, button(Keys.BTN_RIGHT)))"
    }, 
    "trigger_right": {
        "action": "feedback(RIGHT, 4096, trigger(50, 255, button(Keys.BTN_MOUSE)))"
    }, 
    "version": 1.4
}