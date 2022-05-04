const password = document.getElementById("password");
const passwordConfirm = document.getElementById("confirmPassword");

passwordConfirm.addEventListener("keyup", function (event) {
  const Orgvalue = password.value;
  const Confirmvalue = passwordConfirm.value;
  const helper = document.getElementById("confirm-helper");
  if (Orgvalue !== Confirmvalue) {
    if (Confirmvalue.length < 8) {
      helper.setAttribute(
        "data-error",
        "Password must be at least 8 characters!"
      );
    } else {
      helper.setAttribute("data-error", "Password must be same!");
    }
    passwordConfirm.classList.remove("valid");
    passwordConfirm.classList.add("invalid");
  } else {
    passwordConfirm.classList.remove("invalid");
    passwordConfirm.classList.add("valid");
  }
});

function validate() {
  const inputs = document.getElementsByTagName("input");
  let count = 0;
  inputs.forEach((element) => {
    const classList = element.classList;
    classList.includes("valid") ? (count += 1) : count;
  });
  if (count == 5) {
    console.log("Yes!");
    return true;
  } else {
    console.log("No!");
    return false;
  }
}

document.getElementById("register-form").onsubmit = validate;
