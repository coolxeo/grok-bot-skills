"""Tests for plan_page.py. Run: python3 -m pytest -q skills/video/video-plan-page/scripts"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import plan_page as pp  # noqa: E402

EXAMPLE = HERE.parent / "example"
SCRIPT = {
    "title": "Tiny Test",
    "quest": {"goal": "finish", "hooks": [{"text": "Hook one.", "checks": "MHB", "pick": True}, {"text": "No checks."}]},
    "lines": [
        {"who": "C", "text": "First line. | Second row.", "level": 0, "beat": "quest", "see": "A wide shot."},
        {"who": "S", "text": "give up.", "level": 1, "beat": "but"},
        {"who": "C", "text": "Last line.", "see": "A close-up.", "hud": "DAY 2"},
    ],
}


def _write(d, name, obj):
    p = d / name
    p.write_text(json.dumps(obj), encoding="utf-8")
    return p


def test_untimed_lines_get_increasing_times_and_input_is_untouched():
    lines = pp.timed(SCRIPT["lines"])
    assert [l["t"] for l in lines] == sorted(l["t"] for l in lines)
    assert all(l["dur"] >= pp.MIN_LINE_S for l in lines)
    assert "t" not in SCRIPT["lines"][0]


def test_given_times_win_and_zero_duration_is_kept():
    lines = pp.timed([{"text": "a", "t": 3.0, "dur": 5.0}, {"text": "b", "dur": 0}])
    assert lines[1]["t"] == 8.0 and lines[1]["dur"] == 0


def test_page_is_a_real_document_with_viewport(tmp_path):
    page = pp.build(SCRIPT, {}, tmp_path)
    assert page.startswith("<!doctype html>")
    assert 'name="viewport"' in page and 'charset="utf-8"' in page
    assert "/*DATA*/" not in page and "/*TITLE*/" not in page
    assert "<title>Tiny Test</title>" in page


def test_script_text_cannot_break_out_of_the_script_tag(tmp_path):
    page = pp.build({**SCRIPT, "title": "x</script><!--<b>"}, {}, tmp_path)
    body = page.split("<script>", 1)[1]
    assert "</script><!--" not in body.split("</script>")[0]
    assert "<title>x&lt;/script&gt;&lt;!--&lt;b&gt;</title>" in page


def test_keys_attach_by_shot_id(tmp_path):
    from PIL import Image
    Image.new("RGB", (40, 20), "purple").save(tmp_path / "k.png")
    lines = pp.attach_keys(pp.timed(SCRIPT["lines"]), {"S02": "k.png"}, tmp_path)
    assert "key" not in lines[0] and lines[2]["key"].startswith("data:image/jpeg;base64,")


def test_missing_image_warns_and_still_builds(tmp_path, capsys):
    out = tmp_path / "o.html"
    rc = pp.main([str(_write(tmp_path, "s.json", SCRIPT)),
                  "--plan", str(_write(tmp_path, "p.json", {"keys": {"S01": "nope.png"}, "thumb_images": {"A": "gone.png"}})),
                  "--out", str(out)])
    assert rc == 0 and out.is_file()
    assert "to paint" in capsys.readouterr().err
    assert "data:image" not in out.read_text(encoding="utf-8")


def test_no_webfonts_drops_the_outside_request(tmp_path):
    assert "fonts.googleapis.com" in pp.build(SCRIPT, {}, tmp_path)
    assert "fonts.googleapis.com" not in pp.build(SCRIPT, {}, tmp_path, webfonts=False)


def test_no_character_names_are_built_in():
    src = (HERE / "plan_page.py").read_text(encoding="utf-8") + (HERE / "template.html").read_text(encoding="utf-8")
    assert "DEFAULT_COLOURS" not in src and "--snooze" not in src


def test_demo_builds_from_a_fresh_clone(tmp_path):
    rc = pp.main([str(EXAMPLE / "script.json"), "--plan", str(EXAMPLE / "plan.json"), "--out", str(tmp_path / "demo.html")])
    assert rc == 0
    plan = json.loads((EXAMPLE / "plan.json").read_text(encoding="utf-8"))
    for path in list((plan.get("keys") or {}).values()) + list((plan.get("thumb_images") or {}).values()):
        assert not path.startswith(("~", "/")), path


def test_empty_script_fails(tmp_path):
    assert pp.main([str(_write(tmp_path, "s.json", {"title": "x"})), "--out", str(tmp_path / "o.html")]) == 1


def test_reply_names_every_picked_option_by_label(tmp_path):
    """Runs the page in a headless browser when Playwright is installed; skipped otherwise."""
    import pytest
    pw = pytest.importorskip("playwright.sync_api")
    out = tmp_path / "demo.html"
    assert pp.main([str(EXAMPLE / "script.json"), "--plan", str(EXAMPLE / "plan.json"), "--out", str(out), "--no-webfonts"]) == 0
    plan = json.loads((EXAMPLE / "plan.json").read_text(encoding="utf-8"))
    with pw.sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            try:
                browser = p.chromium.launch(channel="chrome")
            except Exception as e:  # no browser on this machine
                pytest.skip(f"no Chromium: {e}")
        page = browser.new_page()
        page.goto(out.as_uri())
        # every decision: first the recommended state, then each other option in turn
        for i, d in enumerate(plan["decisions"]):
            for j, op in enumerate(d["options"]):
                page.click(f"#q{i}_{j}")
                text = page.inner_text("#replytext")
                assert f"{i + 1}. {op['label']}" in text, text
        browser.close()
