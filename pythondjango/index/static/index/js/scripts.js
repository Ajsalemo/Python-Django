// Toggle option for a slide-out menu
const openNav = () => {
  // If the slide out column is open, and the 'menu' button is clicked again to close it, then shorten the bootstrap column width to minimize it
  if (document.getElementById("mySidenav").classList.contains("active")) {
    document.getElementById("mySidenav").className =
      "col-2 col-sm-1 col-md-1 col-lg-1 todo-page-side-column d-flex flex-column";
    // This line adds classes to the menu content to hide the text upon closing
    // This still lets the font-awesome icons show unpon minimizing
    document.getElementById("sideNavContentOne").className =
      "d-none todo-page-sidenav-content";
    document.getElementById("sideNavContentTwo").className =
      "d-none todo-page-sidenav-content";
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

// TODO - Need to see if it's possible to make this more DRY, since the forms are on two different pages

// This checks if the 'Task' form field is empty
// If it's empty, set stylistic changes to indicate there is a validation error
const validateTaskFormSubmit = () => {
  console.log(document.getElementById("create-task-form").value)
  if ((document.getElementById("create-task-form").value === "")) {
    document.getElementById("task-form-error").innerHTML = "You must enter a value";
    document.getElementById("task-form-error").style.color = "red";
    document.getElementById("create-task-form").style.border = "1px solid red";
    return false;
  } else if ((document.getElementById("create-task-form").value !== "")) {
    console.log('loading')
  }
  document.getElementById("task-form-error").innerHTML = "";
};

// This checks if the 'Important Task' form field is empty
// If it's empty, set stylistic changes to indicate there is a validation error
const validateImportantTaskFormSubmit = () => {
  if ((document.getElementById("create-important-task-form").value === "")) {
    document.getElementById("important-task-form-error").innerHTML = "You must enter a value";
    document.getElementById("important-task-form-error").style.color = "red";
    document.getElementById("create-important-task-form").style.border = "1px solid red";
    return false;
  } else if ((document.getElementById("create-important-task-form").value !== "")) {
    console.log('loading')
  }
  document.getElementById("important-task-form-error").innerHTML = "";
}
