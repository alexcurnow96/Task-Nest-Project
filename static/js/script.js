//wait for the DOM to be fully loaded before executing
document.addEventListener("DOMContentLoaded", function () {
  //get the task list element
  const taskList = document.getElementById("task-list");

  //add a change event listener to the task list
  taskList.addEventListener("change", function (e) {
    //check if the changed element is a checkbox
    if (e.target.classList.contains("task-checkbox")) {
      //get the task id from the checkbox's data
      const taskId = e.target.dataset.taskId;
      //get the csrf token from the page
      const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      
      //send a post request to toggle the task status
      fetch(`/toggle-task/${taskId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            //if successful toggle the completed class on the task title
            const taskTitle = e.target.nextElementSibling;
            taskTitle.classList.toggle("completed", data.completed);
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  });
});



//get the menu toggle and sidebar elements
const menu_toggle = document.querySelector(".menu-toggle");
const sidebar = document.querySelector(".sidebar");

//add a click event listener to the menu toggle
menu_toggle.addEventListener("click", () => {
  //toggle the 'is-active' class on both menu toggle and sidebar
  menu_toggle.classList.toggle("is-active");
  sidebar.classList.toggle("is-active");
});




//get all elements with the hoverable class and the popup element
const hoverables = document.querySelectorAll('.hoverable');
const popup = document.getElementById('popup');

//add event listeners to each hoverable element
hoverables.forEach(element => {
  //show popup on mouseover
  element.addEventListener('mouseover', (event) => {
    //set popup text content from attribute
    popup.textContent = event.target.getAttribute('data-popup');
    //display the popup
    popup.style.display = 'block';
    //get the position of the hover element
    const rect = event.target.getBoundingClientRect();
    //reposition the popup below the hovered element
    popup.style.left = `${rect.left}px`;
    popup.style.top = `${rect.bottom + window.scrollY}px`;
  });
  //hide popup on mouseout
  element.addEventListener('mouseout', () => {
    popup.style.display = 'none';
  });
});