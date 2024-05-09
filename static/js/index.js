
// Animation - paragraphs 
document.addEventListener('DOMContentLoaded', function() {
    const fadeInElements = document.querySelectorAll('.fade-in');
  
    function fadeInOnScroll() {
      fadeInElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
  
        if (elementTop < windowHeight) {
          element.classList.add('visible'); // Add the visible class
        } else {
          element.classList.remove('visible'); // Remove the visible class
        }
      });
    }
  
    window.addEventListener('scroll', fadeInOnScroll);
    fadeInOnScroll(); // Initial check
  });
  

// animation - cards 
document.addEventListener('DOMContentLoaded', function() {
    const card = document.querySelector('.card');
  
    function slideInCardOnScroll() {
      const elementTop = card.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
  
      if (elementTop < windowHeight) {
        card.classList.add('slide-in');
      }
    }
  
    window.addEventListener('scroll', slideInCardOnScroll);
    slideInCardOnScroll(); // Initial check
  });

  
function inProgress() {
    alert('Men at work! Feature build in progress!')
}

// charts 
new Chartist.Line('#traffic-chart', {
  labels: ['January', 'Februrary', 'March', 'April', 'May', 'June'],
  series: [
      [23000, 25000, 19000, 34000, 56000, 64000]
  ]
  }, {
  low: 0,
  showArea: true
});

// image carousel slider 
document.querySelectorAll('.carousel-item img').forEach(function(item) {
  item.addEventListener('click', function() {
    document.getElementById('modalImage').src = this.src;
  });
});