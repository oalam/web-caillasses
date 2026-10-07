/**
 * Les Caillasses - Gestion des interactions (menu mobile, sous-menus, etc.)
 */
document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const dropdownToggle = document.querySelector('.nav-item-dropdown > .nav-link');
  const dropdownMenu = document.querySelector('.dropdown-menu');

  // Bascule du menu hamburger mobile
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('open');
    });
  }

  // Gestion du sous-menu Accueil sur mobile / tactile
  if (dropdownToggle && dropdownMenu) {
    dropdownToggle.addEventListener('click', (e) => {
      // Sur les écrans mobiles (< 768px), un clic ouvre le sous-menu au lieu de naviguer
      if (window.innerWidth <= 768) {
        e.preventDefault();
        dropdownMenu.classList.toggle('open');
      }
    });
  }

  // Fermeture du menu si on clique en dehors
  document.addEventListener('click', (e) => {
    if (navMenu && navToggle && !navMenu.contains(e.target) && !navToggle.contains(e.target)) {
      navMenu.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    }
  });
});
