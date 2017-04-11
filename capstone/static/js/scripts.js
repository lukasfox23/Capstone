// use a mainSlider div to create the gallery/main page effects
$(document).ready(function(){
  $('.mainSlider').bxSlider({
    slideWidth: 375,
    minSlides: 3,
    maxSlides: 3,
    moveSlides: 1,
    slideMargin: 20,
    auto: true,
    adaptiveHeight: true
  });
});
