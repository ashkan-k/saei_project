// const usernameInput = document.querySelector(".user-input");
// const passwordInput = document.querySelector(".pass-input");
// const usernameMsg = document.querySelector(".Username-msg");
// const passwordMsg = document.querySelector(".Password-msg");
// const signinMsg = document.querySelector(".signin-status");
// const signinBtn = document.querySelector(".signin-button");

// signinBtn.addEventListener("click", signIn);
// function signIn(event) {
// 	usernameMsg.innerText = "";
// 	passwordMsg.innerText = "";
// 	const usernameValue = usernameInput.value;
// 	const passwordValue = passwordInput.value;
// 	let ifSendData = true;

// 	if (usernameValue.length === 0) {
// 		usernameMsg.innerText = "ایمیل معتبر نمیباشد";
// 	}
// 	if (usernameValue.indexOf("@") === -1) {
// 		usernameMsg.innerText = "ایمیل معتبر نمیباشد";
// 	}
// 	if (usernameValue.indexOf(".") === -1) {
// 		usernameMsg.innerText = "ایمیل معتبر نمیباشد";
// 		ifSendData = false;
// 	}
// 	if (passwordValue.length === 0) {
// 		passwordMsg.innerText = "رمز عبور معتبر نمیباشد";
// 		ifSendData = false;
// 	} else if (passwordValue.length <= 4) {
// 		passwordMsg.innerText = "رمز عبور کوتاه است";
// 		ifSendData = false;
// 	}

// 	// if (ifSendData) {
// 	// 	const body = JSON.stringify({
// 	// 		username: usernameValue,
// 	// 		password: passwordValue,
// 	// 	})
// 	// 	const headers = {
// 	// 		"Content-Type": "application/json"
// 	// 	}
// 	// 	fetch('https://jsonplaceholder.typicode.com/posts', {
// 	// 		metod: "POST",
// 	// 		body: body,
// 	// 		headers: headers
// 	// 	})
// 	// 		.then(response => {
// 	// 			if (response.ok) {
// 	// 				signinMsg.innerText = "You signd in seccesfully";
// 	// 			}
// 	// 		})
// 	// }
