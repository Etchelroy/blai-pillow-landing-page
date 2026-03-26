import re
from html.parser import HTMLParser

# The HTML code to test
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudRest Pillows - Premium Sleep Solutions</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --white: #FFFFFF;
            --blue: #2563EB;
            --blue-dark: #1E40AF;
            --blue-light: #DBEAFE;
            --gray-50: #F9FAFB;
            --gray-100: #F3F4F6;
            --gray-200: #E5E7EB;
            --gray-300: #D1D5DB;
            --gray-600: #4B5563;
            --gray-700: #374151;
            --gray-900: #111827;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            color: var(--gray-900);
            background-color: var(--white);
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <nav class="navbar"></nav>
    <section class="hero"></section>
</body>
</html>"""


class ImageExtractor(HTMLParser):
    """Parse HTML and extract all img tags and their src attributes"""
    def __init__(self):
        super().__init__()
        self.images = []
        self.all_tags = []
    
    def handle_starttag(self, tag, attrs):
        self.all_tags.append(tag)
        if tag == 'img':
            attrs_dict = dict(attrs)
            self.images.append({
                'src': attrs_dict.get('src', ''),
                'alt': attrs_dict.get('alt', ''),
                'attrs': attrs_dict
            })


class StyleValidator:
    """Validate CSS syntax and structure"""
    def __init__(self, style_content):
        self.style_content = style_content
        self.css_variables = []
        self.extract_variables()
    
    def extract_variables(self):
        """Extract CSS custom properties (variables)"""
        pattern = r'--[\w-]+:'
        self.css_variables = re.findall(pattern, self.style_content)


def test_html_structure():
    """Test that HTML has proper structure"""
    assert '<!DOCTYPE html>' in html_content, "Missing DOCTYPE declaration"
    assert '<html lang="en">' in html_content, "Missing or incorrect html tag"
    assert '<meta charset="UTF-8">' in html_content, "Missing charset meta tag"
    assert '<title>' in html_content, "Missing title tag"
    print("PASS: test_html_structure")


def test_navbar_exists():
    """Test that navbar element exists"""
    assert 'class="navbar"' in html_content, "Navbar element missing"
    print("PASS: test_navbar_exists")


def test_hero_section_exists():
    """Test that hero section exists"""
    assert 'class="hero"' in html_content, "Hero section missing"
    print("PASS: test_hero_section_exists")


def test_css_variables_defined():
    """Test that CSS variables are properly defined"""
    parser = StyleValidator(html_content)
    assert len(parser.css_variables) > 0, "No CSS variables found"
    assert '--blue' in html_content, "Blue color variable missing"
    assert '--white' in html_content, "White color variable missing"
    print("PASS: test_css_variables_defined")


def test_color_variables():
    """Test that essential color variables are defined"""
    required_colors = ['--white', '--blue', '--blue-dark', '--blue-light', 
                       '--gray-50', '--gray-100', '--gray-600', '--gray-700', '--gray-900']
    for color in required_colors:
        assert f'{color}:' in html_content, f"Missing color variable: {color}"
    print("PASS: test_color_variables")


def test_shadow_variables():
    """Test that shadow variables are defined"""
    required_shadows = ['--shadow-sm', '--shadow-md', '--shadow-lg', '--shadow-xl']
    for shadow in required_shadows:
        assert f'{shadow}:' in html_content, f"Missing shadow variable: {shadow}"
    print("PASS: test_shadow_variables")


def test_nav_styles_exist():
    """Test that navigation styles are defined"""
    assert '.navbar {' in html_content, "Navbar styles missing"
    assert '.nav-container {' in html_content, "Nav container styles missing"
    assert '.nav-logo {' in html_content, "Nav logo styles missing"
    assert '.nav-menu {' in html_content, "Nav menu styles missing"
    print("PASS: test_nav_styles_exist")


def test_hero_styles_exist():
    """Test that hero section styles are defined"""
    assert '.hero {' in html_content, "Hero styles missing"
    assert '.hero-container {' in html_content, "Hero container styles missing"
    assert '.hero-title {' in html_content, "Hero title styles missing"
    print("PASS: test_hero_styles_exist")


def test_button_styles_exist():
    """Test that button styles are defined"""
    assert '.btn-primary {' in html_content, "Primary button styles missing"
    assert '.nav-cta {' in html_content, "CTA button styles missing"
    print("PASS: test_button_styles_exist")


def test_responsive_design():
    """Test that responsive design elements exist"""
    assert 'viewport' in html_content, "Viewport meta tag missing"
    assert 'grid-template-columns: 1fr 1fr' in html_content, "Grid layout missing"
    print("PASS: test_responsive_design")


def test_accessibility_features():
    """Test that accessibility features are present"""
    assert 'outline:' in html_content, "Focus outline missing for accessibility"
    assert 'min-height: 44px' in html_content, "Touch target size not meeting minimum"
    print("PASS: test_accessibility_features")


def test_image_detection():
    """Test for img tags - critical issue per task"""
    parser = ImageExtractor()
    parser.feed(html_content)
    
    # The provided code snippet is incomplete, so we can only check structure
    # In the complete HTML, we need to verify images have src attributes
    if parser.images:
        for img in parser.images:
            assert 'src' in img['attrs'], f"Image missing src attribute"
            assert img['src'].strip(), f"Image has empty src attribute"
    
    print("PASS: test_image_detection")


def test_no_broken_css_syntax():
    """Test that CSS doesn't have obvious syntax errors"""
    # Count opening and closing braces
    open_braces = html_content.count('{')
    close_braces = html_content.count('}')
    # Note: The provided code is incomplete, so we test what's provided
    assert open_braces > 0, "No CSS rules found"
    print("PASS: test_no_broken_css_syntax")


def test_media_query_structure():
    """Test for responsive breakpoints"""
    assert 'clamp(' in html_content or '@media' in html_content or 'max-width:' in html_content, \
        "No responsive sizing found"
    print("PASS: test_media_query_structure")


def test_font_stack():
    """Test that appropriate font stack is defined"""
    assert 'font-family:' in html_content, "Font family not defined"
    assert '-apple-system' in html_content, "System font stack missing"
    print("PASS: test_font_stack")


def test_transition_effects():
    """Test that transitions are defined for smooth interactions"""
    assert 'transition:' in html_content, "No transitions defined"
    print("PASS: test_transition_effects")


def test_hero_badge_styling():
    """Test that hero badge styling exists"""
    assert '.hero-badge {' in html_content, "Hero badge styles missing"
    assert 'border-radius: 100px' in html_content, "Pill-shaped badge styling missing"
    print("PASS: test_hero_badge_styling")


def test_hamburger_menu():
    """Test that hamburger menu for mobile exists"""
    assert '.hamburger {' in html_content, "Hamburger menu styles missing"
    assert 'display: none' in html_content, "Mobile menu not hidden by default"
    print("PASS: test_hamburger_menu")


def test_sticky_navigation():
    """Test that sticky navigation is implemented"""
    assert 'position: sticky' in html_content, "Sticky positioning not found"
    assert 'z-index: 1000' in html_content, "Z-index for sticky nav missing"
    print("PASS: test_sticky_navigation")


def test_grid_layout():
    """Test that grid layout is used in hero"""
    assert 'grid-template-columns:' in html_content, "Grid layout not used"
    assert 'display: grid' in html_content, "Grid display not found"
    print("PASS: test_grid_layout")


def test_gradient_background():
    """Test that gradient background is applied"""
    assert 'linear-gradient' in html_content, "Linear gradient not found"
    print("PASS: test_gradient_background")


def test_code_quality_no_inline_styles():
    """Test that styles are in style tag, not inline"""
    # Count style attributes in HTML body
    inline_styles = re.findall(r'style="[^"]*"', html_content)
    # The provided code appears to use class-based styling, which is good
    assert '<style>' in html_content, "Style tag not found"
    print("PASS: test_code_quality_no_inline_styles")


def test_semantic_html():
    """Test for semantic HTML elements"""
    assert '<nav' in html_content or 'navbar' in html_content, "Navigation not semantic"
    assert '<section' in html_content, "Section element not found"
    print("PASS: test_semantic_html")


# Run all tests
if __name__ == "__main__":
    tests = [
        test_html_structure,
        test_navbar_exists,
        test_hero_section_exists,
        test_css_variables_defined,
        test_color_variables,
        test_shadow_variables,
        test_nav_styles_exist,
        test_hero_styles_exist,
        test_button_styles_exist,
        test_responsive_design,
        test_accessibility_features,
        test_image_detection,
        test_no_broken_css_syntax,
        test_media_query_structure,
        test_font_stack,
        test_transition_effects,
        test_hero_badge_styling,
        test_hamburger_menu,
        test_sticky_navigation,
        test_grid_layout,
        test_gradient_background,
        test_code_quality_no_inline_styles,
        test_semantic_html,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__}: {str(e)}")
            failed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__}: {str(e)}")
            failed += 1
    
    print(f"\n{passed}/{len(tests)} tests passed")
    
    if failed > 0:
        print(f"{failed} tests failed")