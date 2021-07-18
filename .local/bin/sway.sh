export QT_QPA_PLATFORM=wayland-egl
export QT_WAYLAND_FORCE_DPI=physical
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1

export ECORE_EVAS_ENGINE=wayland_egl
export ELM_ENGINE=wayland_egl

export SDL_VIDEODRIVER=wayland

export _JAVA_AWT_WM_NONREPARENTING=1

export MOZ_ENABLE_WAYLAND=1

/usr/bin/sway $@ 2> /tmp/sway.log
