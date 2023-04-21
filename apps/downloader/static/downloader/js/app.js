console.log('It is working')

const darkMode = document.getElementById('dark-mode')
const body = document.querySelector('body')
const isDarkModeActive = JSON.parse(localStorage.getItem('darkMode'));


// Check Dark mode
document.addEventListener('DOMContentLoaded', () => {
  isDarkModeActive ? body.classList.add('dark') : body.classList.remove('dark')
});

// Toggle Dark mode
darkMode.addEventListener('click', () => {
  body.classList.toggle('dark')
  localStorage.setItem('darkMode', body.classList.contains('dark'))
})


