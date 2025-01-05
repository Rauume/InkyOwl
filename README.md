# Inky Owl

## An e-ink photoframe for displaying your favourite photos (of owls)

This project is built for the [Pimoroni Inky Impression](https://shop.pimoroni.com/products/inky-impression-4), and Raspberry Pi Zero W.

This project makes use of a Python-Flask API backend, and Sveltekit frontend. The goal is to build a periodically refreshing photoframe, from various sources the user can set.

## Features

Web user interface:

- Built in Sveltekit
- [ ] Displays the current image on landing page
- User can set the image source
	- [ ] Shared Immich Gallery
	- [ ] Reddit subreddits
- [ ] Displays image metadata (If available)
	- Image name
	- Date taken
	- Geolocation

Python API/Backend:

- [x] Updates the attached Pimoroni Inky Impression e-ink screen
- [ ] Uses the 4 physical buttons to set the image source and update the screen
- [ ] Automatically updates to a new image after a user-set amount of time (every X hours/mins)
- [ ] Config file for setting the relevant ports and other server settings.

## Getting Started

Todo.

To run the sveltekit development server:

```bash
npm run dev --host
```