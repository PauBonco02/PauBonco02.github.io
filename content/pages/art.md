Title: Art
Date: 2025-01-01
Slug: art
Order: 3

Here is a collection of my artwork. Click on any image to zoom it and see more details.

<!-- PhotoSwipe CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.3.7/photoswipe.min.css">

<div class="gallery" id="my-gallery">
    <a href="/images/gallery/art-collection/im02.png"
       data-pswp-width="1600"
       data-pswp-height="1440"
       data-caption-title="Resurgence"
       data-caption-desc="This is my first attempt at creating pixelart using Aseprite.">
        <img src="/images/gallery/art-collection/im02.png" alt="Resurgence" />
    </a>
    
    <a href="/images/gallery/art-collection/im01.png"
       data-pswp-width="1920"
       data-pswp-height="1440"
       data-caption-title="1-bit dead end"
       data-caption-desc="I did this with a friend of mine for a Neuroscience Project back in Barcelona.">
        <img src="/images/gallery/art-collection/im01.png" alt="1-bit dead end" />
    </a>
    
</div>

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
