// This script is used on the dashboard page to handle file upload
document.addEventListener("DOMContentLoaded", function() {
  const uploadForm = document.getElementById("uploadForm");
  if (uploadForm) {
    uploadForm.addEventListener("submit", function(event) {
      event.preventDefault();
      const fileInput = document.getElementById("fileInput");
      if (fileInput.files.length === 0) {
        alert("Please select a file first!");
        return;
      }
      const file = fileInput.files[0];
      let formData = new FormData();
      formData.append("file", file);

      fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
      })
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        // Store the scan results in localStorage and redirect to the output page
        localStorage.setItem("scanResults", JSON.stringify(data));
        window.location.href = "output.html";
      })
      .catch(error => {
        console.error("Error:", error);
        alert("File scanning failed. Please try again.");
      });
    });
  }
});
