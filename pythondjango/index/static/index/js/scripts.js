
// Toggle option for a slide-out menu
const openNav = () => {
  // If the slide out column is open, and the 'menu' button is clicked again to close it, then shorten the bootstrap column width to minimize it
  if (document.getElementById("mySidenav").classList.contains("active")) {
    document.getElementById("mySidenav").className =
      "col-2 col-sm-1 col-md-1 col-lg-1 todo-page-side-column d-flex flex-column";
    // This line adds classes to the menu content to hide the text upon closing
    // This still lets the font-awesome icons show unpon minimizing
    document.getElementById("sideNavContentOne").className = "d-none todo-page-sidenav-content";
    document.getElementById("sideNavContentTwo").className = "d-none todo-page-sidenav-content";
  } else {
    // If the menu is closed and the 'menu' icon is clicked - this will add the 'active' class to it
    // The boostrap column classes are increased numerically to maximize the side nav
    document.getElementById("mySidenav").className =
      "col-4 col-sm-3 col-md-2 col-lg-2 todo-page-side-column d-flex flex-column active";
    // When the sidenav is maximized, the text for the content is now displayed
    document.getElementById("sideNavContentOne").className =
      "d-block todo-page-sidenav-content pl-1";
    document.getElementById("sideNavContentTwo").className =
      "d-block todo-page-sidenav-content pl-1";
  }
};
