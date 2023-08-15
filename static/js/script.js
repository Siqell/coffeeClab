const smoothLinks = document.querySelectorAll("a[href^='#']");
for (let smoothLink of smoothLinks) {
	smoothLink.addEventListener("click", function (e) {
		e.preventDefault();
		const id = smoothLink.getAttribute("href");

		document.querySelector(id).scrollIntoView({
				behavior: "smooth",
				block: "start"
		});
	});
};


const up = document.querySelector('.up');
document.addEventListener('scroll', function () {
	if (window.scrollY > 600){
		up.classList.add('visable');
	}else{
		up.classList.remove('visable');
	};
});


const fixMenu = document.querySelector('.fix-menu');
document.addEventListener('scroll', function () {
	if (window.scrollY > 600){
		fixMenu.classList.add('active');
	}else{
		fixMenu.classList.remove('active');
	};
});