# Testing

## CI Linter validation
Each file except "Art" passed through the [CI Python linter](https://pep8ci.herokuapp.com/) without any issues.

### Run game

![CI linter results for run game](assets/images/testing/rungame-linter-pass.png)

### Run

![CI linter results for run](assets/images/testing/run-linter-pass.png)

### Settings

![CI linter results for settings](assets/images/testing/settings-linter-pass.png)


### Art
Although an active effort was made to remove any error from the linter, the art linter check still displays 6 errors which were chosen to be ignored to maintain readability of the file and UI integrity of the game. The character limit is exceeded because the design choice was made to have banners and artwork span the entire width of the screen. In a future projects I will make certain the art choices do not intefere with Python Code style standarts.

![CI linter results for art](assets/images/testing/art-linter-errors.png)

## Feature testing

### Loading screen

- [x] Logo displaying as intended
- [x] Typewriting effect for loading text
- [x] Automatically continues to main menu

- [x] FEATURE WORKS AS INTENDED

### Main menu

- [x] All visuals displaying as intended
- [x] Typewriting effect for loading text
- [x] Automatically continues to main menu

- [x] FEATURE WORKS AS INTENDED