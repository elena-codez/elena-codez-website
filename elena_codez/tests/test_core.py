def test_index(django_app):
    response = django_app.get("/")

    # Check for key phrases
    response.mustcontain("Coming Soon", "&copy; 2019 Elena Codez")

    html = response.html

    assert html.title.text == "Elena Codez"

    logo_image = html.find("img", attrs={"class": "logo"})
    assert logo_image is not None
    assert "elena_codez_logo_horizontal.png" in logo_image["src"]

    coming_soon_header = html.find("h1", attrs={"class": "coming-soon"})
    assert coming_soon_header is not None
    assert "Coming Soon" in str(coming_soon_header)
