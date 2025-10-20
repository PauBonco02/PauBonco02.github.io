#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image
import json

# Configuration
GALLERY_FOLDER = "content/images/gallery/art-collection"
OUTPUT_FILE = "content/pages/art.md"
GALLERY_TITLE = "Art"
GALLERY_DATE = "2025-01-01"
SLUG = "art"
GALLERY_ORDER = "3"

# Get all image files
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
gallery_path = Path(GALLERY_FOLDER)
images = sorted([f for f in gallery_path.iterdir() 
                if f.suffix.lower() in image_extensions], reverse=True)

# Generate HTML
html_parts = [f"""Title: {GALLERY_TITLE}
Date: {GALLERY_DATE}
Slug: {SLUG}
Order: {GALLERY_ORDER}

Here is a collection of my artwork. Click on any image to zoom it and see more details.

<!-- PhotoSwipe CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.3.7/photoswipe.min.css">

<div class="gallery" id="my-gallery">
"""]

for img in images:
    # Get actual image dimensions
    try:
        with Image.open(img) as im:
            width, height = im.size
    except:
        width, height = 800, 600  # fallback
    
    # Check if there's a caption file
    caption_file = img.with_suffix('.txt')

    # DEBUG: Print what we're looking for
    print(f"Image: {img.name}")
    print(f"Looking for caption: {caption_file.name}")
    print(f"Caption exists: {caption_file.exists()}")
    if caption_file.exists():
        print(f"Caption content: {caption_file.read_text(encoding='utf-8')[:50]}...")
    print("---")

    title = ""
    description = ""
    
    if caption_file.exists():
        lines = caption_file.read_text(encoding='utf-8').strip().split('\n')
        title = lines[0].strip() if lines else ""
        description = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
    else:
        title = img.stem.replace('-', ' ').replace('_', ' ').title()
    
    img_path = f"/images/gallery/art-collection/{img.name}"
    
    # Escape for HTML attributes
    title_safe = title.replace('"', '&quot;').replace("'", '&#39;')
    desc_safe = description.replace('"', '&quot;').replace("'", '&#39;').replace('\n', '<br>')
    
    html_parts.append(f"""    <a href="{img_path}"
       data-pswp-width="{width}"
       data-pswp-height="{height}"
       data-caption-title="{title_safe}"
       data-caption-desc="{desc_safe}">
        <img src="{img_path}" alt="{title_safe}" />
    </a>
    
""")

html_parts.append("""</div>

<!-- PhotoSwipe JavaScript -->
<script type="module">
import PhotoSwipeLightbox from 'https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.3.7/photoswipe-lightbox.esm.min.js';

const lightbox = new PhotoSwipeLightbox({
  gallery: '#my-gallery',
  children: 'a',
  pswpModule: () => import('https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.3.7/photoswipe.esm.min.js'),
                  
  // Add padding at the bottom for the caption
  paddingFn: (viewportSize) => {
    return {
      top: 10,
      bottom: 100,  // Reserve space for caption (adjust as needed)
      left: 10,
      right: 10
    }
  },
                  
  // Limit maximum zoom
  maxZoomLevel: 2.5,  // Adjust this value (default is 4)
  initialZoomLevel: 'fit'  // Start with fit-to-screen
});

// Add caption
lightbox.on('uiRegister', function() {
  lightbox.pswp.ui.registerElement({
    name: 'custom-caption',
    order: 9,
    isButton: false,
    appendTo: 'root',
    onInit: (el, pswp) => {
      lightbox.pswp.on('change', () => {
        const currSlideElement = lightbox.pswp.currSlide.data.element;
        if (currSlideElement) {
          const title = currSlideElement.getAttribute('data-caption-title') || '';
          const desc = currSlideElement.getAttribute('data-caption-desc') || '';
          
          let html = '';
          if (title) {
            html = '<div class="caption-title">' + title + '</div>';
          }
          if (desc) {
            html += '<div class="caption-desc">' + desc + '</div>';
          }
          
          el.innerHTML = html;
        }
      });
    }
  });
});

lightbox.init();
</script>

<style>
/* Caption container */
.pswp__custom-caption {
  background: rgba(0, 0, 0, 0.85);
  color: #fff;
  padding: 20px 30px;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
  max-height: 30%;
  overflow-y: auto;
}

.pswp__custom-caption .caption-title {
  font-size: 1.3em;
  font-weight: bold;
  margin-bottom: 10px;
}

.pswp__custom-caption .caption-desc {
  font-size: 1em;
  line-height: 1.5;
}
</style>
""")

# Write to file
Path(OUTPUT_FILE).write_text(''.join(html_parts), encoding='utf-8')
print(f"Gallery generated with {len(images)} images!")
print(f"Output: {OUTPUT_FILE}")