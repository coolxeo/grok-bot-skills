> **Pro version:** this free skill works by itself. The kit adds eased pan and zoom, a loudness check and a jitter check. **[Get the kit →](https://daniacostaai.gumroad.com/l/ommvol)**

This is the free `shorts-reframe` skill. The instructions are in [SKILL.md](SKILL.md).

## Inspired by

Inspired by the [FFmpeg crop filter docs](https://ffmpeg.org/ffmpeg-filters.html#crop) (`crop=w:h:x:y`, `ih`/`iw`, and centered defaults) and the [mediacodec.dev crop guide](https://mediacodec.dev/how-to/crop-video/) (`crop=ih*9/16:ih` with `-c:a copy`). The official docs are a filter reference, not a 16:9-to-9:16 recipe; the guide has the centered crop but not a scale to 1080x1920 or duration and resolution checks. This skill adds the complete command and those two checks.

> Built and used for my YouTube Shorts. Want it wired up and ready to go? [The full kit is here.](https://daniacostaai.gumroad.com/l/ommvol)
