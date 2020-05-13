// Element variables
const mySideNav = document.getElementById("mySidenav");
const sideNavContentOne = document.getElementById("sideNavContentOne");
const sideNavContentTwo = document.getElementById("sideNavContentTwo");
const taskButtonAdd = document.getElementById("task-button-add");
const createTaskForm = document.getElementById("create-task-form");
const taskFormError = document.getElementById("task-form-error");
const createImportantTaskForm = document.getElementById(
  "create-important-task-form"
);
const createImportantTaskFormError = document.getElementById(
  "important-task-form-error"
);
const taskButtonImportantAdd = document.getElementById(
  "task-button-important-add"
);
const taskButtonIcon = document.querySelector(
  ".todo-page-add-task-form-submit-text"
);

// Toggle option for a slide-out menu
const openNav = () => {
  // If the slide out column is open, and the 'menu' button is clicked again to close it, then shorten the bootstrap column width to minimize it
  if (mySideNav.classList.contains("active")) {
    mySideNav.classList.remove(
      "col-4",
      "col-sm-3",
      "col-md-2",
      "col-lg-2",
      "active"
    );
    mySideNav.classList.add("col-2", "col-sm-1", "col-md-1", "col-lg-1");
    // Hide the sidebar text upon minimizing
    sideNavContentOne.classList.replace("d-block", "d-none");
    sideNavContentTwo.classList.replace("d-block", "d-none");
  } else {
    // If the menu is closed and the 'menu' icon is clicked - this will add the 'active' class to it
    // The boostrap column classes are increased numerically to maximize the side nav
    mySideNav.classList.add(
      "col-4",
      "col-sm-3",
      "col-md-2",
      "col-lg-2",
      "active"
    );
    // When the sidenav is maximized, the text for the content is now displayed
    sideNavContentOne.classList.replace("d-none", "d-block");
    sideNavContentTwo.classList.replace("d-none", "d-block");
  }
};

// Show the loading spinner upon form submittal for normal Task Form
const showLoadingSpinner = () => {
  const taskButtonIcon = document.querySelector(
    ".todo-page-add-task-form-submit-text"
  );
  taskButtonIcon.classList.add("spinner-border", "text-light");
  taskButtonIcon.innerHTML = "";
  taskButtonAdd.setAttribute("disabled", true);
  taskButtonAdd.setAttribute("role", "status");
  taskButtonAdd.setAttribute("aria-disabled", true);
};

// Show the loading spinner for Important Task Form
const showImportantLoadingSpinner = () => {
  taskButtonIcon.classList.add("spinner-border", "text-light");
  taskButtonIcon.innerHTML = "";
  taskButtonImportantAdd.setAttribute("disabled", true);
  taskButtonImportantAdd.setAttribute("role", "status");
  taskButtonImportantAdd.setAttribute("aria-disabled", true);
};

// TODO - Need to see if it's possible to make this more DRY, since the forms are on two different pages
// This checks if the 'Task' form field is empty
// If it's empty, set stylistic changes to indicate there is a validation error
const validateTaskFormSubmit = () => {
  if (createTaskForm.value === "") {
    taskFormError.innerHTML = "You must enter a value";
    taskFormError.style.color = "red";
    createTaskForm.style.border = "1px solid red";
    return false;
  } else if (createTaskForm.value !== "") {
    showLoadingSpinner();
  }
  taskFormError.innerHTML = "";
};

// This checks if the 'Important Task' form field is empty
// If it's empty, set stylistic changes to indicate there is a validation error
const validateImportantTaskFormSubmit = () => {
  if (createImportantTaskForm.value === "") {
    createImportantTaskFormError.innerHTML = "You must enter a value";
    createImportantTaskFormError.style.color = "red";
    createImportantTaskForm.style.border = "1px solid red";
    return false;
  } else if (createImportantTaskForm.value !== "") {
    showImportantLoadingSpinner();
  }
  createImportantTaskFormError.innerHTML = "";
};
