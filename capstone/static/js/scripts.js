// use a mainSlider div to create the main page effects
$(document).ready(function(){
  $('.mainSlider').bxSlider({
    slideWidth: 375,
    minSlides: 1,
    maxSlides: 3,
    moveSlides: 1,
    slideMargin: 30,
    auto: true,
    adaptiveHeight: true
  });
});

// use a gallerySlider div to create the gallery page effects
$(document).ready(function(){
  $('.gallerySlider').bxSlider({
    slideWidth: 375,
    minSlides: 3,
    maxSlides: 3,
    moveSlides: 1,
    slideMargin: 20,
  });
});
