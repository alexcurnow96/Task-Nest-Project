document.addEventListener("DOMContentLoaded", function () {
  const taskList = document.getElementById("task-list");

  taskList.addEventListener("change", function (e) {
    if (e.target.classList.contains("task-checkbox")) {
      const taskId = e.target.dataset.taskId;
      const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;

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
            const taskTitle = e.target.nextElementSibling;
            taskTitle.classList.toggle("completed", data.completed);
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  });
});

const menu_toggle = document.querySelector(".menu-toggle");
const sidebar = document.querySelector(".sidebar");

menu_toggle.addEventListener("click", () => {
  menu_toggle.classList.toggle("is-active");
  sidebar.classList.toggle("is-active");
});


const hoverables = document.querySelectorAll('.hoverable');
const popup = document.getElementById('popup');

hoverables.forEach(element => {
  element.addEventListener('mouseover', (event) => {
    popup.textContent = event.target.getAttribute('data-popup');
    popup.style.display = 'block';
    const rect = event.target.getBoundingClientRect();
    popup.style.left = `${rect.left}px`;
    popup.style.top = `${rect.bottom + window.scrollY}px`;
  });

  element.addEventListener('mouseout', () => {
    popup.style.display = 'none';
  });
});