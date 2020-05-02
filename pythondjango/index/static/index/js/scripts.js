// Toggle option for a slide-out menu
const openNav = () => {
  if (document.getElementById("mySidenav").classList.contains("active")) {
    document.getElementById("mySidenav").className =
      "col-2 col-sm-1 col-md-1 col-lg-1 todo-page-side-column d-flex flex-column";
    document.getElementById("sideNavContentOne").className = "d-none todo-page-sidenav-content";
    document.getElementById("sideNavContentTwo").className = "d-none todo-page-sidenav-content";
  } else {
    document.getElementById("mySidenav").className =
      "col-3 col-sm-2 col-md-2 col-lg-2 todo-page-side-column d-flex flex-column active";
    document.getElementById("sideNavContentOne").className =
      "d-block todo-page-sidenav-content pl-3";
    document.getElementById("sideNavContentTwo").className =
      "d-block todo-page-sidenav-content pl-3";
  }
};
