[app]
title = Mp3Quran Tarateel
package.name = mp3quran_tarateel
package.domain = org.janradio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0

# Android
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,WAKE_LOCK
android.accept_sdk_license = True

# Buildozer/p4a
p4a.bootstrap = sdl2
p4a.branch = master

# Optional app icon: place icon.png in assets/ and uncomment the next line.
# icon.filename = %(source.dir)s/assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
