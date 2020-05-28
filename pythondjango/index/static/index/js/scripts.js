// Element variables

// Sidenav element ID's
const mySideNav = document.getElementById("mySidenav");
const sideNavContentOne = document.getElementById("sideNavContentOne");
const sideNavContentTwo = document.getElementById("sideNavContentTwo");

// Create Task Form
const createTaskForm = document.getElementById("create-task-form");
// Create Task Form <span> elemement that populates an error message when validation fails
const taskFormError = document.getElementById("task-form-error");

// Create Important Task Form
const createImportantTaskForm = document.getElementById(
  "create-important-task-form"
);
// Create Important Task Form <span> elemement that populates an error message when validation fails
const createImportantTaskFormError = document.getElementById(
  "important-task-form-error"
);

// Login Form username field
const logInFormUsername = document.getElementById("id_username");
// Login Form password field
const logInFormPassword = document.getElementById("id_password");
// Login Form <span> elemement that populates an error message when validation fails
const logInFormError = document.getElementById("login-alert");

// Loading button span - this contains the interior text of the button
const loadingButtonSpan = document.querySelector(".loading-button-span");
// Loading button <button> element
const loadingButton = document.querySelector(".loading-button");

// Toggle option for a slide-out menu
const openNav = () => {
  // If the slide out column is open, and the 'menu' button is clicked again to close it, then shorten the bootstrap column width to minimize it
  if (mySideNav.classList.contains("active")) {
    mySideNav.classList.remove(
      "col-5",
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
    mySideNav.classList.remove("col-2", "col-sm-1", "col-md-1", "col-lg-1");
    mySideNav.classList.add(
      "col-5",
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

// Show the loading spinner for the Login form
const showLoadingSpinner = e => {
  console.log(e);
  e.target.setAttribute("role", "status");
  e.target.setAttribute("aria-disabled", true);
  e.target.classList.add("spinner-border", "text-light", "mx-auto");
  e.target.innerHTML = "";
};

// TODO - Need to see if it's possible to make this more DRY, since the forms are on different pages
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
    showLoadingSpinner();
  }
  createImportantTaskFormError.innerHTML = "";
};

// Validation check for the login form
const validateLogInForm = () => {
  if (logInFormUsername.value === "") {
    logInFormError.innerHTML = "You must enter a value";
    logInFormError.style.color = "red";
    logInFormUsername.style.border = "1px solid red";
    return false;
  } else if (logInFormPassword.value === "") {
    logInFormError.innerHTML = "You must enter a value";
    logInFormError.style.color = "red";
    logInFormPassword.style.border = "1px solid red";
    return false;
  } else if (logInFormUsername.value !== "") {
    showLoadingSpinner();
  }
};
