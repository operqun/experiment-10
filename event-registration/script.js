document.getElementById("regForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name     = document.getElementById("name").value.trim();
  const email    = document.getElementById("email").value.trim();
  const phone    = document.getElementById("phone").value.trim();
  const college  = document.getElementById("college").value.trim();
  const event    = document.getElementById("event").value;
  const gender   = document.querySelector('input[name="gender"]:checked');
  const password = document.getElementById("password").value;
  const terms    = document.getElementById("terms").checked;
  const error    = document.getElementById("error");
  const success  = document.getElementById("success");

  error.textContent = "";
  success.textContent = "";

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phonePattern = /^[6-9][0-9]{9}$/;

  if (name === "" || college === "") {
    error.textContent = "Name and College are required.";
  } else if (!emailPattern.test(email)) {
    error.textContent = "Please enter a valid email address.";
  } else if (!phonePattern.test(phone)) {
    error.textContent = "Mobile number must be 10 digits starting with 6-9.";
  } else if (event === "") {
    error.textContent = "Please select an event.";
  } else if (!gender) {
    error.textContent = "Please select your gender.";
  } else if (password.length < 6) {
    error.textContent = "Password must be at least 6 characters.";
  } else if (!terms) {
    error.textContent = "You must accept the terms and conditions.";
  } else {
    success.textContent = "Thank you " + name + "! You are registered for " + event + ".";
    document.getElementById("regForm").reset();
  }
});