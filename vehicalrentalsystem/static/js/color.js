// Step 3: Listen for clicks on .color-option elements, grab value from data attribute and update --primary-color

document.addEventListener('click', (e) => {
    const colorOption = e.target.closest('.color-option');
    if (!colorOption) return;

    // unselect currently selected color options
    document.querySelectorAll('.color-option').forEach(colorOption => colorOption.classList.remove('is-selected'));
    colorOption.classList.add('is-selected');

    const color = colorOption.dataset.color;

    let root = document.getElementById('sidebar_main');

    root.style.setProperty('background-color', color);

    let vertical_nav_menu = document.querySelectorAll(".vertical-nav-menu li a ")
    for (let i = 0; i<= vertical_nav_menu.length; i++){
        vertical_nav_menu[i].style.setProperty("color", "white");
    }

  });