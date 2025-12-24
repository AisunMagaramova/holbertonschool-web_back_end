// taskFirst funksiyasi yaradilir
function taskFirst (){
	// const istifade edirik cunki sonradan deyeismeyecek
	const task = 'I prefer const when I can.';
	// task deyisen deyeri qaytarir
	return task;
}

// taskNext adli funksiya yatrdilir
function taskNext (){
	let message = 'Let me change it'; // let istifade  olunur

	//combinationadli adli deyisen yaradilir
	//let istifade edirik cunki sonra deyeri deyisdireceyik
	let combination = 'But sometimes let';

	// combination deyisenini deyeri yeniden deyisdiririk 
	combination = message;

	return combination;
}
