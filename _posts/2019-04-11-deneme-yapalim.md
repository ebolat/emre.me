---
title: "Deneme yapalim"
header:
  image: /assets/images/posts/hope-house-press-leather-diary-studio-390262-unsplash.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
categories:
  - testing
tags:
  - deneme
  - yapalim
masthead: true
toc: true
toc_sticky: true
---

This post should display a **header with an overlay image**, if the theme supports it.

Non-square images can provide some unique styling issues.

This post tests overlay header images.

## Overlay filter

You can use it by specifying the opacity (between 0 and 1) of a black overlay like so:

![transparent black overlay]({{ "/assets/images/mm-header-overlay-black-filter.jpg" | relative_url }})

```yaml
excerpt: "This post should [...]"
header:
  overlay_image: /assets/images/unsplash-image-1.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "More Info"
      url: "https://unsplash.com"
```

Or if you want to do more fancy things, go full rgba:

![transparent red overlay]({{ "/assets/images/mm-header-overlay-red-filter.jpg" | relative_url }})

```yaml
excerpt: "This post should [...]"
header:
  overlay_image: /assets/images/unsplash-image-1.jpg
  overlay_filter: rgba(255, 0, 0, 0.5)
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "More Info"
      url: "https://unsplash.com"
```

