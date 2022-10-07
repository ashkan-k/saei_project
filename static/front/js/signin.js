// const phoneNumber = document.querySelector(".phone");
// const emailInput = document.querySelector(".email-input");
// const passInput = document.querySelector(".pass-input");
// const repeatPass = document.querySelector(".repeat-the-password");
// const phoneMsg = document.querySelector(".phone-msg");
// const OneTimePasswordMsg = document.querySelector(".One-time-password-msg");
// const emailMsg = document.querySelector(".email-msg");
// const passMsg = document.querySelector(".password-msg");
// const repeatPassMsg = document.querySelector(".repeat-the-password-msg");
// const signupButton = document.querySelector(".signup-button");
// const signupStatus = document.querySelector(".signup-status");

// signupButton.addEventListener("click", signIn);
// function signIn() {
//     phoneMsg.innerText = "";
//     OneTimePasswordMsg.innerText = "";
//     emailMsg.innerText = "";
//     passMsg.innerText = "";
//     repeatPassMsg.innerText = "";

//     const phoneNumberValue = phoneNumber.value;
//     const emailInputValue = emailInput.value;
//     const passInputValue = passInput.value;
//     const repeatPassValue = repeatPass.value;
//     let ifSendData = true;

//     if (phoneNumberValue.length < 10) {
//         phoneMsg.innerText = "شماره وارد شده اشتباه است";
//     } else if (phoneNumberValue.length = 10) {
//         phoneNumber.style.color = "#32CD32";
//     }

//     if (emailInputValue.length === 0) {
//         emailMsg.innerText = "لطفا ایمیل خود را وارد کنید"
//     }
//     if (emailInputValue.indexOf("@") === -1) {
//         emailMsg.innerText = "ایمیل وارد شده معبتر نمیباشد";
//     } else {
//         emailInput.style.color = "#32CD32";
//     }
//     if (emailInputValue.indexOf(".") === -1) {
//         emailMsg.innerText = "ایمیل وارد شده معبتر نمیباشد";
//     } else {
//         emailInput.style.color = "#32CD32";
//     }

//     if (passInputValue.length < 5) {
//         passMsg.innerText = "رمز عبور کوتاه است";
//     } else if (passInputValue.length >= 5) {
//         passInput.style.color = "#32CD32";
//     }

//     if (repeatPassValue.length < 5) {
//         repeatPassMsg.innerText = "تکرار رمز با <<رمز عبور>> مطابقت ندارد";
//     } else if (repeatPassValue.length >= 5) {
//         repeatPass.style.color = "#32CD32";
//     }
// }