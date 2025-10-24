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
       data-caption-desc="This is my first attempt at creating pixelart with Aseprite. The color palette I used is Bubblegum, consisting of 16 colors, out of which I used 9. I wanted to experiment with new features like the gradient tool, and that is why I made the background a sunset. Also, I found this sort of reversed light source to be a fun challenge to improve my pixel art skills.<br><br>Seeing the animation feature also present in Aseprite, I would also love to turn this into an animated piece in the near future.">
        <img src="/images/gallery/art-collection/im02.png" alt="Resurgence" />
    </a>
    
    <a href="/images/gallery/art-collection/im01.png"
       data-pswp-width="1920"
       data-pswp-height="1440"
       data-caption-title="1-bit dead end"
       data-caption-desc="I did this piece with a friend of mine for a neuroscience project back at UPF University in Barcelona. We were studying the visual system and how artists took advantage of certain mechanisms in the brain to create effects in their artwork, such as depth or dynamism.<br><br>Our idea was to use the most minimalist form of pixel art: 1-bit art. And I say minimalist rather than simple because working with such a strict limitation — only two possible colors — made it surprisingly challenging to create a scene with recognizable objects. In fact, this kind of art depends entirely on the brain’s ability to interpret visual contrast and fill in missing information.<br><br>In this piece, every element is built only from black and white pixels. Yet, thanks to how our visual system processes edges, perspective, and light, the brain reconstructs a three-dimensional space from almost nothing. The alternating density of dots mimics shading, the converging lines suggest depth, and the sharp contrasts define shapes. Our perception completes the rest, inventing light sources, textures, and even atmosphere.<br><br>What looks like a simple pattern of pixels is, in reality, a small demonstration of how vision is not just about seeing — it’s about interpreting.">
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
                  
  // Adjust padding for caption
  paddingFn: (viewportSize) => {
    const isMobile = window.innerWidth <= 768;
    const isPortrait = window.innerHeight > window.innerWidth;
    const captionPercent = (isMobile && isPortrait) ? 0.40 : 0.35;
    
    return {
      top: 10,
      bottom: Math.floor(viewportSize.y * captionPercent),
      left: 10,
      right: 10
    };
  },
  
  initialZoomLevel: 'fit',
  secondaryZoomLevel: 1.5,
  maxZoomLevel: 2.5,
  
  pinchToClose: true,
  closeOnVerticalDrag: true,
  
  bgOpacity: 0.9
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
          if (title) html = '<div class="caption-title">' + title + '</div>';
          if (desc) html += '<div class="caption-desc">' + desc + '</div>';
          
          el.innerHTML = html;
        }
      });
    }
  });
});

lightbox.init();

// Simple pan reset for mobile centering
lightbox.on('change', () => {
  if (window.innerWidth <= 768) {
    setTimeout(() => {
      const slide = lightbox.pswp.currSlide;
      if (slide && slide.content) {
        slide.content.pan.x = 0;
        slide.content.pan.y = 0;
        slide.content.applyCurrentZoomPan();
      }
    }, 50);
  }
});

// Allow scrolling in caption
lightbox.on('bindEvents', () => {
  const caption = document.querySelector('.pswp__custom-caption');
  if (caption) {
    caption.addEventListener('wheel', (e) => e.stopPropagation(), { passive: true });
    caption.addEventListener('touchmove', (e) => e.stopPropagation(), { passive: true });
  }
});
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
  max-height: 35%;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  border-top: 2px solid rgba(255, 255, 255, 0.3);
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.5) rgba(0, 0, 0, 0.3);
}

@media (max-width: 768px) {
  .pswp__custom-caption {
    max-height: 40%;
    padding: 15px 20px;
    font-size: 0.9em;
  }
  
  .pswp__custom-caption .caption-title {
    font-size: 1.2em !important;
    margin-bottom: 8px !important;
  }
  
  .pswp__custom-caption .caption-desc {
    font-size: 0.95em !important;
    line-height: 1.4 !important;
  }
}

.pswp__custom-caption::-webkit-scrollbar {
  width: 8px;
}

.pswp__custom-caption::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.3);
}

.pswp__custom-caption::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.5);
  border-radius: 4px;
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
