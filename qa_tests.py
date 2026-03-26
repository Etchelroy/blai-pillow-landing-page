import re
from html.parser import HTMLParser

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Track test results
tests_passed = 0
tests_failed = 0
test_results = []

def test_pass(name):
    global tests_passed
    tests_passed += 1
    test_results.append(f"PASS: {name}")
    print(f"PASS: {name}")

def test_fail(name, reason):
    global tests_failed
    tests_failed += 1
    test_results.append(f"FAIL: {name}: {reason}")
    print(f"FAIL: {name}: {reason}")

# ===== TEST 1: HTML Structure =====
try:
    if html_content.startswith("<!DOCTYPE html>"):
        test_pass("HTML has DOCTYPE declaration")
    else:
        test_fail("HTML has DOCTYPE declaration", "DOCTYPE not found")
except Exception as e:
    test_fail("HTML has DOCTYPE declaration", str(e))

# ===== TEST 2: Meta Tags =====
try:
    has_charset = 'charset="UTF-8"' in html_content
    has_viewport = 'viewport' in html_content
    has_title = '<title>CloudRest Pillows' in html_content
    has_description = 'name="description"' in html_content
    
    if has_charset and has_viewport and has_title and has_description:
        test_pass("All required meta tags present")
    else:
        missing = []
        if not has_charset: missing.append("charset")
        if not has_viewport: missing.append("viewport")
        if not has_title: missing.append("title")
        if not has_description: missing.append("description")
        test_fail("All required meta tags present", f"Missing: {', '.join(missing)}")
except Exception as e:
    test_fail("All required meta tags present", str(e))

# ===== TEST 3: CSS Variables Defined =====
try:
    css_vars = [
        '--white', '--blue', '--blue-dark', '--blue-light',
        '--gray-50', '--gray-100', '--gray-200', '--gray-300',
        '--gray-600', '--gray-700', '--gray-900',
        '--shadow-sm', '--shadow-md', '--shadow-lg', '--shadow-xl'
    ]
    
    missing_vars = []
    for var in css_vars:
        if f'{var}:' not in html_content:
            missing_vars.append(var)
    
    if not missing_vars:
        test_pass("All CSS variables are defined")
    else:
        test_fail("All CSS variables are defined", f"Missing: {', '.join(missing_vars[:5])}")
except Exception as e:
    test_fail("All CSS variables are defined", str(e))

# ===== TEST 4: Navbar Present =====
try:
    if 'class="navbar"' in html_content:
        test_pass("Navbar element exists")
    else:
        test_fail("Navbar element exists", "Navbar class not found")
except Exception as e:
    test_fail("Navbar element exists", str(e))

# ===== TEST 5: Navbar Brand =====
try:
    if 'class="navbar-brand"' in html_content:
        test_pass("Navbar brand element exists")
    else:
        test_fail("Navbar brand element exists", "Navbar brand class not found")
except Exception as e:
    test_fail("Navbar brand element exists", str(e))

# ===== TEST 6: Hero Section =====
try:
    if 'class="hero"' in html_content:
        test_pass("Hero section exists")
    else:
        test_fail("Hero section exists", "Hero class not found")
except Exception as e:
    test_fail("Hero section exists", str(e))

# ===== TEST 7: Hero Title =====
try:
    if 'class="hero-title"' in html_content:
        test_pass("Hero title element exists")
    else:
        test_fail("Hero title element exists", "Hero title class not found")
except Exception as e:
    test_fail("Hero title element exists", str(e))

# ===== TEST 8: Primary Button Style =====
try:
    if 'class="btn-primary"' in html_content:
        test_pass("Primary button class defined")
    else:
        test_fail("Primary button class defined", "btn-primary class not found")
except Exception as e:
    test_fail("Primary button class defined", str(e))

# ===== TEST 9: CSS Box Sizing Reset =====
try:
    if 'box-sizing: border-box;' in html_content:
        test_pass("CSS box-sizing reset applied")
    else:
        test_fail("CSS box-sizing reset applied", "box-sizing property not found")
except Exception as e:
    test_fail("CSS box-sizing reset applied", str(e))

# ===== TEST 10: Font Family Applied =====
try:
    if 'font-family:' in html_content and 'Segoe UI' in html_content:
        test_pass("Font family stack is defined")
    else:
        test_fail("Font family stack is defined", "Font family not found")
except Exception as e:
    test_fail("Font family stack is defined", str(e))

# ===== TEST 11: Navbar Position Fixed =====
try:
    if 'position: fixed;' in html_content and '.navbar' in html_content:
        test_pass("Navbar is fixed position")
    else:
        test_fail("Navbar is fixed position", "Fixed position not configured for navbar")
except Exception as e:
    test_fail("Navbar is fixed position", str(e))

# ===== TEST 12: Hero Gradient Background =====
try:
    if 'linear-gradient' in html_content and '#EFF6FF' in html_content:
        test_pass("Hero gradient background defined")
    else:
        test_fail("Hero gradient background defined", "Gradient not found in hero")
except Exception as e:
    test_fail("Hero gradient background defined", str(e))

# ===== TEST 13: Hero Container Grid =====
try:
    if 'display: grid;' in html_content and 'grid-template-columns: 1fr 1fr;' in html_content:
        test_pass("Hero container grid layout exists")
    else:
        test_fail("Hero container grid layout exists", "Grid layout not found")
except Exception as e:
    test_fail("Hero container grid layout exists", str(e))

# ===== TEST 14: Responsive Media Query =====
try:
    if '@media (max-width: 768px)' in html_content:
        test_pass("Mobile responsive media query exists")
    else:
        test_fail("Mobile responsive media query exists", "Media query not found")
except Exception as e:
    test_fail("Mobile responsive media query exists", str(e))

# ===== TEST 15: Navbar Toggle Button =====
try:
    if 'class="navbar-toggle"' in html_content:
        test_pass("Navbar toggle button exists")
    else:
        test_fail("Navbar toggle button exists", "navbar-toggle class not found")
except Exception as e:
    test_fail("Navbar toggle button exists", str(e))

# ===== TEST 16: Hero Badge Element =====
try:
    if 'class="hero-badge"' in html_content:
        test_pass("Hero badge element exists")
    else:
        test_fail("Hero badge element exists", "hero-badge class not found")
except Exception as e:
    test_fail("Hero badge element exists", str(e))

# ===== TEST 17: Transitions Defined =====
try:
    if 'transition:' in html_content:
        test_pass("CSS transitions are defined")
    else:
        test_fail("CSS transitions are defined", "Transition properties not found")
except Exception as e:
    test_fail("CSS transitions are defined", str(e))

# ===== TEST 18: HTML is not truncated =====
try:
    if 'btn-primary {' in html_content and html_content.count('<') > 10:
        test_pass("HTML content appears complete (not severely truncated)")
    else:
        test_fail("HTML content appears complete (not severely truncated)", "HTML seems incomplete or very short")
except Exception as e:
    test_fail("HTML content appears complete (not severely truncated)", str(e))

# ===== TEST 19: Backdrop Filter for Modern Browser Support =====
try:
    if 'backdrop-filter: blur' in html_content:
        test_pass("Backdrop filter effect defined for navbar")
    else:
        test_fail("Backdrop filter effect defined for navbar", "Backdrop filter not found")
except Exception as e:
    test_fail("Backdrop filter effect defined for navbar", str(e))

# ===== TEST 20: Z-index Stacking Context =====
try:
    if 'z-index: 1000;' in html_content:
        test_pass("Z-index stacking context defined")
    else:
        test_fail("Z-index stacking context defined", "z-index not found")
except Exception as e:
    test_fail("Z-index stacking context defined", str(e))

# Print summary
print("\n" + "="*60)
print(f"SUMMARY: {tests_passed}/{tests_passed + tests_failed} tests passed")
print("="*60)

if tests_failed > 0:
    print(f"\nFailed tests: {tests_failed}")
    for result in test_results:
        if result.startswith("FAIL"):
            print(f"  - {result}")