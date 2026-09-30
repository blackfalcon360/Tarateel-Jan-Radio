from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

STREAM_URL = "https://qurango.net/radio/tarateel"

class RadioApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = None
        self.prepared = False

    def build(self):
        Window.clearcolor = (0.06, 0.07, 0.09, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=28,
            spacing=18
        )

        title = Label(
            text="Mp3Quran Tarateel",
            font_size="30sp",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=65
        )

        country = Label(
            text="🇸🇦 Saudi Arabia • Quran Radio",
            font_size="17sp",
            color=(0.75, 0.85, 0.78, 1),
            size_hint_y=None,
            height=45
        )

        self.status = Label(
            text="Ready — press PLAY",
            font_size="18sp",
            color=(0.85, 0.85, 0.85, 1)
        )

        play = Button(
            text="▶  PLAY",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=70
        )
        play.bind(on_release=self.play_radio)

        pause = Button(
            text="⏸  PAUSE",
            font_size="20sp",
            size_hint_y=None,
            height=65
        )
        pause.bind(on_release=self.pause_radio)

        stop = Button(
            text="■  STOP",
            font_size="20sp",
            size_hint_y=None,
            height=65
        )
        stop.bind(on_release=self.stop_radio)

        layout.add_widget(title)
        layout.add_widget(country)
        layout.add_widget(self.status)
        layout.add_widget(play)
        layout.add_widget(pause)
        layout.add_widget(stop)

        return layout

    def on_start(self):
        if platform == "android":
            try:
                from android.permissions import request_permissions, Permission
                request_permissions([Permission.INTERNET])
            except Exception:
                pass

    def create_player(self):
        from jnius import autoclass, PythonJavaClass, java_method

        MediaPlayer = autoclass("android.media.MediaPlayer")
        self.player = MediaPlayer()

        class PreparedListener(PythonJavaClass):
            __javainterfaces__ = ["android/media/MediaPlayer$OnPreparedListener"]
            @java_method("(Landroid/media/MediaPlayer;)V")
            def onPrepared(self, mp):
                self.prepared = True
                self.status.text = "Playing — Mp3Quran Tarateel"
                mp.start()

        class ErrorListener(PythonJavaClass):
            __javainterfaces__ = ["android/media/MediaPlayer$OnErrorListener"]
            @java_method("(Landroid/media/MediaPlayer;II)Z")
            def onError(self, mp, what, extra):
                self.status.text = "Stream error — please try again"
                return True

        self.prepared_listener = PreparedListener()
        self.error_listener = ErrorListener()

        self.player.setOnPreparedListener(self.prepared_listener)
        self.player.setOnErrorListener(self.error_listener)
        self.player.setDataSource(STREAM_URL)
        self.status.text = "Connecting…"
        self.player.prepareAsync()

    def play_radio(self, *_):
        if platform != "android":
            self.status.text = "Android APK required for radio playback"
            return

        try:
            if self.player is None:
                self.create_player()
            elif self.prepared and not self.player.isPlaying():
                self.player.start()
                self.status.text = "Playing — Mp3Quran Tarateel"
        except Exception as e:
            self.status.text = "Unable to start stream"

    def pause_radio(self, *_):
        try:
            if self.player and self.prepared and self.player.isPlaying():
                self.player.pause()
                self.status.text = "Paused"
        except Exception:
            pass

    def stop_radio(self, *_):
        try:
            if self.player:
                self.player.stop()
                self.player.release()
        except Exception:
            pass
        self.player = None
        self.prepared = False
        self.status.text = "Stopped — press PLAY"

    def on_pause(self):
        # Keep the Android activity alive when possible.
        return True

    def on_stop(self):
        try:
            if self.player:
                self.player.stop()
                self.player.release()
                self.player = None
        except Exception:
            pass

if __name__ == "__main__":
    RadioApp().run()
