# Mp3Quran Tarateel — Android Radio App

A simple Android radio app for **Mp3Quran Tarateel**.

## Stream

The app uses this direct MP3 stream:

`https://qurango.net/radio/tarateel`

The Telegradio listing identifies Mp3Quran Tarateel as a Saudi Arabia internet radio station with 128 kbps MP3 quality.

## Features

- Play
- Pause
- Stop
- Internet streaming
- Android APK build through GitHub Actions
- Kivy + PyJNIus
- No account or API key required

## Build APK on GitHub

1. Create a new GitHub repository.
2. Upload all files from this project.
3. Commit/push to `main` or `master`.
4. Open the repository's **Actions** tab.
5. Run **Build Android APK** manually, or push a commit.
6. When the workflow finishes, open the workflow run.
7. Download the artifact named **mp3quran-tarateel-apk**.

## Local build

On Linux:

```bash
pip install buildozer
buildozer android debug
```

The generated APK will be placed in the `bin/` directory.

## Important

The radio stream is an external service. If its URL, availability, bitrate, or access policy changes, the app may need an update.

## Credits / source

Radio listing:
https://telegradio.com/radio/saudi-arabia/mp3quran-tarateel

Direct stream currently used:
https://qurango.net/radio/tarateel
