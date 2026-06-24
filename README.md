# Hiking Trails App

A beginner-friendly Flask web app for exploring hiking trails.

This project was created while learning Python and Flask. It displays hiking trail information such as location, difficulty, distance, time, and best use. It also includes a simple search feature.

## Features

- Home page built with Flask
- Hiking trail data stored in Python
- Trail cards with useful details
- Difficulty badges for Easy, Moderate, and Hard trails
- Search by trail name
- Basic CSS styling

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Git and GitHub

## How To Run The App

First, make sure you are inside the project folder:

```bash
cd ~/Documents/hiking_trails_app
```

## Project Status

This is an early learning version. More features will be added step by step.

## Future Ideas

- Add more hiking trails
- Add difficulty filter
- Add trail images
- Add a trail detail page
- Add map support
- Improve mobile design


## June 18, 2026 Update

Today I continued improving the Hiking Trails App.

### Work Completed

- Ran the Flask app from the terminal
- Added a difficulty dropdown filter
- Connected the filter to the trail data
- Made search and difficulty filter work together
- Fixed the dropdown so it remembers the selected option
- Tested Easy, Moderate, Hard, and All filter options

### What I Learned

- How to read URL values using `request.args.get()`
- How to filter Python list data using conditions
- How to combine search and dropdown filters
- How HTML forms send data to Flask
- How to keep selected form values visible after submitting

### Next Ideas

- Add more trails
- Move HTML into a template file
- Move CSS into a separate CSS file
- Add trail images


## June 24, 2026 Update

Today I continued improving the Hiking Trails App.

### Work Completed

- Restarted and tested the Flask app locally
- Added a no-results message for searches with no matching trails
- Fixed the placement of the no-results logic in the Python function
- Updated the results heading from "Available Trails" to "Search Results"
- Tested the empty search result using random search text

### What I Learned

- How indentation affects where Python code runs
- Why logic after a `for` loop must line up correctly
- How to check if a generated HTML string is empty
- How to improve the user experience when no data matches a search

### Next Ideas

- Move HTML into a separate Flask template file
- Move CSS into a separate stylesheet
- Add more trail data
- Add images for each trail
